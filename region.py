from ParseCampaign import Parser
from Battle import Battle as Arena
from Character import Character
from CharacterArray import CharacterArray
import os

clear = lambda: os.system("cls")


class Region:
    def __init__(self, filepath=""):
        self.region_file = Parser(filepath)
        self.arena = Arena()
        self.keywords = ['skirmish', 'battle']
        self.characters = CharacterArray()
        self.characters, self.campaign, self.credits = self.region_file.parse_file()

    def findKeyword(self, lineIN=""):
        for keyword in self.keywords:
            if lineIN.find(keyword) != -1:
                return True
        return False

    def getKeyword(self, lineIN=""):
        for keyword in self.keywords:
            if lineIN.find(keyword) != -1:
                return keyword
        return -1

    def get_fighters(self, lineIN=""):
        partitions = self.region_file.split_line(lineIN, " => ")
        fighter1, fighter2 = self.region_file.split_line(str(partitions[1]), ", ")

        if fighter1.endswith("\n"):
            fighter1 = str(fighter1[:len(fighter1) - 1])
        if fighter2.endswith("\n"):
            fighter2 = str(fighter2[:len(fighter2) - 1])

        return str(fighter1), str(fighter2)

    def doFunction(self, keyword="", lineIN=""):
        if keyword == "skirmish":
            fighters = self.get_fighters(lineIN)
            self.arena.skirmish(self.characters.get(fighters[0]), self.characters.get(fighters[1]))
        elif keyword == "battle":
            fighters = self.get_fighters(lineIN)
            self.arena.battle(self.characters.get(fighters[0]), self.characters.get(fighters[1]))

    def game_loop(self):
        for line in self.campaign:
            if self.findKeyword(str(line)):
                self.doFunction(self.getKeyword(line), line)
                nextLine = input(">")
                clear()
            else:
                print(line)
                nextLine = input(">")
                clear()

        for credit in self.credits:
            clear()
            print("Credits:")
            print(credit)
            gameOver = input(">")


overWorld = Region("testParser")
overWorld.game_loop()

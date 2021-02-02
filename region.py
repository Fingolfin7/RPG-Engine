from ParseCampaign import Parser
from Battle import Battle as Arena
from CharacterArray import CharacterArray
import threading
from FormatText import format_text
import Music
import os


clear = lambda: os.system("cls")


class Region:
    def __init__(self, filepath=""):
        self.region_file = Parser(filepath)
        self.arena = Arena()
        self.keepMusicOn = True
        self.keywords = ['music', 'skirmish', 'battle']
        self.characters = CharacterArray()
        self.characters, self.campaign, self.atmosphere, self.credits = self.region_file.parse_file()

    @staticmethod
    def cleanString(lineIn=""):
        if lineIn.endswith("\n"):
            lineIn = str(lineIn[:len(lineIn) - 1])
        return str(lineIn)

    def hasKeyword(self, lineIN=""):
        for keyword in self.keywords:
            if lineIN.__contains__(keyword):
                return True
        return False

    def getKeyword(self, lineIN=""):
        for keyword in self.keywords:
            if lineIN.__contains__(keyword):
                return keyword
        return -1

    def get_args(self, lineIN=""):
        partitions = self.region_file.split_line(lineIN, " => ")
        fighter1, fighter2 = self.region_file.split_line(str(partitions[1]), ", ")

        return self.cleanString(str(fighter1)), self.cleanString(str(fighter2))

    def doFunction(self, keyword="", lineIN=""):
        returnValue = None
        if keyword.lower().__contains__("skirmish"):
            fighters = self.get_args(lineIN)
            returnValue = self.arena.skirmish(self.characters.get(fighters[0]), self.characters.get(fighters[1]))

        elif keyword.lower().__contains__("battle"):
            fighters = self.get_args(lineIN)
            returnValue = self.arena.battle(self.characters.get(fighters[0]), self.characters.get(fighters[1]))

        elif keyword.lower().__contains__("music"):
            partitions = self.region_file.split_line(lineIN, " => ")
            music_thread = threading.Thread(target=Music.play_song, args=(self.cleanString(partitions[1]),))
            music_thread.start()
            clear()

        return returnValue

    def game_loop(self):
        returnValue = None
        if len(self.atmosphere) > 0:
            for line in self.atmosphere:
                if self.hasKeyword(str(line)):
                    self.doFunction(self.getKeyword(line), line)
        clear()

        if len(self.campaign) > 0:
            for line in self.campaign:
                if self.hasKeyword(str(line)):
                    returnValue = self.doFunction(self.getKeyword(line), line)
                    input(">")
                    clear()
                else:
                    if str(line) != "\n":
                        print(self.cleanString(line))
                    else:
                        input(">")
                        clear()

        self.keepMusicOn = False

        if len(self.credits) > 0:
            clear()
            print("Credits:")
            for credit in self.credits:
                print(credit)
            input(">")

        return returnValue

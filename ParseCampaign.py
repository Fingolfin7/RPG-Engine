from Character import Character
from Battle import Battle as Arena
from CharacterArray import CharacterArray


class Parser:

    def __init__(self, filepath=""):
        self.campaignfile = open(filepath, 'r')
        self.all_lines = self.campaignfile.readlines()

    @staticmethod
    def split_line(lineIN="", seperator=""):
        partitions = str(lineIN).partition(seperator)
        return str(partitions[0]), str(partitions[2])

    @staticmethod
    def parse_character_stats(Character_line):
        stats_arr = []
        stats = str(Character_line).partition(" ")

        stats_arr.append(int(stats[0]))

        stats = str(stats[2]).partition(" ")

        stats_arr.append(int(stats[0]))
        stats_arr.append(int(stats[2]))

        return stats_arr

    def parse_file(self):
        character_dictionary = CharacterArray()
        character_section = []
        campaign_section = []
        credits_section = []
        section = str

        for line in self.all_lines:
            if line.find("#Characters") != -1:
                section = "#Characters"
            elif line.find("#Campaign") != -1:
                section = "#Campaign"
            elif line.find("#Credits") != -1:
                section = "#Credits"

            if section == "#Characters":
                character_section.append(line)
            elif section == "#Campaign":
                campaign_section.append(line)
            if section == "#Credits":
                credits_section.append(line)

        character_section.pop(0)
        campaign_section.pop(0)
        credits_section.pop(0)

        if len(character_section) > 0:

            for character in character_section:
                name_key, stats_string = self.split_line(character, ": ")

                health, strength, block = self.parse_character_stats(stats_string)

                New_character = Character(name_key, health, strength, block)
                # print(New_character)
                character_dictionary.addCharacter(New_character)

        return character_dictionary, campaign_section, credits_section

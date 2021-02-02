from region import Region
import os


clear = lambda: os.system("cls")
clear()


def makechoice(options=[], returnType=""):
    convertDict = {
        "int": lambda line="": int(line),
        "str": lambda line="": line,
        "string": lambda line="": line,
    }

    for i in options:
        print(i)

    try:
        return convertDict.get(returnType)(input(">"))
    except ValueError:
        print("Invalid Input! {} expected!".format(returnType))
        return makechoice(options, returnType)


def main():
    Ascefelia = Region("Ascefelia Campaign\Ascefelia")
    Ascefelia1 = Region("Ascefelia Campaign\Ascefelia1")
    Ascefelia.game_loop()

    choice = makechoice(["1.Could I say no to such an adventure?", "2.Ah, I'll come back another time..."], "int")

    if choice == 1:
        if Ascefelia1.game_loop() == "End":
            print("Game Over")
            input(">")
    else:
        print("Wise decision. Now flee,")
        print("flee before they find you!")
        input(">")


main()


'''
clear()
myArena = Arena()
Ozymandius = Character("Ozymandius", 100, 100, 100)
Phlebas = Character("Phlebas", 100, 100, 100)

myArena.battle(Ozymandius, Phlebas)
'''
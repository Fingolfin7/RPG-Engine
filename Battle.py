import os


class Battle:
    @staticmethod  # used for methods that don't use 'self'  (i think)
    def getAttack(attacker, defender):
        attack = attacker.attack()
        block = defender.getBlock()
        damage = attack - block

        if damage >= 0:
            defender.health -= damage

        print("{} attacked with {} force!".format(attacker.name, attack))
        print("{} blocked with {} block!".format(defender.name, block))
        print("{}'s health -> {}".format(defender.name, defender.health))
        print()

        if defender.health <= 0:
            print("{} has died, {} is victorious!".format(defender.name, attacker.name))
            return "End"
        else:
            return "the fight will continue!"

    def battle(self, fighter1, fighter2):
        while True:
            if self.getAttack(fighter1, fighter2) == "End":
                break
            nextLine = input(">")
            os.system("cls")
            if self.getAttack(fighter2, fighter1) == "End":
                break
            nextLine = input(">")
            os.system("cls")

    def skirmish(self, fighter1,  fighter2, rounds=2):
        for i in range(rounds):
            if i % 2 == 0:
                if self.getAttack(fighter1, fighter2) == "End":
                    break
            else:
                if self.getAttack(fighter2, fighter1) == "End":
                    break
            nextLine = input(">")
            os.system("cls")

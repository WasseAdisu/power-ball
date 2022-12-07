# ### lottory machine

import random
import colors


class Lotery:
    def __init__(self):
        self.whiteuser = []
        self.whitepicku = []
        self.pick = random.randint(1, 10)
        self.x = random.randint(1, 10)
        self.intersection_set = []

    def filter(self):
        for i in range(5):
            ab = random.randint(1, 20)
            nb = random.randint(1, 20)
            self.whitepicku.append(nb)
            self.whiteuser.append(ab)


class intersec(Lotery):
    def select(self):
        self.intersection_set = len(set(self.whiteuser).intersection(set(self.whitepicku)))


    def show(self):
        white = " "
        for i in self.whiteuser:
            white += str(f" {i} ")

        whitel = " "
        for j in self.whitepicku:
                whitel += str(f" {j} ")
        print("Today’s Powerball winning numbers:", colors.BLUE, (white), colors.MAGENTA, (self.pick), colors.RESET)
        print("your lucky numbers:", colors.BLUE, (whitel), colors.MAGENTA, (self.x))

    def result(self):
        if self.intersection_set == 5 and self.pick == self.x:
            print(colors.YELLOW, "Correct White Balls and the Powerball: Jackpot $324,000,000")
        elif self.intersection_set == 5 and self.pick != self.x:
            print(colors.WHITE, "5 Correct White Balls, but no Powerball: $1,000,000")
        elif self.intersection_set == 4 and self.pick == self.x:
            print(colors.GREEN, "4 Correct White Balls and the Powerball: Jackpot $10,000")
        elif self.intersection_set == 4 and self.pick != self.x:
            print(colors.WHITE, "4 Correct White Balls, but no Powerball: $100")
        elif self.intersection_set == 3 and self.pick == self.x:
            print(colors.BLACK, "3 Correct White Balls and the Powerball: Jackpot $100")
        elif self.intersection_set == 3 and self.pick != self.x:
            print(colors.CYAN, "3 Correct White Balls, but no Powerball: $7")
        elif self.intersection_set == 2 and self.pick == self.x:
            print("2 Correct White Balls and the Powerball: $7")
        elif self.intersection_set == 1 and self.pick == self.x:
            print(colors.WHITE, "1 Correct White Ball and the Powerball: $4")
        elif self.intersection_set == 0 and self.pick == self.x:
            print(colors.WHITE, "No White Balls, Just the Powerball: $4")
        else:
            print(colors.YELLOW, "Not lucky \n try again!")


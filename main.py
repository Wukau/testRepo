import itertools
import math


class Bet():
    def __init__(self, index, name, odds):
        self.index = index
        self.name = name
        self.odds = odds

    @staticmethod
    def input_bets():
        bets_in = []
        end = False
        i = 0

        while not end:
            bets_in.append(Bet(i, input("Nazwa zakładu: "), int(input("Kurs: "))))
            i += 1

            while end != 'Y' and end != 'N':
                end = input("Czy to ostatni zakład? [Y/N]")
                end = end.upper()
                print(end)

            end = True if end == 'Y' else False

        return bets_in

    @classmethod
    def combinations(cls, bets):
        # '''
        #
        #
        # :param
        # bets: list
        #     Need to know how many bets we have to make all kind of combination
        #
        # :return:
        # Function returns:
        # kind_of_combination : list
        #     kind of diffrent combination there will be
        #         fe. if there are 3 diffrent bets the list kind_of_bets will return [(0,), (1,), (2,), (0, 1), (0, 2),
        #         (1, 2), (0, 1, 2)]
        # amount : list
        #     how many combination there will be
        #         fe. if there are 3 diffrent bets the list amount will return seven's 1 [1, 1, 1, 1, 1, 1, 1]
        # '''
        kind_of_combinations = []
        amount = []

        for i in range(1, len(bets) + 1):
            for subset in itertools.combinations([bets[x].index for x in range(len(bets))], i):
                kind_of_combinations.append(subset)
                amount.append(1)

        num = 0
        for i in kind_of_combinations:
            for j in list(i): amount[num] = amount[num] * bets[j].odds
            num += 1
        amount = [round(amount[x], 2) for x in range(len(amount))]

        count_of_bets = []
        for j in range(1, len(bets) + 1):
            count_of_bets.append(int(math.factorial(len(bets)) / (math.factorial(j) * (math.factorial(len(bets) - j)))))

        stake = []
        k = 0
        for i in range(len(count_of_bets)):
            stake.append(float(input("Stawka na " + text(i) + ": ")))
            for y in range(k, count_of_bets[i] + k):
                amount[y] *= stake[i]

            stake[i] = 0
            for x in range(k, count_of_bets[i] + k):
                stake[i] += amount[x]
                k += 1

        for i in range(len(bets)):
            if i == 0:
                print("Ilość Singli = " + str(count_of_bets[i]) + " Maksymalna Wygrana = " + str(stake[i]))
            elif i == 1:
                print("Ilość Dubli = " + str(count_of_bets[i]) + " Maksymalna Wygrana = " + str(stake[i]))
            elif i == 2:
                print("Ilość Trebli = " + str(count_of_bets[i]) + " Maksymalna Wygrana = " + str(stake[i]))
            else:
                print("Ilość " + str(i + 1) + ". Zdarzeń = " + str(count_of_bets[i]) + " Maksymalna Wygrana = " + str(
                    stake[i]))

        return kind_of_combinations, amount, count_of_bets, stake

    def __repr__(self):
        return "Index %d Nazwa zakładu: %s Kurs: %d" % (self.index, self.name, self.odds)


def text(i):
    if i == 0:
        return "Single"
    elif i == 1:
        return "Duble"
    elif i == 2:
        return "Treble"
    elif i == 3:
        return "4 Zdarzenia"
    else:
        return str(i + 1) + "Zdarzeń"


bet1 = Bet(0, "zakład1", 2)
bet2 = Bet(1, "zakład2", 10)
bet3 = Bet(2, "zakład3", 2)
bet4 = Bet(3, "zakład4", 4)
bet5 = Bet(4, "zakład5", 5)
bet = Bet(0, "0", 0)
# bets = [bet.input_bets()]
bets = Bet.input_bets()

print(bets)



# kind_of_combinations, amount, count_of_bets, stake = Bet.combinations(bets)
# print(kind_of_combinations, amount, count_of_bets, stake)



# kind_of_combinations, amount, count_of_bets, stake = combinations(bets)

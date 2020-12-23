import random

def diceRoll():
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    return die1+die2

def pointGame(roll_1):
    finished = False
    i = 2
    while(finished == False):
        roll_i = diceRoll()
        #print(str(i) + " roll:" + str(roll_i))
        if(roll_1 == roll_i):
            return True, i
        if(roll_i == 7):
            return False, i
        i += 1

def crapsGame(iter):
    wins = 0
    losses = 0
    for i in range(iter):
        num_rolls = 1
        roll = diceRoll()
        #print("1 roll:" + str(roll))

        if num_rolls == 1 and (roll == 7 or roll == 11):
            #print("player won on 1st roll")
            wins += 1
        elif num_rolls == 1 and (roll == 2 or roll == 3 or roll == 12):
            #print("player lost on 1st roll")
            losses += 1
        else:
            status, i = pointGame(roll)
            if status == True:
                #print("player won on " + str(i) + " roll")
                wins += 1
            else:
                #print("player lost on " + str(i) + " roll")
                losses +=1

    print("wins:" + str(wins))
    print("losses:" + str(losses))
    print("P(W) = " + str(wins/iter))
    print("P(L) = " + str(losses/iter))


crapsGame(100000)
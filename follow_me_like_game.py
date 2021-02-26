import sys, select
import random, string

def winningMessage():
    print("You are champion")

def losingMessage():
    print("Game Over!! Better Luck Next Time")


#function to start the game
def startGame(second, score, lifes):
    #base case to end game if life is 0
    if(lifes<=0 or score<-3):
        losingMessage()
        return

    if(score>=10):
        winningMessage()
        return

    randomCharacter = random.choice(string.ascii_lowercase)
    print (f"You have {second} seconds to answer!")
    print (f"Press {randomCharacter} ")
    i, o, e = select.select( [sys.stdin], [], [], second )

    #if the user has pressed a button
    if(i):
        #restoring lifes once user presses anything
        lifes = 3
        
        userInput = sys.stdin.readline().strip()
        if(userInput==randomCharacter):
            score = score+1
            print(f"Yiee!! Your Score is: {score}")
            startGame(second,score,lifes)
        else:
            score = score-1
            print(f"Invalid Input :< Your Score is: {score}")
            startGame(second,score,lifes)
    else:
        lifes = lifes - 1
        print(f"You Entered Nothing, You have {lifes} lifes left")
        startGame(second,score,lifes)


def main():
    startGame(5, 0, 3) #first argument is time & second argumner is score  & third argument is number of lifes

if __name__ == "__main__":
    main()
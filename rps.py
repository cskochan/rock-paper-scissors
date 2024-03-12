import random

def main():
    name = intro()
    winner = game(name)
    print(f"Thanks for playing. Looks like {winner} won! Good game!")

def intro() -> None:
    print("Welcome to Rock Paper Scissors. What's your name?")
    name = input("> ")
    print(f"Welcome {name}. The rules are simple. Scissors cut Paper, Paper covers Rock, Rock smashes Scissors.")
    print("Oh, and if you ever get tired of playing, just type Exit, and we'll call it quits. Ready?")
    ready = input("> ").lower()
    if ready in ("y", "yes", "yeah"):
        print("Good.\n")
    elif ready in ("n", "no", "nah"):
        print("Too bad.\n")
    else:
        print("What? Nevermind, just play the game.\n")
    return name

def game(name) -> None:
    pScore = cScore = 0
    sign = ["Rock", "Paper", "Scissors"]
    pRock = pPaper = pScissors = 1 # Weight of computer choice can't total 0
    while(True):
        print("*****    ****   ***  ** * **  ***   ****    *****")
        print(f"{name}: {pScore}\t\tComputer: {cScore}")
        print("*****    ****   ***  ** * **  ***   ****    *****")
        print("Rock Paper Scissors Shoot!")
        w = computeWeights(pRock, pPaper, pScissors)
        #print(f"Weights: Rock - {w[0]}, Paper - {w[1]}, Scissors - {w[2]}")
        cThrow = random.choices(sign, weights=(w[2], w[0], w[1]), k=1)[0]
        pThrow = input("> ").capitalize()
        # Count number of times thrown for weight of computer choice on next round
        if pThrow == "Rock": pRock += 1
        elif pThrow == "Paper": pPaper += 1
        elif pThrow == "Scissors": pScissors += 1
        print(f"Computer: {cThrow}\n")
        if pThrow == "Exit":
            # determine who won for closing statement in main()
            if pScore - cScore < 0: winner = "the computer"
            elif pScore - cScore > 0: winner = "you"
            elif pScore - cScore == 0: winner = "nobody"
            return winner
        elif pThrow in sign:
            if sign.index(cThrow) - sign.index(pThrow) in (-1, 2):
                print(f"{name} wins!")
                pScore += 1
            elif sign.index(cThrow) - sign.index(pThrow) in (-2, 1):
                print("Computer wins!")
                cScore += 1
            else:
                print("Tie!")
        else:
            print("Unintelligable. Lets try again.")

# simple weighting system just for fun
def computeWeights(rock, paper, scissors) -> tuple:
    total = rock + paper + scissors
    pRock = (rock/total)
    pPaper = (paper/total)
    pScissors = (scissors/total)
    return pRock, pPaper, pScissors

if __name__ == "__main__":
    main()
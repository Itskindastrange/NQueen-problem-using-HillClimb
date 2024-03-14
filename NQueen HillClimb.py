from random import randint as random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

prob = 0

def getRandState(prob):
    return[random(0, prob-1) for _ in range(prob)]

def Neighbours(currState):
    neighbours = []
    temp = len(currState)
    for i in range(temp):
        for j in range(temp):
            if j != currState[i]:
                n = list(currState)
                n[i] = j
                neighbours.append(n)
    return neighbours

def checkAttack(currState):
    temp = len(currState)
    attackCounter = 0
    for i in range(temp):
        for j in range(i+1, temp):
            if currState[i] == currState[j] or abs(currState[i] - currState[j]) == abs(i - j):
                attackCounter += 1
    return attackCounter

def HillClimb(prob, max_restarts=100):
    for _ in range(max_restarts):
        currState = getRandState(prob)
        currVal = checkAttack(currState)

        while True:
            neighbours = Neighbours(currState)
            bestNeigh = None
            bestVal = currVal

            for i in neighbours:
                neighbourVal = checkAttack(i)
                if neighbourVal < bestVal:
                    bestNeigh = i
                    bestVal = neighbourVal

            if bestVal >= currVal:
                break

            currState = bestNeigh
            currVal = bestVal

        if currVal == 0:
            return currState

    return currState

def printBoard(state):
    n = len(state)
    chessboard = [['0'] * n for _ in range(n)]

    for i in range(n):
        chessboard[state[i]][i] = 'Q'

    for row in chessboard:
        print(' '.join(row))

def NQueen(prob):
    solution = HillClimb(prob)
    print("\nTextual representation of the chessboard:")
    printBoard(solution)
    plot_board(solution)

def plot_board(state):
    n = len(state)
    chessboard = [[0] * n for _ in range(n)]

    for i in range(n):
        chessboard[state[i]][i] = 1

    custom_cmap = ListedColormap(['green', 'white'])

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

    ax1.imshow(chessboard, cmap=custom_cmap)
    ax1.set_title(f'Chessboard with {prob} Queens')
    ax1.set_xticks(range(n))
    ax1.set_yticks(range(n))

    for i in range(n):
        ax2.text(i, state[i], 'Q', ha='center', va='center', color='black', fontsize=20)
    ax2.set_title(f'Textual Representation of {prob} Queens')
    ax2.set_xticks(range(n))
    ax2.set_yticks(range(n))
    ax2.set_xlim(-0.5, n-0.5)
    ax2.set_ylim(n-0.5, -0.5)
    ax2.grid(True)

    plt.tight_layout()
    plt.show()

prob = int(input("\nEnter the number of queens (for example 4 or 8): "))
NQueen(prob)

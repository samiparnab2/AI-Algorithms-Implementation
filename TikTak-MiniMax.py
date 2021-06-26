import MinMax as mm
import copy


def whoseMove(state):
    count1=0
    count2=0
    for x in state:
        count1+=x.count(1)
        count2+=x.count(2)
    if count2==count1:
        return 1
    else:
        return 2


def createChildren(state):
    player=whoseMove(state)
    children=[]
    tmp=copy.deepcopy(state)
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j]==0:
                tmp[i][j]=player
                children.append(tmp)
                tmp=copy.deepcopy(state)
    return children
            
def maxProfit(state):
    global playermax,playermin
    if isGameOver(state)==playermax:
        return 5
    elif isGameOver(state)==playermin:
        return -5
    elif isGameOver(state)==0:
        return 0
    



def printPlay(state):
    print("choose a number to play your move at that position")
    for i in range(3):
        for j in range(i*3+1,(i+1)*3+1):
            print(j,end=" ")
        
        print("\t\t",end="")
        for j in range(3):
            if state[i][j]==0:
                print("-",end=" ")
            elif state[i][j]==1:
                print("X",end=" ")
            elif state[i][j]==2:
                print("0",end=" ")
        print()
    print("----------------------------------------------------------")

def isGameOver(state):
    for x in range(1,3):
        for i in state:
            if i.count(x)==3:
                return x
    for x in range(1,3):
        for i in range(len(state[0])):
            if state[:][i].count(x)==3:
                return x
    for x in range(1,3):
        if state[0][0]==x and state[1][1]==x and state[2][2]==x:
            return x
    
    cnt0=0
    for x in state:
        cnt0+=x.count(0)
    if cnt0==0:
        return 0
    return -1

def changeState(state,move):
    move-=1
    i=move//3
    j=move%3
    if move>8 or move<0 or state[i][j]!=0:
        return None
    state[i][j]=whoseMove(state)
    return state


choice=int(input("1>Player First\n2>Computer First\n"))
currentState=[[0,0,0],[0,0,0],[0,0,0]]
if choice==1:
    playermax=2
    playermin=1
    printPlay(currentState)
    move=int(input())
    newstate=changeState(currentState,move)
    while newstate==None:
        move=int(input("wrong input try again: "))
        newstate=changeState(currentState,move)
    currentState=newstate


elif choice==2:
    playermax=1
    playermin=2
minimaxbrain=mm.MiniMax(currentState,createChildren,maxProfit)
minimaxbrain.buildTree()
minimaxbrain.estimateProfit()
# minimaxbrain.show()
print(currentState)
currentState=minimaxbrain.play(currentState)
print(currentState)
print("isgameover=",isGameOver(currentState),currentState)
while isGameOver(currentState)==-1:
    printPlay(currentState)
    move=int(input())
    newstate=changeState(currentState,move)
    while newstate==None:
        move=int(input("wrong input try again: "))
        newstate=changeState(currentState,move)
    currentState=newstate
    if isGameOver(currentState)==playermin:
        printPlay(currentState)
        print("GAME OVER...TOU WON!")
        break
    currentState=minimaxbrain.play(currentState)
    if isGameOver(currentState)==playermax:
        printPlay(currentState)
        print("GAME OVER...COMPUTER WON!")
        break
if isGameOver(currentState)==0:
    printPlay(currentState)
    print("GAMO OVER")
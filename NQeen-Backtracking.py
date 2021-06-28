import sys
import copy
def nqeenbacktrack(board,queenno):
    if queenno<=0:
        return board,True
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j]==0 and colliding(board,i,j,queenno)==False:
                board[i][j]=queenno
                finalboard,success=nqeenbacktrack(board,queenno-1)
                if success==False:
                    board[i][j]=0
                elif success==True:
                    return finalboard,True
    return board,False

def colliding(board,i,j,qn):
    row=len(board)
    col=len(board[0])
    if board[i].count(0)!=col:
        return True
    for t in range(row):
        if board[t][j]!=0:
            return True
    row-=1
    col-=1
    tmpi=i
    dfj=0
    board[tmpi][j-dfj]
    while tmpi>=0:
        if j-dfj>=0:
            if board[tmpi][j-dfj]!=0:
                return True
        if j+dfj<=col:
            if board[tmpi][j+dfj]!=0:
                return True
        dfj+=1
        tmpi-=1
    tmpi=i
    dfj=0
    while tmpi<=row:
        if j-dfj>=0:
            if board[tmpi][j-dfj]!=0:
                return True
        if j+dfj<=col:
            if board[tmpi][j+dfj]!=0:
                return True
        dfj+=1
        tmpi+=1
    return False

        

board=[[0 for j in range(4)]  for i in range(4)]
newboard,succ=nqeenbacktrack(board,4)
for i in range(len(newboard)):
    for j in range(len(newboard[i])):
        if newboard[i][j]==0:
            print('_',end=",")
        else:
            print(newboard[i][j],end=",")
    print()


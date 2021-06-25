import HillClimbing as hc
import numpy as np

if __name__=="__main__":

    def createChildren(state):
        r,c=state.shape
        for i in range(state.shape[0]):
            for j in range(state.shape[1]):
                if state[i,j]==0:
                    pi=i
                    pj=j
        children=[]
        if pi+1<r :
            t=state+0
            t[pi,pj],t[pi+1,pj]=t[pi+1,pj],t[pi,pj]
            children.append(t)
        if pi-1>=0 :
            t=state+0
            t[pi,pj],t[pi-1,pj]=t[pi-1,pj],t[pi,pj]
            children.append(t)
        if pj+1<c :
            t=state+0
            t[pi,pj],t[pi,pj+1]=t[pi,pj+1],t[pi,pj]
            children.append(t)
        if pj-1>=0 :
            t=state+0
            t[pi,pj],t[pi,pj-1]=t[pi,pj-1],t[pi,pj]
            children.append(t)
        return children

    def heuristic(state1,state2):
        return np.sum((state2-state1)!=0)

    
    # start=np.arange(0,9)
    # np.random.shuffle(start)
    # start=start.reshape(3,3)
    # print(start)
    start=np.array([[0,1,3],[4,2,5],[7,8,6]])
    # start=np.array([[1,0,2],[4,6,7],[8,5,3]])
    goal=np.array([[1,2,3],[4,5,6],[7,8,0]])
    b=hc.HillClimb(start,goal,createChildren,heuristic)
    b.search()
    b.printPath()
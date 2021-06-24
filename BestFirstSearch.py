import numpy as np
import math

class MinHeap:
    def __init__(self):
        self.heap=[None]
        self.length=0
    def lchild(self,index):
        l=index*2
        if l>self.length:
            return None
        return index*2
    def rchild(self,index):
        r=(index*2)+1
        if r>self.length:
            return None
        return (index*2)+1
    def parent(self,index):
        p=index//2
        if p<=1:
            return None
        return p
    def heapify(self,index): 
        if self.length<index:
            return           
        l=self.lchild(index)
        min=index
        if l!=None and self.heap[l].key<self.heap[min].key:
            min=l
        r=self.rchild(index)
        if r!=None and self.heap[r].key<self.heap[min].key:
            min=r
        if min!=index:
            self.heap[min],self.heap[index]=self.heap[index],self.heap[min]
            self.heapify(min)
        else :
            return

    def insert(self,node):
        self.heap.append(node)
        self.length+=1
        i=self.length
        while self.parent(i)!=None and self.heap[i].key<self.heap[self.parent(i)].key:
            self.heap[i],self.heap[self.parent(i)]=self.heap[self.parent(i)],self.heap[i]
            i=self.parent(i)
    def delete(self):
        if self.length==0:
            return None
        self.heap[1],self.heap[self.length]=self.heap[self.length],self.heap[1]
        val=self.heap.pop()
        self.length-=1
        self.heapify(1)
        return val

class Node():
    def __init__(self,value,key=math.inf,parent=None):
        self.value=value
        self.key=key
        self.parent=parent
    
class BestFirstSearch():
    def __init__(self,startState,goalState,createChildren,heuristic):
        self.startState=Node(startState)
        self.goalState=Node(goalState)
        self.createChildren=createChildren
        self.heuristic=heuristic
        self.open=MinHeap()
        self.closed=[]
        self.pathFound=False

    def search(self):
        self.open.insert(self.startState)
        while self.open.length>0:
            current=self.open.delete()
            self.closed.append(current)
            if np.array_equal(current.value,self.goalState.value):   
                self.pathFound=True             
                return
            childrenval=self.createChildren(current.value)
            for i in childrenval:
                if self.isClosed(i)!=True:
                    self.open.insert(Node(i,self.heuristic(i,self.goalState.value),current))
    
    def isClosed(self,val):
        for i in self.closed:
            if np.array_equal(i.value,val):
                return True
        return False

    def printPath(self):    
        if self.pathFound==False:
            print("No solution found")
            return
        path=[]
        current=self.closed[len(self.closed)-1]
        while np.array_equal(current.value,self.startState.value)!=True:
            path.append(current.value)
            current=current.parent
        path.reverse()
        for i in path:
            print(i,end="\n\n")


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


    start=np.arange(0,9).reshape(3,3)
    # start=np.array([[0,1,3],[4,2,5],[7,8,6]])
    goal=np.array([[1,2,3],[4,5,6],[7,8,0]])
    b=BestFirstSearch(start,goal,createChildren,heuristic)
    b.search()
    b.printPath()


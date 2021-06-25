import math

class Node():
    def __init__(self,value,key=math.inf,parent=None):
        self.value=value
        self.key=key
        self.parent=parent
    
class HillClimb():
    def __init__(self,startState,goalState,createChildren,heuristic):
        self.startState=Node(startState)
        self.goalState=Node(goalState)
        self.createChildren=createChildren
        self.heuristic=heuristic
        self.closed=[]
        self.pathFound=False

    def search(self):
        current=self.startState
        while True:
            self.closed.append(current)
            if self.heuristic(current.value,self.goalState.value)==0:   
                self.pathFound=True             
                return
            childrenval=self.createChildren(current.value)
            found=False
            for i in childrenval:
                if self.isClosed(i)!=True and self.heuristic(current.value,self.goalState.value)>self.heuristic(i,self.goalState.value):
                    current=Node(i,self.heuristic(i,self.goalState.value),current)
                    found=True
                    break
            if found==False:
                return

    
    def isClosed(self,val):
        for i in self.closed:
            if self.heuristic(i.value,val)==0:
                return True
        return False

    def printPath(self):    
        if self.pathFound==False:
            print("No solution found")
            return
        path=[]
        current=self.closed[len(self.closed)-1]
        while self.heuristic(current.value,self.startState.value)!=0:
            path.append(current.value)
            current=current.parent
        path.reverse()
        print("Start=>")
        print(current.value)
        print("---------------------------------------")
        no=1
        for i in path:
            print("Step",no,":")
            print(i)
            print("---------------------------------------")
            no+=1


import math
class Node():
    def __init__(self,value,key=math.inf,parent=None):
        self.value=value
        self.key=key
        self.parent=parent
    
class DepthFirstSearch():
    def __init__(self,startState,goalState,createChildren,heuristic):
        self.startState=Node(startState)
        self.goalState=Node(goalState)
        self.createChildren=createChildren
        self.heuristic=heuristic
        self.closed=[]
        self.stack=[]
        self.pathFound=False

    def search(self):
        self.stack.append(self.startState)
        while len(self.stack)>0:
            current=self.stack.pop()
            self.closed.append(current)
            if self.heuristic(current.value,self.goalState.value)==0:   
                self.pathFound=True             
                return
            childrenval=self.createChildren(current.value)
            for i in childrenval:
                if self.isClosed(i)!=True:
                    self.stack.append(Node(i,self.heuristic(i,self.goalState.value),current))
    
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
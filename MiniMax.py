import math
class Node():
    def __init__(self,value,profit=math.inf,level=0,parent=None):
        self.value=value
        self.profit=profit
        self.parent=parent
        self.children=[]
        self.level=level
    
class MiniMax():
    def __init__(self,root,createChildren,profit):
        self.root=Node(root)
        self.createChildren=createChildren
        self.profit=profit
        self.queue=[]
        self.maxCurrentMove=None
 
    def dequeue(self):
        self.queue.reverse()
        element=self.queue.pop()
        self.queue.reverse()
        return element
    
    def buildTree(self):
        self.queue.append(self.root)
        for i in self.queue:
            childrenval=self.createChildren(i.value)
            if childrenval!= None:
                for j in childrenval:
                    newnode=Node(j,level=i.level+1,parent=i)
                    self.queue.append(newnode)
                    i.children.append(newnode)
    
    def estimateProfit(self):
        for i in range(len(self.queue)-1,-1,-1):
            if self.queue[i].children==[]:
                self.queue[i].profit=self.profit(self.queue[i].value)
            else:
                if self.queue[i].level%2==0:
                    self.queue[i].profit=max([x.profit for x in self.queue[i].children])
                else:
                    self.queue[i].profit=min([x.profit for x in self.queue[i].children])

    def play(self,state):
        if self.maxCurrentMove==None:
             self.maxCurrentMove=self.root
        else:
            for i in self.maxCurrentMove.children:
                if i.value==state:
                    self.maxCurrentMove=i
        mx=-1234556
        for i in self.maxCurrentMove.children:
            if i.profit>mx:
                self.maxCurrentMove=i
                mx=i.profit
        return self.maxCurrentMove.value

    def show(self):
        for i in self.queue:
            print(i.value)

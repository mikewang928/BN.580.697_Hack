'''
created by Erx
no package at all :)
using EK+SPFA to find the minimum cost maximum flow
input: follow the hint and input your number / array of numbers (separated by space)
output: a chart about the assignment arrangements
'''

class Graph:
    def __init__(self,points):
        self.costTab={}        #table of costs
        self.capTab={}         #table of capacities
        self.resCap={}         #residual/left capacities
        self.backPath={}       #backward arcs
        self.len=len(points)
        self.INF=1e9
        for i in points:
            self.costTab.update({i:{}})
            self.capTab.update({i:{}})
            self.resCap.update({i:{}})

    def addEdge(self,s,t,cap,cost):
        self.costTab[s].update({t:cost})
        self.capTab[s].update({t:cap})
        self.resCap[s].update({t:cap})

    def costFlow(self,s,t):
        path=self.SPFA(s,t)
        while path:
            #print(" \n\nthe shortest path:",path)
            minFlow=self.findMinFlow(path,s,t)
            #print("the bottleneck: ",minFlow)
            self.changeFlow(minFlow,path,s,t)
            path=self.SPFA(s,t)
        return self.backPath

    def SPFA(self,s,t):
        que=[]          #spfa's que
        path=[0]*self.len          #record the shortest path
        dist=[self.INF]*self.len              #spfa's dist
        visited=[False]*self.len         #whether the point is in spfa's que

        dist[s]=0
        que.append(s);visited[s]=True        #the source in que

        while que:
            nowPoint=que[0]
            que.pop(0)
            visited[nowPoint]=False  #take out the first element in que
            for linkPoint,leftCapacity in self.resCap[nowPoint].items():  #its connected points  /  edges
                if (leftCapacity!=0)&(dist[linkPoint]>dist[nowPoint]+self.costTab[nowPoint][linkPoint]):
                    dist[linkPoint]=dist[nowPoint]+self.costTab[nowPoint][linkPoint]  #refresh the shorted path
                    path[linkPoint]=nowPoint
                    if not visited[linkPoint]:   #add in que
                        que.append(linkPoint)
                        visited[linkPoint]=True
        if dist[t]!=self.INF:
            return path
        else:
            return False

    def findMinFlow(self,path,s,t):
        pathNow=t
        mm=self.INF
        while pathNow!=s:
            pathPre=path[pathNow]
            if self.resCap[pathPre][pathNow]<mm:
                mm=self.resCap[pathPre][pathNow]
            pathNow=pathPre
        if mm!=self.INF:
            return mm
        else:
            return -1

    def changeFlow(self,minFlow,path,s,t):
        pathNow = t
        #print("backwards change flow path:",pathNow,end="")
        while pathNow != s:
            pathPre = path[pathNow]
            #print("->",pathPre,end="")
            self.resCap[pathPre][pathNow]-=minFlow
            if pathNow not in self.backPath:
                self.backPath[pathNow] = {}
            if pathPre not in self.backPath[pathNow]:
                self.backPath[pathNow][pathPre] = 0
            self.backPath[pathNow][pathPre]+=minFlow
            pathNow = pathPre

def input_patient_preference_list(N):
    rank=[[]]*N
    #rank: list of lists, every list's order represent a patient's prefered doctor's number, listed from most like to least like.
    # e.g. "4 2 3 1" represent the patient likes doctor 4 more than doctor 2, and so on.
    for i in range(N):
        input_string=input("Rank Order of Patient No.%d:" %(i+1)) #input seperated by space " "
        rank[i]=input_string.split()
        rank[i]=[int(ele) for ele in rank[i]]
    return rank

if __name__ == '__main__':
    N=int(input("Number of Patients:"))
    K=int(input("Number of Doctors:"))
    C=[]                                            #same/different capacity for each doctor
    input_string=input("Capacity of Each Doctor:")  #input seperated by space " "
    C=input_string.split()
    C=[int(ele) for ele in C]  #turn into integers
    rank=input_patient_preference_list(N) #patients' preferences
    points=[]                       #dots in the graph
    for i in range(N+K+2):
        points.append(i)
    G=Graph(points)

    for i in range(N):
        G.addEdge(0,i+1,1,0)                     #from source to patient: capacity 1, cost 0
    for i in range(N):
        for j in range(K):
            G.addEdge(i+1,j+N+1,1,rank[i][j])    #from patient to doctor: capacity 1, cost (preferences)
    for i in range(K):
        G.addEdge(i+N+1,N+K+1,C[i],0)            #from doctor to terminal: capacity (doc_cap), cost 0

    s=0;t=N+K+1
    outputTab=G.costFlow(s,t)

    title="\nAssignments:\n    Doctor"+" "*8+"Patient(s)    "
    print(title)
    print("-"*(len(title)-len("\nAssignments:\n)")),end="")
    for p,linkage in outputTab.items():
        if (p>N)&(p<N+K+1):
            print("\n     No.%d         "%(p-N),end="")
            #print("\nDoctor No.%d"%(p-N),"will take in Patient ",end="")
            for patient,choice in linkage.items():
                print(" No.%d "%(patient),end="")
                #print("No. %d  "%(patient),end="")



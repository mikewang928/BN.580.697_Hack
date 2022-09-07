'''
created by Ziyang Xu
using EK+SPFA to find the minimum cost maximum flow, which is from Rongxi Yi's coding
input: follow the hint and input your number in Ui
output: a chart about the assignment arrangements in Ui and a graph about the assignment arrangements
'''


'''
assuming that:
1. the number of doctors is random
2. the number of patients is random
3. the number of doctors is not always equal to the number of patients
4. every doctor have a capacity, whcih means that the doctor can only treat a certain number of patients; the capacity is different for different doctors
5. every patient have a rank of the doctors, which means preferenece to the doctor with a higher rank
6. input of the patients perference is in the format of (patients*doctors) matrix
7. the output is the assignment arrangements of the doctors and patients in format of dictionary and a graph
'''


from errno import WSAEHOSTUNREACH
import sys
from tkinter.tix import ButtonBox
from turtle import width
import Ui_Assignment_display
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QGraphicsScene, QFileDialog,QMessageBox
from PyQt5.QtGui import QMouseEvent,QFont, QStandardItemModel, QStandardItem, QPixmap
from PyQt5.QtCore import Qt, QPoint
from PyQt5 import QtCore, QtWidgets,QtGui
import matplotlib.pyplot as plt
import networkx as nx

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


######################################################################################################
#                                       Algorithm design                                             #
###################################################################################################### 
'''
This is a class whcih is used to find the minimum cost maximum flow by using EK+SPFA

input: the capacity table and the cost table
output: the minimum cost maximum flow path

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

######################################################################################################
#                                       UI design                                             #
###################################################################################################### 
'''
This is a class used to design the UI of the program and the interaction between the user and the program.
User could input the number of doctors and patients and the preference of the patients in the UI, then get the assignment arrangements of the doctors and patients in the UI and a graph about the assignment arrangements.


input: 
    1. the number of patients as an integer
    2. the number of doctors as an integer
    3. the preference of the patients in the format of patients ranking list

output:
    1. the hint during the input
    2. the assignment arrangements of the doctors and patients in the UI
    3. a dot graph about the assignment arrangements

'''

color_list = ['#262b4b'] #define a color list for storing the color of the nodes in the graph


class MyFigure(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        super(MyFigure, self).__init__(self.fig)

    def plotSin(self, x, y):
        self.axes0 = self.fig.add_subplot(111)
        self.axes0.plot(x, y)


class MainWindow(QMainWindow, Ui_Assignment_display.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

        self.setWindowTitle('Assignment Display')
        self.pushButton_7.clicked.connect(self.slot_max_or_recv) #connect pushButton_7 to slot_max_or_recv (resize the window)
        self.pushButton_8.clicked.connect(self.restart) #connect pushButton_8 to restart (reboot the program)
        self.pushButton_5.clicked.connect(self.showMinimized) #connect pushButton_5 to showMinimized (minimize the window)
        self.pushButton_6.clicked.connect(self.close) #connect pushButton_6 to close (close the window)

        self.textBrowser.setText('Please input your parameters.') #set the textBrowser's default text

        self.spinBox.valueChanged.connect(self.input_parameter) #connect spinBox to input_parameter (input the number of patients)
        self.spinBox_2.valueChanged.connect(self.input_parameter) #connect spinBox_2 to input_parameter (input the number of doctor)

        self.pushButton.clicked.connect(self.input_patient_preference_list) #connect pushButton to input_patient_preference_list (input the patient's preference list)
        self.pushButton.clicked.connect(self.input_doctor_capital) #connect pushButton to input_doctor_capital (input the doctor's capital)
        self.pushButton.clicked.connect(self.run_program) #connect pushButton to run_program (run the program)
        self.pushButton_2.clicked.connect(self.drow_dot_graph) #connect pushButton_2 to drow_dot_graph (draw the dot graph)
        self.pushButton_2.clicked.connect(self.drow_tree_View) #connect pushButton_2 to drow_tree_View (draw the tree view)

        self.pushButton_3.clicked.connect(self.output_to_local) #connect pushButton_3 to output_list (output the assignment arrangements to pgn file)

        self.checkBox_6.clicked.connect(self.set_dot_default_color) #connect checkBox_6 to set_dot_color (set the dot color)
        self.checkBox_7.clicked.connect(self.set_dot_red_color) #connect checkBox_7 to set_dot_color (set the dot color)
        self.checkBox_9.clicked.connect(self.set_dot_skyblue_color) #connect checkBox_8 to set_dot_color (set the dot color)
        self.checkBox_10.clicked.connect(self.set_output_is_list) #connect checkBox_10 to set_output_option (set the output option)
        self.checkBox_11.clicked.connect(self.set_output_is_graph) #connect checkBox_11 to set_output_option (set the output option)

    def input_parameter(self):
        
        #define the input_parameter function: get the number of patients and doctors, show the widget of inputting the preference list and capital
        
        N=self.spinBox.value() #get the number of patients
        K=self.spinBox_2.value() #get the number of doctors

        self.tableWidget.setRowCount(N) #set the row of tableWidget
        self.tableWidget.setColumnCount(K) #set the column of tableWidget
        self.tableWidget.setVerticalHeaderLabels('Patient %d' %(i+1) for i in range(N)) #set the vertical header of tableWidget
        self.tableWidget.horizontalHeader().setVisible(False)#set HorizontalHeader unvisible
        
        #show the patient information in textBrowser
        self.textBrowser.clear() #clear textBrowser
        self.textBrowser.append('The Patient list is:')
        for i in range(N):
            self.textBrowser.append('Patient %d' %(i+1))
        
        #set header width mode to stretch to fill the available space
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #set header's font
        font = QFont()
        font.setPointSize(15)
        self.tableWidget.verticalHeader().setFont(font)
        

        #set the tableWidget_2, as the input of doctor's capital
        self.tableWidget_2.setRowCount(1)
        self.tableWidget_2.setColumnCount(K)
        self.tableWidget_2.setHorizontalHeaderLabels('Doctor %d' %(i+1) for i in range(K))
        self.tableWidget_2.verticalHeader().setVisible(False)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setFont(font)

        return N,K

    def input_patient_preference_list(self):
    
        #get the row and column of tableWidget
        rows = self.tableWidget.rowCount()
        clos = self.tableWidget.columnCount()

        self.textBrowser.append(f'There are {rows} rows and {clos} columns in the tableWidget.') #show the row and column of tableWidget in textBrowser

        rank=[[]]*rows
        #rank: list of lists, every list's order represent a patient's prefered doctor's number, listed from most like to least like.
        # e.g. "4 2 3 1" represent the patient likes doctor 4 more than doctor 2, and so on.
        
        rank=[[self.tableWidget.item(i,j).text() for j in range(clos)] for i in range(rows)]  #get the input data from tableWidget, and store in rank, i stands for the row, j stands for the column
        rank=[[int(ele) for ele in rank[i]] for i in range(rows)]  #turn into integers
        self.textBrowser.append(f'The preference is {rank}')  #show the preference in textBrowser

        #print (rank[0])
        #print (rank[1])
        #print (rank[2])
        #print(rank[2][1])
        #print(rank[1][2])
        #print(rank[0][0])

        return rank
        
    def input_doctor_capital(self):
        #define the input_doctor_capital function: get the doctor's capital, and show the doctor information in textBrowser

        cap_clos = self.tableWidget_2.columnCount() #get the column of tableWidget_2
        C =[] #C: list of doctors' capital
        C = [self.tableWidget_2.item(0,j).text() for j in range(cap_clos)] #get the input data from tableWidget_2, and store in C
        self.textBrowser.append(f'The capacity is {C}') #show the capacity in textBrowser
        
        return C
      
    def run_program(self):
        #define the run_program function: run the algorithm, and show the assignment in textBrowser

        N=int(self.spinBox.value()) #get the number of patients and turn into integer
        K=int(self.spinBox_2.value()) #get the number of doctors and turn into integer
        
        rank=self.input_patient_preference_list() #get patients' preferences list from input_patient_preference_list function
        print(rank)
        
        C=self.input_doctor_capital() #get doctors' capital from input_doctor_capital function
        C=[int(ele) for ele in C]  #turn into integers
        print(C)

        #run the algorithm
        points=[]                      #dots in the graph
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

        #show the assignment in textBrowser
        title="\nAssignments:\n    Doctor"+" "*8+"Patient(s)    "
        self.textBrowser.append(title)
        print(title)
        print("-"*(len(title)-len("\nAssignments:\n)")),end="")

        self.textBrowser.append("-"*(len(title)-len("\nAssignments:\n)")))
        
        assignment_list= {} #assignment_list: dictionary, key is doctor, value is patient(s)
        
        #set doctor's name as key
        for key in range(K):
            assignment_list['Doctor %d' %(key+1)] = []
        #set patient's name as value
        for p,linkage in outputTab.items():
            if (p>N)&(p<N+K+1):
                print("\n     No.%d         "%(p-N),end="")
                #self.textBrowser.append("\nNo.%d"%(p-N))
                #print("\nDoctor No.%d"%(p-N),"will take in Patient ",end="")
                for patient,choice in linkage.items():
                    print(" No.%d "%(patient),end="")
                    #self.textBrowser.append("No.%d"%(patient))
                    #print("No. %d  "%(patient),end="")
                    assignment_list['Doctor %d' %(p-N)].append("Patient %d"%(patient))
        
        print(f'\nThe assignment of patients is {assignment_list}')
        
        #show the assignment of patients in textBrowser
        for key,Value in assignment_list.items():
            for i in range(len(Value)):
                self.textBrowser.append(f'    {key}        {Value[i]}')
        self.textBrowser.append(f'\nThe assignment of patients is {assignment_list}')
        
        return assignment_list
                    
    def drow_dot_graph(self):
        #define the drow_dot_graph function: drow the dot graph, and show the dot graph in textBrowser

        assignment_list= self.run_program() #get the assignment of patients from run_program function, assignment_list: dictionary, key is doctor, value is patient(s)
        print('--------------------------')
        print(assignment_list) 
        print('--------------------------')
        Assignment = {'Assignment List':[assignment_list]} #Assignment: dictionary, key is hospital, value is assignment_list as a dictionary
        print(Assignment)
    
        # Create a graph
        G = nx.Graph()
        # Add nodes
        G.add_nodes_from(assignment_list.keys())
        #add start node as Assignment List
        G.add_node('Assignment List')
        # Add edges
        for key,Value in assignment_list.items():
            for i in range(len(Value)):
                G.add_edge('Assignment List',key)
                G.add_edge(key,Value[i])
        
        #create a figure and add a subplot
        F_graph = MyFigure(width=5, height=3, dpi=100) 
        F_graph.axes = F_graph.fig.add_subplot(111) #add a subplot to figure
        F_graph.axes.set_title('Assignment Graph') #set the title of the graph

        width,height =self.graphicsView.size().width(),self.graphicsView.size().height() #get the size of graphicsView
        F_graph.resize(width,height) #resize the figure to the size of graphicsView

        #draw the graph
        nx.draw(G, with_labels=True, node_size=1000, font_size=8, pos=nx.spring_layout(G), node_color=color_list[-1], edge_color='black', width=2, alpha=0.5, arrows=True, ax=F_graph.axes) 

        F_graph.axes.set_axis_off() #set the axis off
        F_graph.axes.set_xticks([])  #set the xticks off
        F_graph.axes.set_yticks([]) #set the yticks off
        F_graph.axes.set_xticklabels([]) #set the xticklabels off
        F_graph.axes.set_yticklabels([]) #set the yticklabels off
        F_graph.axes.set_aspect('auto') #set the aspect of the graph to auto
        F_graph.axes.set_facecolor('white') #set the background color of the graph to white
        
        self.dot_graph_scene = QGraphicsScene() #create a scene
        self.dot_graph_scene.setSceneRect(0, 0, width, height) #set the size of the scene to the size of graphicsView
        self.dot_graph_scene.addWidget(F_graph) #add the figure to the scene
        self.graphicsView.setScene(self.dot_graph_scene) #set the scene to graphicsView  

    def drow_tree_View(self):
        #define the drow_tree_View function: drow the tree graph, and show in treeView

        assignment_list= self.run_program()
        
        #show Assignmentin treeView
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Assignment List'])
        itemProject = QStandardItem('Assignment List')
        self.model.appendRow(itemProject)
        for key, value in assignment_list.items():
            itemProject.appendRow([QStandardItem(key)])
            for i in range(len(value)):
                itemChild = QStandardItem(value[i])
                itemProject.child(itemProject.rowCount() - 1).appendRow(itemChild)

        self.treeView.setModel(self.model)
        self.treeView.expandAll() #expand all the items in treeView

    def output_to_local(self):
        if self.checkBox_10.isChecked():
            save_path = QFileDialog.getSaveFileName(self, 'Save assignment list','Assignment List','*.png')
            self.treeView.grab().save(save_path[0])
        elif self.checkBox_11.isChecked():
            save_path = QFileDialog.getSaveFileName(self, 'Save assignment graph','Assignment Graph','*.png')
            self.graphicsView.grab().save(save_path[0])
        else:
            box = QMessageBox()
            box.setWindowTitle('Warning')
            box.setText('Please select the output list or graph')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec_()
    

    def set_dot_default_color(self):
        #define the set_dot_default_color function: set the default color of the dot graph
        
        self.checkBox_6.setChecked(True) #set the checkbox_6 checked
        self.checkBox_7.setChecked(False) #set the checkbox_7 unchecked
        self.checkBox_9.setChecked(False) #set the checkbox_9 unchecked
 
        color = '#262b4b' #set the default color to #262b4b 
        color_list.append(color) #add the color to color_list

        if self.treeView.model() != None: #if the treeView is not empty
            self.drow_dot_graph()
        else:
            box = QMessageBox()
            box.setWindowTitle('Warning')
            box.setText('Please input parameters and run the program first')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec_()
    def set_dot_skyblue_color(self):
        #define the set_dot_blue_color function: set the blue color of the dot graph
        
        self.checkBox_6.setChecked(False) #set the checkbox_6 unchecked
        self.checkBox_9.setChecked(True) #set the checkbox_7 checked
        self.checkBox_7.setChecked(False) #set the checkbox_9 unchecked

        color = 'skyblue' #set the default color to skyblue
        color_list.append(color) #add the color to color_list

        if self.treeView.model() != None: #if the treeView is not empty
            self.drow_dot_graph()
        else:
            box = QMessageBox()
            box.setWindowTitle('Warning')
            box.setText('Please input parameters and run the program first')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec_()
    def set_dot_red_color(self):
        #define the set_dot_red_color function: set the red color of the dot graph
        
        self.checkBox_6.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_7.setChecked(True)

        color = 'red'
        color_list.append(color)

        if self.treeView.model() != None: #if the treeView is not empty
            self.drow_dot_graph()
        else:
            box = QMessageBox()
            box.setWindowTitle('Warning')
            box.setText('Please input parameters and run the program first')
            box.setIcon(QMessageBox.Warning)
            box.setStandardButtons(QMessageBox.Ok)
            box.exec_()

    def set_output_is_list(self):
        #define the set_output_is_list function: set the output is list
        
        if self.checkBox_10.isChecked():
            self.checkBox_11.setChecked(False)
    
    def set_output_is_graph(self):
        #define the set_output_is_graph function: set the output is graph
        
        if self.checkBox_11.isChecked():
            self.checkBox_10.setChecked(False)

    def default_parameter(self):
        #define the default_parameter function: set the default parameter
        self.spinBox.setValue(0)
        self.spinBox_2.setValue(0)
        self.checkBox_6.setChecked(True)
        self.checkBox_7.setChecked(False)
        self.checkBox_9.setChecked(False)
        self.checkBox_10.setChecked(True)
        self.checkBox_11.setChecked(False)
    def restart(self):
        #define the restart function: reboot the program and set the default parameter
        self.textBrowser.append("The program is rebooting, pls wait...")
        self.default_parameter()
        self.textBrowser.setText("The program has restarted, pls input your parameters.")
    def slot_max_or_recv(self):
        #define the slot_max_or_recv function: set the window size biggest or normal
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()   
    def mouseMoveEvent(self, e: QMouseEvent):
        #define the mouseMoveEvent function: set the movement of the window  
        if self._tracking:
            self._endPos = e.pos() - self._startPos
            self.move(self.pos() + self._endPos)  
    def mousePressEvent(self, e: QMouseEvent):
        #define the mousePressEvent function: set the press of the window
        if e.button() == Qt.LeftButton:
            self._startPos = QPoint(e.x(), e.y())
            self._tracking = True
    def mouseReleaseEvent(self, e: QMouseEvent):
        #define the mouseReleaseEvent function: set the release of the window
        if e.button() == Qt.LeftButton:
            self._tracking = False
            self._startPos = None
            self._endPos = None


# main loop
if __name__ == '__main__':
    
    app = QApplication(sys.argv)  #create a QApplication instance
    myWin = MainWindow() #create the MainWindow object
    myWin.setWindowTitle('Assignment Display') #set the title of the window
    myWin.show() 
    
    sys.exit(app.exec_()) #enter the mainloop of the application



######################################################################################################
#                                        example run                                        #
###################################################################################################### 
'''
The input in the UI:
    Number of patients: 5
    Number of doctors: 3

    Patient 1's preferences: 1 2 3
    Patient 2's preferences: 2 1 3
    Patient 3's preferences: 3 2 1
    Patient 4's preferences: 1 2 3
    Patient 5's preferences: 2 1 3

    Doctor 1's capacity: 2
    Doctor 2's capacity: 3
    Doctor 3's capacity: 2

Assignments:
    Doctor         Patient(s)
    -------------------------------
    Doctor 1         Patient 1  Patient 4
    Doctor 2         Patient 2  Patient 5
    Doctor 3         Patient 3  

    The assignment of patients is {'Doctor 1': ['Patient 1', 'Patient 4'], 'Doctor 2': ['Patient 2', 'Patient 5'], 'Doctor 3': ['Patient 3']}

The output in the UI:
    see the pictures in the attachment

'''
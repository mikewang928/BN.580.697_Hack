'''
created by Ziyang Xu
using EK+SPFA to find the minimum cost maximum flow, which is from Rongxi Yi's code
input: follow the hint and input your number in Ui
output: a chart about the assignment arrangements in Ui and a graph about the assignment arrangements
'''

import sys
import Ui_Assignment_display
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QGraphicsScene, QFileDialog,QMessageBox
from PyQt5.QtGui import QMouseEvent,QFont, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QPoint

import sys
import Ui_Assignment_display
from PyQt5.QtWidgets import QApplication, QMainWindow,QHeaderView
from PyQt5.QtGui import QMouseEvent,QFont
from PyQt5.QtCore import Qt, QPoint
import matplotlib.pyplot as plt
import networkx as nx
from NRMP_method import run
import math

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure


######################################################################################################
#                                       UI design                                                    #
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

        self.pushButton.clicked.connect(self.input_doctor_preference_list) #connect pushButton to input_patient_preference_list (input the patient's preference list)
        self.pushButton.clicked.connect(self.input_Hospital_preference_list) #connect pushButton to input_doctor_capital (input the doctor's capital)
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
        
        N=self.spinBox.value() #get the number of patients (get the number of doctors)
        K=self.spinBox_2.value() #get the number of doctors (get the number of hospitals)

        self.tableWidget.setRowCount(N) #set the row of tableWidget
        self.tableWidget.setColumnCount(K) #set the column of tableWidget
        self.tableWidget.setVerticalHeaderLabels('Doctor %d' %(i+1) for i in range(N)) #set the vertical header of tableWidget
        self.tableWidget.horizontalHeader().setVisible(False)#set HorizontalHeader unvisible
        
        #show the patient information in textBrowser
        self.textBrowser.clear() #clear textBrowser
        self.textBrowser.append('The Doctor list is:')
        for i in range(N):
            self.textBrowser.append('Doctor %d' %(i+1))
        
        #set header width mode to stretch to fill the available space
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #set header's font
        font = QFont()
        font.setPointSize(15)
        self.tableWidget.verticalHeader().setFont(font)
        
        
        #set the tableWidget_Hosp, as the input of the doctors preference
        self.tableWidget_2.setRowCount(K)
        self.tableWidget_2.setColumnCount(N)
        self.tableWidget_2.setVerticalHeaderLabels('Hospital %d' %(i+1) for i in range(K)) #set the vertical header of tableWidget
        self.tableWidget_2.horizontalHeader().setVisible(False)#set HorizontalHeader unvisible
        #show the patient information in textBrowser
        self.textBrowser.clear() #clear textBrowser
        self.textBrowser.append('The Hospital list is:')
        for i in range(N):
            self.textBrowser.append('Hospital %d' %(i+1))
        
        #set header width mode to stretch to fill the available space
        self.tableWidget_2.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget_2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #set header's font
        font = QFont()
        font.setPointSize(15)
        self.tableWidget_2.verticalHeader().setFont(font)


        return N,K


    
    def input_doctor_preference_list(self):
    
        #get the row and column of tableWidget
        rows = self.tableWidget.rowCount()
        clos = self.tableWidget.columnCount()

        self.textBrowser.append(f'There are {rows} rows and {clos} columns in the tableWidget.') #show the row and column of tableWidget in textBrowser

        rank=[[]]*rows
        #rank: list of lists, every list's order represent a doctor's prefered hospital's number, listed from most like to least like.
        # e.g. "4 2 3 1" represent the doctor likes hospital 4 more than hospital 2, and so on.
        
        rank=[[self.tableWidget.item(i,j).text() for j in range(clos)] for i in range(rows)]  #get the input data from tableWidget, and store in rank
        rank=[[int(ele) for ele in rank[i]] for i in range(rows)]  #turn into integers
        self.textBrowser.append(f'The preference is {rank}')  #show the preference in textBrowser

        return rank
        
    
    
    def input_Hospital_preference_list(self):
        #get the row and column of tableWidget
        rows = self.tableWidget_2.rowCount() # number hospitals 
        clos = self.tableWidget_2.columnCount() # number of rows

        self.textBrowser.append(f'There are {rows} rows and {clos} columns in the tableWidget_2.') #show the row and column of tableWidget in textBrowser

        rank=[[]]*rows
        #rank: list of lists, every list's order represent a patient's prefered doctor's number, listed from most like to least like.
        # e.g. "4 2 3 1" represent the patient likes doctor 4 more than doctor 2, and so on.
        
        rank=[[self.tableWidget_2.item(i,j).text() for j in range(clos)] for i in range(rows)]  #get the input data from tableWidget, and store in rank
        rank=[[int(ele) for ele in rank[i]] for i in range(rows)]  #turn into integers
        self.textBrowser.append(f'The preference is {rank}')  #show the preference in textBrowser
        Doctor_is_occupied_list = [False]*clos
        Hospital_target_list = [[] for _ in range(rows)] 
        Hospital_cap = math.ceil(clos/rows)

        return rank, Doctor_is_occupied_list, Hospital_target_list,Hospital_cap
    
        
    def run_program(self):
        #define the run_program function: run the algorithm, and show the assignment in textBrowser

        N=int(self.spinBox.value()) #get the number of doctors and turn into integer
        K=int(self.spinBox_2.value()) #get the number of Hospitals and turn into integer
        
        rank=self.input_doctor_preference_list() #get doctors' preferences list from input_doctor_preference_list function
        rank_H,Doctor_is_occupied_list,Hospital_target_list, Hospital_cap,= self.input_Hospital_preference_list()
        Hospital_confirmed_list = run(Doctor_is_occupied_list, N, Hospital_cap, rank, Hospital_target_list, rank_H)
        print(Hospital_confirmed_list)
        assignment_list = {} #assignment_list: dictionary, key is Hospital, value is doctor(s)
        print(K)
        for key in range(K):
            assignment_list['Hospital %d' %(key+1)] = []
            for i in range(len(Hospital_confirmed_list[key])):
                # set Doctor's ID as values
                assignment_list['Hospital %d' %(key+1)].append('Doctor id %d'%Hospital_confirmed_list[key][i])
        print(assignment_list)

        #show the assignment in textBrowser
        title="\nAssignments:\n    Hospital"+" "*8+"doctor(s)    "
        self.textBrowser.append(title)
        print(title)
        print("-"*(len(title)-len("\nAssignments:\n)")),end="")

        self.textBrowser.append("-"*(len(title)-len("\nAssignments:\n)")))
        
        #show the assignment of Doctors in textBrowser
        for key,Value in assignment_list.items():
            for i in range(len(Value)):
                self.textBrowser.append(f'    {key}        {Value[i]}')
        self.textBrowser.append(f'\nThe assignment of doctors is {assignment_list}')
        
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




if __name__ == '__main__':
    
    app = QApplication(sys.argv)  #create a QApplication instance
    myWin = MainWindow() #create the MainWindow object
    myWin.setWindowTitle('Assignment Display') #set the title of the window
    myWin.show() 
    
    sys.exit(app.exec_()) #enter the mainloop of the application
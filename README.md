# BN.580.697_Hack
Within this Github repo, we (Siyu Wang, Rongxi Yi, ZiYang Xu) implemented the Hospital-Doctors matching problems both in the hospital don't have a perference case (standard question) and the hopitals have prefernce cases (the challenge question). Each cases is solved by using MCMF and NRMP algorthims respectively. <br><br>
To make a better user experience, an UI interface is implemented (Operation is manuel is explained in `Section I`). A detailed algorthim explaination is further summarized in the `min_cost_flow.ipynb` file and in Section II of the `readme.md` file. 




## SECTION I: UI interface user manuel
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/UI_input_output_Example/UI.png) <br><br>

## NOTICE that the UI interface is a shared structure between MCMF and NRMP algorithm. If performing MCMF task, please open `main_Assignment of doctors.py` and run. If performing NRMP task please open `Main_NRMP.py` file and run. 
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/Picture2.png) <br><br>

## Input example for MCMF task (requires to run the `main_Assignment of doctors.py` file)
* Number of Doctors in spinbox: an integer <br>
* Number of Hospitals in spinbox: an integer <br>
* Each doctor's perference in the chart: every row is a ranking of hospitals according doctor's perference, put an integer (smaller than the number of hospital) in each blank <br>
* Hospital capacity: put an integer in the blank under each hospital <br>

### Example
    Number of doctors: 5 
    Number of hospitals: 3 

    doctor 1's preferences: 1 2 3 
    doctor 2's preferences: 2 1 3 
    doctor 3's preferences: 3 2 1 
    doctor 4's preferences: 1 2 3 
    doctor 5's preferences: 2 1 3 

    hospital 1's capacity: 2 
    hospital 2's capacity: 3 
    hospital 3's capacity: 2 

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/UI_input_output_Example/Example_run_01.png) <br><br>

### Action
* run: click the `run` button, run the algorism and output the assignment in textBrower <br>
* drow: click the `drow` button, get the treelist and graph in output window <br>

### Output
* Tree List: a list which can fold or unfold a class of assignment <br>
* Dot Gragh: a gragh which includes nodes of hospitals/doctors, and edge indicating the assignment <br>

### Example

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/UI_input_output_Example/Example_run_02.png) <br><br>

### Output Action
* Change node color: Three colors to change, `default`, `skyblue` or `red` <br>
* Change output_to_local option: Two options to switch, `list` or `graph`<br>
* Output to local: click the `output to local` button and input the filename and filelocation in dialog<br>

### Example

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/UI_input_output_Example/Example_run_03.png) <br><br>


## Input example for MCMF task (requires to run the `main_NRMP.py` file)
* Number of Doctors in spinbox: an integer <br>
* Number of Hospitals in spinbox: an integer <br>
* Each doctor's perference in the chart: every row is a ranking of hospitals according doctor's perference, put an integer (smaller than the number of hospital) in each blank <br>
*  Each Hsopital's perference in the chart: every row is a ranking of doctors according Hsopital's perference, put an integer (smaller than the number of doctor) in each blank <br>

### Example
    Number of doctors: 5 
    Number of hospitals: 2 

    doctor 1's preferences: 1 2  
    doctor 2's preferences: 1 2 
    doctor 3's preferences: 1 2
    doctor 4's preferences: 1 2 
    doctor 5's preferences: 1 2 

    hospital 1's preferences: 1 2 3 4 5
    hospital 2's preferences: 5 4 3 2 1 
    

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/Picture_NRMP_Example.png) <br><br>

### Action
* run: click the `run` button, run the algorism and output the assignment in textBrower <br>
* drow: click the `drow` button, get the treelist and graph in output window <br>

### Output
* Tree List: a list which can fold or unfold a class of assignment <br>
* Dot Gragh: a gragh which includes nodes of hospitals/doctors, and edge indicating the assignment <br>

### Example

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/Picture_NRMP_example_result.png) <br><br>

### Output Action
* Change node color: Three colors to change, `default`, `skyblue` or `red` <br>
* Change output_to_local option: Two options to switch, `list` or `graph`<br>
* Output to local: click the `output to local` button and input the filename and filelocation in dialog<br>

### Example

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/Picture_NRMP_export_image.png) <br><br>


## Window action

* `Reboot`: reboot the program, put the mouse on the yellow button at top right corner of the window and you will see the hint<br>
* `Minimize`: minimize the window, put the mouse on the gray button at top right corner of the window and you will see the hint<br>
* `Maximize and Restore`: maximize the window and restore to a normal one when maximized, put the mouse on the green button at top right corner of the window and you will see the hint<br>
* `Close`: close the window and end the program, put the mouse on the red button at top right corner of the window and you will see the hint<br>

## Warning
A window of `warning` will pop up if there is not parameter in the running process. <br>
eg. you change a node color in output window but you haven't input any parameter or haven't run the algrorithm yet.<br>

### Example
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/UI_input_output_Example/warning.png) <br><br>


## SECTION II Algorthim explaination 



 
### Case I: Hosptials have no preference 
#### Supported matchings & Assumptions
We support the following assignment tasks that are common in the healthcare systems.<br>
 * Each Doctor `needs` to find a hosptial.
 * Each Doctor has a `ranked preference list` containing every hosptial.
 * hosptials don't have preferences over doctors.
 * The `maximum capacity` of each hospital varies. <br>The total capacity exceeds the number of doctors.<br><br>
  
#### Why does MCMF works in Case I [1] [2] [3]
As shown in the figure below, circles ○ representing doctors, and triangles △ representing hospitals.<br>
The problem can be modeled into a bipartite graph, which means that vertices are separated into two sets and vertices in the same set has no connections between each other. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/1.png) <br><br>
doctor No.1 has a level of preference towards hospital No.1, hospital No.2, and hospital No.3. This can be represented as three different edges pointing from doctor No.1 to each hospital, as shown in the figure below. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/2.png) <br><br>

Each doctor has a level of preference towards each hospital. Now the problem can be represented as the figure below. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/3.png) <br><br>

What we need to find out is that, what is the `most satisfying` arrangement when ensuring `every doctor can find a hospital`.<br>
* We can translate `most satisfying` into `least cost`, where the cost is the preference ranking. If a doctor rank a hospital as their favorite, the rank value is the smallest, which can be used as a cost. We set the cost of each edge as the preference ranking.<br>
* Also, we can translate `every doctor can find a hospital` into `maximize the matching number`, which can be translated into `maximize flow  under certain restrictions`. Since that each person is ONE doctor and can only take 1 capacity of a hospital, we set the flow capacity of each edge as 1.<br>
* For example, if doctor No.1 likes hospital No.1 the most, hospital No.2 the second, and hospital No.3 the least, the costs and flow capacities of doctor No.1's edges are as below. (Edge: flow_capacity (cost) )<br><br>

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/5.png) <br><br>

* Add a starting point `S` and connect it with every doctor point. We set the flow capacities of these edges as 1. This way, a doctor can maximumly choose one hospital. <br>
* Add a ending point `E` and connect it with every hospital point. We set the flow capacities of these edges as each hospital's capcities. This way, a hospital can maximumly take in their capacity amount of doctor.<br>
* Set the costs of all starting and ending edges as 0. This way, only doctor' preferences towards hospital can contribute to costs.<br><br>

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/6.png) <br><br>

The problem is now a `minimum cost maximum flow` problem.[3] The algorithm follows the below flowchart. It searches for the least-cost path in all the paths that still have left some flow capacities, and fills the path with maximum flow. The algorithms repeats itself until there is no more available path.<br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/fc.png) <br><br>


### Case II: Hosptials have preference 
We support the following assignment tasks that are common in the healthcare systems.<br>
 * Each doctor `needs` to find a hospital.
 * Each doctor has a `ranked preference list` containing every hospital.
 * Each hospital has a `ranked preference list` containing every doctor.<br><br>
  
#### Why does NRMP works in Case I [4]
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/Picture_NRMP_flowchart.png) <br><br>
As shown in the above flowchart. Each match is a combined result both from the doctors and the hospital's perference.[4] In such a way the final matching result represents the optimal solution. 



References:<br>
[1] Ahuja, Ravindra K.; Magnanti, Thomas L.; Orlin, James B. (1993). Network Flows. Theory, Algorithms, and Applications. Prentice Hall.<br>
[2] Moore, Edward F. (1959). "The shortest path through a maze". Proceedings of the International Symposium on the Theory of Switching. Harvard University Press. pp. 285–292.<br>
[3] Duan, Fanding (1994), "关于最短路径的SPFA快速算法 [About the SPFA algorithm]", Journal of Southwest Jiaotong University, 29 (2): 207–212 <br>
[4] P. A. Nagarkar and J. E. Janis, “Fixing the ‘match’: How to play the game,” Journal of Graduate Medical Education, vol. 4, no. 2, pp. 142–147, 2012. <br>

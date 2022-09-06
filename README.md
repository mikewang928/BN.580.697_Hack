# BN.580.697_Hack
# Supported matchings
We support the following assignment tasks that are common in the healthcare systems.<br>
* Patients --> Doctors 
  * Each patient `needs` to visit a doctor.
  * Each patient has a `ranked preference list` containing every doctor.
  * Doctors don't have preferences over patients.
  * The `maximum capacity` of each doctor varies. <br>The total capacity exceeds the number of patients.<br><br>

* Doctors --> Hospitals
  * Each doctor `needs` to find a hospital.
  * Each doctor has a `ranked preference list` containing every hospital.
  * Each hospital has a `ranked preference list` containing every doctor.
  * <br><br>

# How to use it
### Patients --> Doctors
Input:
* K: an integer, represents `the number of patients`.
* N: an integer, represents `the number of doctors`.
* C: a list of integers separated by spaces, represents `the capacity of each doctor`.
* Rank orders: K lines of list of integers separated by spaces, represents `each patient's ranked preferences` over doctors.

Input example:
>Number of Patients: 4
<br>Number of Doctors: 3
<br>Capacity of Each Doctor: 1 2 2
<br>Rank Order of Patient No.1: 1 2 3
<br>Rank Order of Patient No.2: 2 1 3
<br>Rank Order of Patient No.3: 1 2 3
<br>Rank Order of Patient No.4: 2 1 3

This means:
* There are 4 patients and 3 doctors.
* Doctor No.1 has a capacity of 1. Doctor No.2 has a capacity of 2. Doctor No.3 has a capacity of 2.
* Patient No.1 prefers Doctor No.1 most, then Doctor No.2, and Doctor No.3 least.
* Patient No.2 prefers Doctor No.2 most, then Doctor No.1, and Doctor No.3 least.
* And so on...

Output
* A simple chart containing 2 columns, `Doctor` and `Patient(s)`.
* Each row represents a patient-doctor arrangement.

Onput example:
>Assignments:
<br><pre>    Doctor        Patient(s)    
<br>-------------------------------
<br>     No.1          No.1 
<br>     No.2          No.2  No.4 
<br>     No.3          No.3 

This means the most satisfying assignment is: 
* Doctor No.1 takes in Patient No.1, 
* Doctor No.2 takes in Patient No.2 and No.4, 
* Doctor No.3 takes in Patient No.3.
### Doctors --> Hospitals
Input:
* Please refer to the .ipynb document.<br>

Output:
* Please refer to the .ipynb document.

# Why it works
### Patients --> Doctors
As shown in the figure below, circles ○ representing patients, and triangles △ representing doctors.<br>
The problem can be modeled into a bipartite graph, which means that vertices are separated into two sets and vertices in the same set has no connections between each other. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/1.png) <br><br>
Patient No.1 has a level of preference towards doctor No.1, doctor No.2, and doctor No.3. This can be represented as three different edges pointing from patient No.1 to each doctor, as shown in the figure below. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/2.png) <br><br>

Each patient has a level of preference towards each doctor. Now the problem can be represented as the figure below. <br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/3.png) <br><br>

What we need to find out is that, what is the `most satisfying` arrangement when ensuring `every patient can meet a doctor`.<br>
* We can translate `most satisfying` into `least cost`, where the cost is the preference ranking. If a patient rank a doctor as their favorite, the rank value is the smallest, which can be used as a cost. We set the cost of each edge as the preference ranking.<br>
* Also, we can translate `every patient can meet a doctor` into `maximize the matching number`, which can be translated into `maximize flow  under certain restrictions`. Since that each person is ONE person and can only take 1 capacity of a doctor's office, we set the flow capacity of each edge as 1.<br>
* For example, if patient No.1 likes doctor No.1 the most, doctor No.2 the second, and doctor No.3 the least, the costs and flow capacities of patient No.1's edges are as below. (Edge: flow_capacity (cost) )<br><br>

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/5.png) <br><br>

* Add a starting point `S` and connect it with every patient point. We set the flow capacities of these edges as 1. This way, a patient can maximumly choose one doctor. <br>
* Add a ending point `E` and connect it with every doctor point. We set the flow capacities of these edges as each doctor's capcities. This way, a doctor can maximumly take in their capacity amount of patients.<br>
* Set the costs of all starting and ending edges as 0. This way, only patients' preferences towards doctors can contribute to costs.<br><br>

![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/6.png) <br><br>

The problem is now a classic `minimum cost maximum flow` problem. The algorithm follows the below flowchart. It searches for the least-cost path in all the paths that still have left some flow capacities, and fills the path with maximum flow. The algorithms repeats itself until there is no more available path.<br><br>
![image](https://github.com/mikewang928/BN.580.697_Hack/blob/main/images/fc.png) <br><br>

### Doctors --> Hospitals
* Please refer to the .ipynb document.<br>

References:<br>
Ahuja, Ravindra K.; Magnanti, Thomas L.; Orlin, James B. (1993). Network Flows. Theory, Algorithms, and Applications. Prentice Hall.<br>
Moore, Edward F. (1959). "The shortest path through a maze". Proceedings of the International Symposium on the Theory of Switching. Harvard University Press. pp. 285–292.<br>
Duan, Fanding (1994), "关于最短路径的SPFA快速算法 [About the SPFA algorithm]", Journal of Southwest Jiaotong University, 29 (2): 207–212

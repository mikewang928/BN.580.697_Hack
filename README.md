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

Output


# Why it works
### Patients --> Doctors

### Doctors --> Hospitals


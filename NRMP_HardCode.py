# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 23:32:45 2022

@author: wsycx
"""
'''
assuming that:


input of the doctors perference is in the format of (doctors*hospitals) where the horizatal direction of the 
matrix is the doctors perference of hospitals


input of the hospital perference is in the format of (hospitals*doctors) where the horizatal direction of the 
matrix is the doctors perference of hospitals


the output is in the format of #hospitals lists of arrays containing the admission result 

'''
import math
import numpy as np

# define constants 

'''
Test 1
'''
num_doctor = 5
num_Hospital = 2
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[1,2],[2,1],[1,2],[2,1],[1,2]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 



'''
Test 2
'''
num_doctor = 5
num_Hospital = 2
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[1,2],[1,2],[1,2],[2,1],[1,2]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 



'''
Test 3
'''
num_doctor = 5
num_Hospital = 2
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[2,1],[2,1],[2,1],[2,1],[2,1]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 


'''
Test 4
'''
num_doctor = 5
num_Hospital = 3
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[2,1,3],[3,2,1],[2,1,3],[2,3,1],[2,1,3]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5],[1,5,4,3,2]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 


'''
Test 5
'''
num_doctor = 5
num_Hospital = 3
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5],[1,5,4,3,2]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 



'''
Test 6
'''
num_doctor = 5
num_Hospital = 3
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[1,2,3],[1,2,3],[1,2,3],[1,2,3],[1,2,3]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5],[1,5,4,3,2]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 


'''
Test 7
'''
num_doctor = 5
num_Hospital = 3
Hospital_cap = math.ceil(num_doctor/num_Hospital)
Doctor_Rank = [[2,1,3],[2,1,3],[2,1,3],[2,1,3],[2,1,3]]
Hospital_Rank = [[1,2,3,4,5],[4,2,1,3,5],[1,5,4,3,2]]
Doctor_is_occupied_list = [False]*num_doctor

Hospital_target_list = [[] for _ in range(num_Hospital)] 



# '''
# Test 5
# '''
# num_doctor = 10
# num_Hospital = 4
# Hospital_cap = math.ceil(num_doctor/num_Hospital)
# Doctor_Rank = [[1,2,3,4],[3,2,1,4],[4,1,3,2],[3,2,4,1],[3,1,4,2],[3,1,2,4],[4,3,2,1],[3,2,1,4],[2,1,3,4],[1,3,4,2]]
# Hospital_Rank = [[1,2,3,4,5,6,7,8,9,10],[2,1,4,3,5,10,9,6,8,7],[6,2,1,3,5,4,7,10,9,8],[5,4,3,2,1,10,9,8,7,6]]
# Doctor_is_occupied_list = [False]*num_doctor

# Hospital_target_list = [[] for _ in range(num_Hospital)] 
'''
input: 
    Doctor_Id: the doctor id of the new coming doctor 
    Hospital_Id: the new coming doctor's choise of hospital

output:
    status: 
        0: there is an replaced doctor 
        -1: there is no replaced doctor 
        -2: the exisitng doctors in the hospital target list all rank higher than the new coming doctor 
'''
# check if there's a higher ranked docter in the hospital target list 
# Doctor Id and Hospital Id must start from 1 
def higher_ranker_check(Doctor_Id, Hospital_Id):
    print('---------- in higher ranker check ---------')
    print('doctor id: ' + str(Doctor_Id))
    Doctor_Ranking_index_in_Hospital_list = Hospital_Rank[Hospital_Id - 1].index(Doctor_Id) # Doctor_Ranking_index_in_Hospital_list starts from 0
    # if the list is empty or have avalible space add the doctor in the target list 
    if len(Hospital_target_list[Hospital_Id -  1]) == 0 or len(Hospital_target_list[Hospital_Id -1 ]) < Hospital_cap:
        Hospital_target_list[Hospital_Id -1 ].append(Doctor_Id) 
        Doctor_is_occupied_list[Doctor_Id-1] = True # set the docters status as occupied
        status = -1
        print('status: ' + str(status))
        return -1 # -1 means there's no replaced doctor in record 
    else:
        # if the hospital list is full
        replaceble_doctor_list = []
        replaceble_doctor_Id = None
        # finding the replaceble doctor's ID 
        for doctor_ID_in_hospital_list in Hospital_target_list[Hospital_Id -1 ]:
            # if an exisiting doctor in the list ranks shorter than the new coming doctor, the existing doctor will be move to the replaceble list
            if Hospital_Rank[Hospital_Id -1 ].index(doctor_ID_in_hospital_list) > Hospital_Rank[Hospital_Id-1].index(Doctor_Id):
                replaceble_doctor_Id = doctor_ID_in_hospital_list
                # if the replacable_doctor_list is empty and the replaceble doctor's ID
                if len(replaceble_doctor_list) == 0:
                    replaceble_doctor_Id = doctor_ID_in_hospital_list
                    replaceble_doctor_list.append(replaceble_doctor_Id)
                    print(replaceble_doctor_list)
                    print('replaceble_doctor_Id: ' + str(replaceble_doctor_Id))
                else: 
                    # find the shortest ranking replaceble doctor
                    if Hospital_Rank[Hospital_Id -1 ].index(doctor_ID_in_hospital_list) > Hospital_Rank[Hospital_Id -1 ].index(replaceble_doctor_Id):
                        replaceble_doctor_Id = doctor_ID_in_hospital_list
                        replaceble_doctor_list[0] = replaceble_doctor_Id
                        print(replaceble_doctor_list)
                        print('replaceble_doctor_Id: ' + str(replaceble_doctor_Id))
        # if there is a replaceble doctor in the hospital's target list
        if replaceble_doctor_Id is not None:
            print("H-list before remove: ")
            print(Hospital_target_list)
            print('replaceble_doctor_Id: ' + str(replaceble_doctor_Id))
            Hospital_target_list[Hospital_Id -1 ].remove(replaceble_doctor_Id) # remove the replaced docter ID from the target list 
            print("H-list after remove: ")
            print(Hospital_target_list)
            Doctor_is_occupied_list[replaceble_doctor_Id-1] =False # set the replaced doctor status as available
            Hospital_target_list[Hospital_Id -1].append(Doctor_Id) # add the new doctor's ID in the list
            print("H-list after insertion: ")
            print(Hospital_target_list)
            Doctor_is_occupied_list[Doctor_Id-1] = True # set the docters status as occupied
            status = 0
            print('status: ' + str(status))
            return 0 # 0 indicates there are replaced doctor in the record
        else: 
            status = -2
            print('status: ' + str(status))
            return -2 # -2 indicates that the exisitng doctors in the hospital target list all rank higher than the new coming doctor


def input_Doctor_preference_list(N):
    rank=[[]]*N
    #rank: list of lists, every list's order represent a patient's prefered doctor's number.
    # e.g. "1 2 3 4" represent the patient likes doctor 1 more than doctor 2, and so on.
    for i in range(N):
        input_string=input("Rank Order of Doctor (seperated by space) No.%d:" %(i+1)) #input seperated by space " "
        rank[i]=input_string.split()
        rank[i]=[int(ele) for ele in rank[i]]
    return rank


def input_Hospital_preference_list(N):
    rank=[[]]*N
    #rank: list of lists, every list's order represent a patient's prefered doctor's number.
    # e.g. "1 2 3 4" represent the patient likes doctor 1 more than doctor 2, and so on.
    for i in range(N):
        input_string=input("Rank Order of Hospital (seperated by space) No.%d:" %(i+1)) #input seperated by space " "
        rank[i]=input_string.split()
        rank[i]=[int(ele) for ele in rank[i]]
    return rank




while all(Doctor_is_occupied_list) == False:
    for i in range(num_doctor):
        if Doctor_is_occupied_list[i] == False:
            Doctor_Id = i+1
            Doctor_Hospital_choice = Doctor_Rank[i][0]
            status = higher_ranker_check(Doctor_Id, Doctor_Hospital_choice)
            del Doctor_Rank[i][0] # remove it's perfernece once submitted
            # if the submission is rejected by the hosipital and the doctor still has a perfernece, try the next perference hoispital
            while status == -2 and len(Doctor_Rank[i]) !=0: 
                Doctor_Hospital_choice = Doctor_Rank[i][0]
                status = higher_ranker_check(Doctor_Id, Doctor_Hospital_choice)
                del Doctor_Rank[i][0] #remove it's perfernece once submitted
            if status == -2 and len(Doctor_Rank[i])==0:
                Doctor_is_occupied_list[i] = None
            print(Hospital_target_list)

# if __name__ == '__main__':
#     N_Doctor =int(input("Number of Doctors:"))
#     N_Hospital =int(input("Number of Hospitals:"))
#     Doctor_cap = math.ceil(N_Doctor/N_Hospital)  #same capacity for every doctor
#     Doctor_cap_list = list(np.ones(N_Doctor)*Doctor_cap)
#     Doctor_rank = input_Doctor_preference_list(N_Doctor) #patients' preferences
#     Hospital_rank = input_Hospital_preference_list(N_Hospital)
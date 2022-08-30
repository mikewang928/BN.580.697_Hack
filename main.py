from ortools.graph import pywrapgraph

def input_patient_preference_list(N):
    rank=[[]]*N
    #rank: list of lists, every list's order represent a patient's prefered doctor's number.
    # e.g. "1 2 3 4" represent the patient likes doctor 1 more than doctor 2, and so on.
    for i in range(N):
        input_string=input("Rank Order of Patient No.%d:" %(i+1)) #input seperated by space " "
        rank[i]=input_string.split()
        rank[i]=[int(ele) for ele in rank[i]]
    return rank

def building_net(N,K,C,rank):
    start_nodes=[]
    for i in range(N):
        start_nodes.append(0)
    for i in range(N):
        for j in range(K):
            start_nodes.append(i+1)
    for i in range(K):
        start_nodes.append(i+1+N)
    #print(start_nodes)
    end_nodes=[]
    for i in range(N):
        end_nodes.append(i+1)
    for i in range(N):
        for j in range(K):
            end_nodes.append(j+1+N)
    for i in range(K):
        end_nodes.append(N+K+1)
    #print(end_nodes)
    capacities=[]
    for i in range(N):
        capacities.append(1)
    for i in range(N):
        for j in range(K):
            capacities.append(1)
    for i in range(K):
        capacities.append(C[i])
    #print(capacities)
    unit_costs=[]
    for i in range(N):
        unit_costs.append(0)
    for i in range(N):
        for j in range(K):
            unit_costs.append(rank[i].index(j+1)+1)
    for i in range(K):
        unit_costs.append(0)
    #print(unit_costs)
    supplies=[N]
    for i in range(N):
        supplies.append(0)
    for i in range(K):
        supplies.append(0)
    supplies.append(-N)
    #print(supplies)
    return start_nodes,end_nodes,capacities,unit_costs,supplies

def hand_min_cost_max_flow(N,start_nodes,end_nodes,capacities,unit_costs,supplies):
    #Dijkstra+EK



def min_cost_maximum_flow(N,start_nodes,end_nodes,capacities,unit_costs,supplies):
    min_cost_flow = pywrapgraph.SimpleMinCostFlow()
    # Add each arc.
    for i in range(0, len(start_nodes)):
        min_cost_flow.AddArcWithCapacityAndUnitCost(start_nodes[i], end_nodes[i],
                                                    capacities[i], unit_costs[i])
    # Add node supplies.
    for i in range(0, len(supplies)):
        min_cost_flow.SetNodeSupply(i, supplies[i])
    # Find the minimum cost flow between node 0 and node 4.
    if min_cost_flow.Solve() == min_cost_flow.OPTIMAL:
        print('')
        print('Minimum cost:', min_cost_flow.OptimalCost())
        print('')
        ''' #the follows prints the whole network flow
        print('  Arc    Flow / Capacity  Cost')
        for i in range(min_cost_flow.NumArcs()):
            cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
            print('%1s -> %1s   %3s  / %3s       %3s' % (
                min_cost_flow.Tail(i),
                min_cost_flow.Head(i),
                min_cost_flow.Flow(i),
                min_cost_flow.Capacity(i),
                cost))
        '''
        #print the assignments
        print("Assignments as:")
        for i in range(min_cost_flow.NumArcs()):
            cost = min_cost_flow.Flow(i) * min_cost_flow.UnitCost(i)
            if cost != 0:
                print('Patient No. %1s -> Doctor No. %1s' % (min_cost_flow.Tail(i), min_cost_flow.Head(i) - N))
    else:
        print('There was an issue with the min cost flow input.')

if __name__ == '__main__':
    N=int(input("Number of Patients:"))
    K=int(input("Number of Doctors:"))
    #C=int(input("Capacity /Doctor:"))  #same capacity for every doctor
    C=[]                                #same/different capacity for each doctor
    input_string=input("Capacity of Each Doctor:")  #input seperated by space " "
    C=input_string.split()
    C=[int(ele) for ele in C]  #turn into integers

    rank=input_patient_preference_list(N) #patients' preferences

    start_nodes,end_nodes,capacities,unit_costs,supplies=building_net(N, K, C, rank)
    min_cost_maximum_flow(N, start_nodes,end_nodes,capacities,unit_costs,supplies)
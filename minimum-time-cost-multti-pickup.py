import numpy as np

durations = [[0,2,31,4,51,9,12,88,99],[0,2,31,4,51,9,12,88,7],[6,0,8,7,9,10,12,33,88],[11,77,12,0,14,15,43,21,88],[2,55,10,13,0,20,32,12,88],[11,21,23,24,0,12,11,55,66],[1,2,3,55,4,5,6,7,66],[1,22,33,44,55,66,55,43,55],[1,22,33,44,55,55,66,43,44]]
drivers_count = 3
trips_count_pickup_list = [2,3,1]


def find_minimum_cost_time_assigning(durations, drivers_count, trips_count_pickup_list):
    import copy
    new_durations = copy.deepcopy(durations)
    new_trips_count_pickup_list = copy.deepcopy(trips_count_pickup_list)
    all_custumized_assignations = []
    for step in range(len(trips_count_pickup_list)):
        step_opt = optimizer_driver_to_pickup_points_in_special_sorting_trips(new_durations, drivers_count, new_trips_count_pickup_list, step)
        all_custumized_assignations.append(step_opt)
        change_order_one_step(new_durations, new_trips_count_pickup_list, drivers_count)
    print('all_custumized_assignations :', all_custumized_assignations)
    for i in range(len(all_custumized_assignations)):
        cost_time = 0
        best_cost_time = 0
        for j in range(len(trips_count_pickup_list)) : 
            cost_time += all_custumized_assignations[i][j][3] 
        print(cost_time) 
        if not(i):
            best_assination = all_custumized_assignations[i]
            best_cost_time = cost_time
        else :
            if cost_time < best_cost_time :
                best_assination = all_custumized_assignations[i]
                best_cost_time = cost_time
    
    return best_assination

def optimizer_driver_to_pickup_points_in_special_sorting_trips(durations, driver_count, trips_count_pickup_list, step):
    import copy
    trips_count = len(trips_count_pickup_list)
    INF = 1e10
    duration_matrix = copy.deepcopy(durations)
    horizontal_index = 0
    driver_assigned_to_trips = []
    for i in range(trips_count):
        if(i==0):
            horizontal_index += driver_count
        else: 
            horizontal_index += trips_count_pickup_list[i]-1
        in_trips_driver_selected=[]

        for j in range(trips_count_pickup_list[i]):
            for k in range(driver_count):
                time = duration_matrix[k][horizontal_index+j]
                if not(k) and not(j) :
                    in_trips_driver_selected = [i, j, k, time]
                else:
                    if time < in_trips_driver_selected[3]:
                        trip_index = i+step if i+step < len(trips_count_pickup_list) else i+step-len(trips_count_pickup_list)

                        in_trips_driver_selected = [trip_index, j, k, time]
            selected_driver = in_trips_driver_selected[2]
        for t in range(len(duration_matrix[in_trips_driver_selected[2]])):
            duration_matrix[in_trips_driver_selected[2]][t] = INF
        driver_assigned_to_trips.append(in_trips_driver_selected)
    return(driver_assigned_to_trips)
            
def change_order_one_step(durations, trips_count_pickup_list, drivers_count):
    for j in range(drivers_count):
        for i in range(trips_count_pickup_list[0]):
            x= durations[j].pop(drivers_count)
            durations[j].append(x)
    y = trips_count_pickup_list.pop(0)
    y = trips_count_pickup_list.append(y)
    return(durations)











print('minimums',find_minimum_cost_time_assigning(durations, drivers_count, trips_count_pickup_list))
# print(change_order_one_step(durations, trips_count_pickup_list, driver_count))
# print(optimizer_driver_to_pickup_points_in_special_sorting_trips(durations, driver_count, trips_count_pickup_list))

# def optimize_driver_to_pickup_points(drivers,trips):
#     count_trips = len(trips)
#     count_drivers = len(drivers)
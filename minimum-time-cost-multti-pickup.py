import numpy as np
durations = [[0,2,31,4,51,9,12],[6,0,8,9,10,12,33],[11,12,0,14,15,43,21],[2,10,13,0,20,32,12],[11,21,23,24,0,12,11],[1,2,3,4,5,6,7],[1,22,33,44,55,66,43]]
driver_count = 2
trips_count_pickup_list = [2,3]

def optimizer_driver_to_pickup_points(duration_matrix, driver_count, trips_count_pickup_list):
    trips_count = len(trips_count_pickup_list)
    print(duration_matrix)
    INF = 1e10
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
                        in_trips_driver_selected = [i, j, k, time]
            selected_driver = in_trips_driver_selected[2]
            print(selected_driver)
            duration_matrix[in_trips_driver_selected[2]][0:len(duration_matrix[0])-1]=INF
            print(duration_matrix)
        driver_assigned_to_trips.append(in_trips_driver_selected)
    return(driver_assigned_to_trips)
            
def rotate_trips(durations, driver_count, step):
    pass
    












optimizer_driver_to_pickup_points(durations, driver_count, trips_count_pickup_list)


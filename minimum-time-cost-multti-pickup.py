import numpy as np
durations = [[0,2,3,4,5,11,12],[6,0,8,9,10,12,33],[11,12,0,14,15,43,21],[2,10,13,0,20,32,12],[11,21,23,24,0,12,11],[1,2,3,4,5,6,7],[1,22,33,44,55,66,43]]
driver_count = 2
trips_count_pickup_list = [2,3]

def optimizer_driver_to_pickup_points(duration_matrix, driver_count, trips_count_pickup_list):
    trips_count = len(trips_count_pickup_list)
    print(duration_matrix)







    horizontal_index = 0

    for i in range(trips_count):
        if(i==0):
            horizontal_index += driver_count
        else: 
            horizontal_index += trips_count_pickup_list[i]-1
        
        for j in range(trips_count_pickup_list[i]):

            for k in range(driver_count):
                print(duration_matrix[k][horizontal_index+j])
            

    












optimizer_driver_to_pickup_points(durations, driver_count, trips_count_pickup_list)


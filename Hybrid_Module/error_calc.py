import numpy as np
from Hybrid_Module import loading_data
from Hybrid_Module.kmeans_clustering import *

# Evaluate accuracy of predictions
def rmsd_element (num1, num2):
    "Finds the inside of rmsd formula between two movie ratings"
    return ((float(num1))-(float(num2)))**2
      
def one_user_rmsd (m1, m2):
    "Finds the average rmsd for all of one user's movie ratings"
    sum = 0.0
    i = 0
    for index, (a, b) in enumerate(zip(m1, m2)):
        if b!=0:
            sum = sum+rmsd_element(a, b)
            i = i+1
        else:
            continue
    if i==0:
        rmsd_inside = 0
    else:
        rmsd_inside = sum/float(i)
    user_rmsd = np.sqrt(rmsd_inside)
    return user_rmsd

def calculate (user_cluster, centroids):
    "Finds the average rmsd for all users"
    test_matrix = loading_data.testing_load_data("u1.test", 1)
    
    total_rmsd = 0.0
    number_test_users = 0
    user_id = 0
    for test_user in test_matrix:
        actual = test_user
        predictions = centroids[user_cluster[user_id]]
        one_rmsd = one_user_rmsd (predictions, actual)
        total_rmsd = total_rmsd+one_rmsd
        user_id = user_id + 1
        if one_rmsd==0:
            continue
        else:
            number_test_users = number_test_users+1
    final_evaluation = total_rmsd/float(number_test_users)
    print("RMSD: %.5f" % final_evaluation)
     
    return final_evaluation

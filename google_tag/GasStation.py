# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:46:23 2018

@author: I309535
"""

class Solution:
    # @param A : tuple of integers
    # @param B : tuple of integers
    # @return an integer
    def canCompleteCircuit(self, A, B):
        maxFuelServing = -1
        minIndex = -1
        """
        for i in range(len(A)):
            fuel_serving = A[i]-B[i]
            if fuel_serving > maxFuelServing:
                maxFuelServing = fuel_serving
                minIndex = i
                
        if minIndex == -1:
            return -1
       """     
        start = minIndex
        n = len(A)
        for start in range(n):
            # forward
            fuelRemaining = 0
            fuel = True
            for i in range(start,n):
                fuel_serving = A[i]-B[i]
                fuelRemaining += fuel_serving
                if fuelRemaining < 0:
                    fuel = False
                    break
            if not fuel:    
                continue
            
            ## backward
            for i in range(0, minIndex):
                fuel_serving = A[i]-B[i]
                fuelRemaining += fuel_serving
                if fuelRemaining < 0:
                    fuel = False
                    break
            
            if fuel:
                return start
        return -1

gas =  [ 204, 918, 18, 17, 35, 739, 913, 14, 76, 555, 333, 535, 653, 667, 52, 987, 422, 553, 599, 765, 494, 298, 16, 285, 272, 485, 989, 627, 422, 399, 258, 959, 475, 983, 535, 699, 663, 152, 606, 406, 173, 671, 559, 594, 531, 824, 898, 884, 491, 193, 315, 652, 799, 979, 890, 916, 331, 77, 650, 996, 367, 86, 767, 542, 858, 796, 264, 64, 513, 955, 669, 694, 382, 711, 710, 962, 854, 784, 299, 606, 655, 517, 376, 764, 998, 244, 896, 725, 218, 663, 965, 660, 803, 881, 482, 505, 336, 279 ]
cost = [ 273, 790, 131, 367, 914, 140, 727, 41, 628, 594, 725, 289, 205, 496, 290, 743, 363, 412, 644, 232, 173, 8, 787, 673, 798, 938, 510, 832, 495, 866, 628, 184, 654, 296, 734, 587, 142, 350, 870, 583, 825, 511, 184, 770, 173, 486, 41, 681, 82, 532, 570, 71, 934, 56, 524, 432, 307, 796, 622, 640, 705, 498, 109, 519, 616, 875, 895, 244, 688, 283, 49, 946, 313, 717, 819, 427, 845, 514, 809, 422, 233, 753, 176, 35, 76, 968, 836, 876, 551, 398, 12, 151, 910, 606, 932, 580, 795, 187 ]    
print Solution().canCompleteCircuit(gas,cost)
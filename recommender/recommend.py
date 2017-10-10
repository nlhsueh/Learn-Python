#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 20:52:33 2017

@author: nlhsueh
"""

from math import sqrt

class DistanceComputer:
    def manhattan(rating1, rating2):
        """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
           of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
        distance = 0
        commonRatings = False
    
        for key in rating1:
            if key in rating2:
                distance += abs(rating1[key] - rating2[key])
                commonRatings = True
        if commonRatings:
            return distance
        else:
            return -1 #Indicates no ratings in common   
            
    def pearson(rating1, rating2):
        sum_xy = sum_x = sum_y = sum_x2 = sum_y2 = 0
        n = 0
        for key in rating1:
            if key in rating2:
                n += 1
                x = rating1[key]
                y = rating2[key]
                sum_xy += x * y
                sum_x += x
                sum_y += y
                sum_x2 += pow(x, 2)
                sum_y2 += pow(y, 2)
        # now compute denominator
        denominator = sqrt(sum_x2 - pow(sum_x, 2) / n) * sqrt(sum_y2 - pow(sum_y, 2) / n)
        if denominator == 0:
            return 0
        else:
            return (sum_xy - (sum_x * sum_y) / n) / denominator
            
def computeNearestNeighbor(username, users, dis):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    for user in users:
        if user != username:
            if dis == 0:  
                distance = DistanceComputer.manhattan(users[user], users[username])
            else:
                distance = DistanceComputer.pearson(users[user], users[username])

            distances.append((distance, user))
    # sort based on distance -- closest first
    distances.sort()
    print ("The distances to " + username + " are (sorted): ", distances)
    return distances

def recommend(username, users, dis=0):
    """回傳一個推薦的 list, 排序"""

    # 1. 找到與我最近的人, nearestPerson
    neighbors = computeNearestNeighbor(username, users, dis)
    nearestPerson = neighbors[0][1]
    nearestDis = neighbors[0][0]
    
    print("和我最相近的人: ", nearestPerson, ", dis=", nearestDis)

    # 2. nearestPerson 有 rate 但我沒有 rate 的資料組成一個 list
    recommendations = []
    neighborRatings = users[nearestPerson]
    userRatings = users[username]
    print ("推薦者的 rating: ", neighborRatings)
    print ("我的 rating: ", userRatings)
    
    for artist in neighborRatings:
        if not artist in userRatings:
            recommendations.append((artist, neighborRatings[artist]))
    recommendations = sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse = True)
    print ("給我的推薦列表：", recommendations)     
    # using the fn sorted for variety - sort is more efficient
    return recommendations
# Basic Dijkstra — Most Important
# You are given a weighted graph with V vertices and E edges. All edge weights are non-negative. Given a source vertex S, find the shortest distance from S to every other vertex.

import heapq
def dij(graphs,st):
    dis={}
    prev={}
    for node in graphs:
        dis[node]=float("inf")
        prev[node]=None
    dis[st]=0
    pri_que=[(0,st)]
    while pri_que:
        curr_dis,curr_node=heapq.heappop(pri_que)
        if curr_dis>dis[curr_node]:
            
             









            






          






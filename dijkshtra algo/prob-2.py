# Basic Dijkstra — Most Important
# You are given a weighted graph with V vertices and E edges. All edge weights are non-negative. Given a source vertex S, find the shortest distance from S to every other vertex.

import heapq
def dij(graph,st):
    dis={}
    prev={}
    for node in graph:
        dis[node]=float("inf")
        prev[node]=None
    dis[st]=0
    pre_que=[(0,st)]
    while pre_que:
        cur_dist,cur_node=heapq.heappop(pre_que)
        if cur_dist>dis[cur_node]:
            continue
        for nei,wt in graph[cur_node]:

            new_dis=cur_dist+wt
            if new_dis<dis[nei]:
                dis[nei]=new_dis
                prev[nei]=cur_node
                heapq.heappush(pre_que,(new_dis,nei))


    return dis,prev
graph={
    "A":[("B",2),("D",8)],
        "B":[("A",4),("D",5),("E",4)],
        "D":[("A",8),("B",5),("E",3),("F",7)],
        "E":[("B",9),("D",8),("F",1),("C",9)],
        "F":[("D",2),("E",1),("C",9)],
        "C":[("E",9),("F",22)]

}
st="A"
en="d"

            
dis,prev=dij(graph,st)
print(dis["D"])













 








            






          






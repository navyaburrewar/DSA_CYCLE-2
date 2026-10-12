import heapq
def dij(grapgh,st):
    dis={}
    prev={}
    for node in grapgh:
        dis[node]=float("inf")
        prev[node]=None

    dis[st]=0
    pre_que=[(0,st)]
    while pre_que:
        curr_dis,curr_node=heapq.heappop(pre_que)
        if curr_dis>dis[curr_node]:
            continue
        for nei,wt in grapgh[curr_node]:
            new_dis=curr_dis+wt
            if new_dis<dis[nei]:
                dis[nei]=new_dis
                prev[nei]=curr_node
                heapq.heappush(pre_que,(new_dis,nei))

    return dis,prev           
grapgh={
    "A":[("B",2),("D",6)],
        "B":[("A",1),("D",5),("E",4)],
        "D":[("A",8),("B",3),("E",3),("F",7)],
        "E":[("B",9),("D",8),("F",1),("C",9)],
        "F":[("D",1),("E",1),("C",9)],
        "C":[("E",9),("F",5)]
    
    }


st="A"
end="B"

dis,prev=dij(grapgh,st)
print(dis,prev)






                 











        












        
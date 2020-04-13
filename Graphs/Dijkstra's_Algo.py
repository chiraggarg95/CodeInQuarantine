import numpy as np
import math

def sp_min_idx(arr, idx_list):
    min=math.inf
    for i in idx_list:
        if arr[i]<min:
            min=arr[i]

    return arr.index(min)

def Dijkatra_mtd(source, connections, weights):
   
    nodes=len(connections)
    nodes_left=np.arange(nodes)

    dist=[math.inf]*nodes
    dist[source]=0

    while len(nodes_left) !=0 :
        
        curr_node=sp_min_idx(dist, nodes_left)

        for adj_node in connections[curr_node]:

            if adj_node in nodes_left:

                add_dist=weights[curr_node][connections[curr_node].index(adj_node)]       #dist between current node and adjacent node

                if ((dist[curr_node]+add_dist)<dist[adj_node]):
                    dist[adj_node]=dist[curr_node]+add_dist

        nodes_left=np.delete(nodes_left, np.where(nodes_left==curr_node))

        # print('loop running')        #checkpoint

    return dist



#receiving and organising input

nodes=int(input())

connections=[]
weights=[]

for node in range(nodes):
    connected_to=int(input())
    connected_nodes=[]
    connection_weights=[]
    while connected_to != 0:
        a=input().split()
        connected_nodes.append(int(a[0]))
        connection_weights.append(int(a[1]))
        connected_to-=1
    connections.append(connected_nodes)
    weights.append(connection_weights)

#checking inputs

# print(connections)
# print(weights)

#inputs correctly taken

source=0                #assumption that source node is always 0
print(Dijkatra_mtd(source, connections, weights))

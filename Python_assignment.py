import numpy as np
visited=[]
next_row=[]
cost=[]
visited_city=[]
def find_coordinates(x):
    cord = np.where(graph == x)
    listOfCoordinates=(list(zip(cord[0], cord[1])))
    cord=choose_cordinate(listOfCoordinates)

def choose_cordinate(x):
    if len(visited)==0:
        visited.append(x[0])
        change_visited(x[0])
        next_row.append(x[0][1])
    elif len(visited)>0:
        for c in x:
            if c[0]==visited[len(visited)-1][1]:
                change_visited(c)
                visited.append(c)
                next_row.append(c[1])
                break

def change_visited(c):
    for row in range (0,8):
        for col in range (0,8):
            if col==c[0] or col==c[1]:
                graph[row][col]=9999999

def go_to_row():
    x=next_row[len(next_row)-1]
    next_min=(min(graph[x]))
    cost.append(next_min)
    find_coordinates(next_min)

def print_path():

    match={0:"Mysore",1:"Mandya",2:"Chennapatna",3:"Nanjangud",4:"Bandipur",5:"Nagarhole",6:"Somnathpur",7:"Bylakuppe"}
    for x in visited:
        for y in x:
            visited_city.append(match[y])

    counter=0
    for x in range(0,len(visited_city)-1):
        if x%2==0 or x==0:
            print(visited_city[x],"-->",visited_city[x+1],"  cost:",cost[counter])
            x=x+1
            counter=counter+1
        else:
            print(" ")
graph = np.array([[ 9999999,66,28,60,34,34,3,108],
    [66,9999999,22,12,91,121,111,71],
    [ 28,22,9999999,39,113,130,35,40],
    [ 60,12,39,9999999,63,21,57,83],
    [ 34,91,113,63,9999999,9,50,60],
    [ 34,121,130,21,9,9999999,27,81],
    [ 3,111,35,57,50,27,9999999,90],
    [ 108,71,40,83,60,81,90,9999999]])

initial_min=graph.min()
cost.append(initial_min)
find_coordinates(initial_min)
count=0
while count<6:
    go_to_row()
    count=count+1
print(" ")
print("-----------------------------")
print_path()
print("-----------------------------")
print(" ")
print("The total minimum cost path",sum(cost))

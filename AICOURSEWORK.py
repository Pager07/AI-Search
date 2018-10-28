import numpy as np
import networkx as nx
import heapq

file_path = "/Users/sandeep/Desktop/Year 2/SoftwareMethod/AI-Search/NEWAISearchfile012.txt"

f = open(file_path, "r")

#striping away empty lines

raw_text = [line for line in f.readlines() if line.strip()]

#striping away /r/n
raw_text = [string.rstrip() for string in raw_text] 


def get_num_cities():
    unprocessed_size_string = raw_text[1]
    size_string = ""
    for letter in unprocessed_size_string:
        if letter.isdigit():
            size_string += letter
    
    num_cities = int(size_string)
    return num_cities
    

#make a function that makes the matrix
#this is your f(x)
def distance_matrix():
    #getting the num of cities
    unprocessed_size_string = raw_text[1]
    size_string = ""
    for letter in unprocessed_size_string:
        if letter.isdigit():
            size_string += letter
    
    num_cities = int(size_string)
    
    #creating an empty matrix using num_cities
    mat = np.zeros((num_cities , num_cities), dtype = int)
    
    #removing the first 2 line or string(like the size = 12 part of it)
    #and spliting on commas
    distance_list = [raw_text[i].split(",") for i in range(2,len(raw_text))]
    distance_list = [int(num) for string in distance_list for num in string if(len(num)!=0)]
    #distacne_list= now will contain [13,.....all nums] and removing all empty rows
    #populate matrix
    #set a pointer in the list 
    #only move the pointer if you put the value it is pointing to
    # but when x>y or x=y you dont have to.
    rows = num_cities 
    cols = num_cities
    distance_list_pointer = 0
    for x in range(rows):
        for y in range(cols): 
            if x < y: 
              mat[x,y] = distance_list[distance_list_pointer] 
              distance_list_pointer = distance_list_pointer +1 
            
            elif x > y:
                mat[x,y] = mat[y,x]          
    return mat

mat = distance_matrix()
G = nx.Graph()

#this fuction updates this visisted list of state
#gives us a list, this list will be your states 'visited' list
def update_visited(current_state_id ,current_city,city):
    #making of 'visited' for inital state
    if current_city == city and current_state_id == 1:
        visited_list = [city]
    #making of 'visited' of state other than intital state
    else:
        #this line ensusres that we creat a new list and repointing poniters
        visited_list = G.node[current_state_id]['state_info']['visited'][:]
        visited_list.append(city)
    return visited_list
    

def find_heuristic(current_city,city,visited_list):
    min_distance_option = []
    city_distances = mat[city] 
    for city , distance in enumerate(city_distances):
        if city not in visited_list:
            min_distance_option.append(city_distances[city])
            
    if len(min_distance_option) == 0:
        print("LAST CITY")
        h_value = mat[ visited_list[-1] ][ visited_list[0]  ]
    else:  
        h_value = min(min_distance_option)
    return h_value

def find_path_cost(visited_list):
    path_cost = 0
    if len(visited_list) != 1:
        pointer = 0
        while pointer < len(visited_list)-1:
            first_city = visited_list[pointer]
            second_city = visited_list[pointer+1]
            first_second_path_cost = mat[first_city][second_city]
            path_cost = path_cost + first_second_path_cost
            pointer = pointer+1
        return path_cost
    else:
        return path_cost
        
        
def find_a_star_value(h_value , pc):
    a_star = h_value + pc
    return a_star        
        
def find_state_id():
    state_id = len(list(G.nodes))+1
    return state_id




#Getting node data 
#G.node[city]['state_info']['h']





def get_state_id(city):
    for state in list(G.nodes):
        last_city_visited = G.node[state]['state_info']['visited'][-1]
        if city == last_city_visited:
            return G.node[state]['state_info']['state_id'] 
    return -1



unvisited_states_id = []

#pass in a node and the ciy you want to add
#it will create a new state eg . state1 =[0] ,now new state2 = [0,3]
#it will also at the state2 in unvisited_states_id
def create_state(current_state_id,city):
    
    current_city = G.node[current_state_id]['state_info']['visited'][-1]
    state_id = find_state_id()
    visited_list = update_visited(current_state_id,current_city ,city)
    
    # if it is a goal node we are making, then h_vlaue = 0 ,else,normal
    if city in G.node[current_state_id]['state_info']['visited']:
        h_value = 0
    else:
        h_value = find_heuristic(current_city,city,visited_list)
    
    pc = find_path_cost(visited_list)
    a_star = find_a_star_value(h_value,pc)
    
    feed_dict = {'h':h_value,
                 'pc':pc,
                 'a_star':a_star,
                 'visited':visited_list,
                 'state_id':state_id
                }
    G.add_node(state_id , state_info = feed_dict)
    G.add_edge(current_state_id, state_id)
    unvisited_states_id.append(state_id)


def initial_state_node(start_city):
    visited_list = update_visited(1, start_city ,start_city)
    pc = find_path_cost(visited_list)
    h_value = find_heuristic(start_city,start_city,visited_list)
    a_star = find_a_star_value(h_value , pc)
    state_id = find_state_id()
    feed_dict = {'h': h_value,
                 'pc': pc,
                 'a_star':a_star,
                 'visited':visited_list,
                 'state_id': state_id
                }
    G.add_node(state_id, state_info = feed_dict)
    unvisited_states_id.append(state_id)
#Assumming that I have found the A* hence the min state
#I want to remove the current state id from unvisited_state_id
#creats all posible state from a state
#returns you all the all child of that state of A STATE(it wont now)
#CREAT_STATE WILL AUTOMATICALLY ADD THE CREATED NODE IN THE UNVISITED_STATE_ID
def create_all_states(current_state_id):
    #remove current state id
    unvisited_states_id.remove(current_state_id)
    #making the other all child state for the node
    visited = G.node[current_state_id]['state_info']['visited']
    current_city = visited[-1]
#    state_child_states_id=[]
    city_distance = mat[current_city]
    for city,distances in enumerate(city_distance):
#        print("I have entered for loop")
#        print("city:{} , visitedd:{}".format(city , visited))
        if city not in visited:
            create_state(current_state_id ,city)
#            print("I have created a state")
            state_id = get_state_id(city)
            if state_id == -1:
                raise Exception('State for city {} was -1'.format(city))
#            else:
#                state_child_states_id.append(state_id)
#    return state_child_states_id

    
total_cities = get_num_cities()
#from all the unvisited child_states in the tree
# pick this node with smallest A* vlaue
def transition(unvisited_states_id):
    #for all the childs, getting their a* vlaues
    a_star_vlaues = []
    for unvisited_state_id in unvisited_states_id:
        if total_cities == len(G.node[unvisited_state_id]['state_info']['visited']):
            return unvisited_state_id
        else:
            a_star = G.node[unvisited_state_id]['state_info']['a_star']
            a_star_vlaues.append(a_star)
#    print("Univisited_states_id:",unvisited_states_id)
    #finding the index of the min A* value
    min_state_id_index = np.argmin(a_star_vlaues)
    #getting the state for that index
    min_state_id = unvisited_states_id[min_state_id_index]
    
    return min_state_id


    
    


def a_star_search(city): 
    
    initial_state_node(city)
    goal_state_found = False
    while(goal_state_found == False):
        #we are picking an node
        min_state_id = transition(unvisited_states_id)
        op=G.node[min_state_id]['state_info']['visited']
        pc =G.node[min_state_id]['state_info']['pc']
        a_star = G.node[min_state_id]['state_info']['a_star']
        print("Optimal Path:{} ,Num_cities:{}, Path Cost:{},A*:{}".format(op ,len(op) ,pc,a_star))
        #before expanding all the possible states from this state
        #check if the initial node= goal noddde
        #if numberofvisited cities in that node is == to number of citites
        #then we know we are in goal node
        visited = G.node[min_state_id]['state_info']['visited']
        if(total_cities == len(visited)):
            #this create state will craet a goal state
            #Because we are passing in a city that already exxist in visited list
            create_state(min_state_id , city)
            goal_state =unvisited_states_id[-1]
            optimal_path = G.node[goal_state]['state_info']['visited']
            optimal_path_cost = G.node[goal_state]['state_info']['pc']
            goal_state_found = True
            return optimal_path , optimal_path_cost
        
        create_all_states(min_state_id)
        #now we have created the branches
        #pick a state and do it agian

        
    
    
    
    
        
    
r , pc = a_star_search(0)   
    
    

        
        
        
        
    
    
    
                
            
         

    

    
    
    
    
    
    
    
    
    
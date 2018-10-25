import numpy as np
import networkx as nx

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

def update_visited(current_state_id ,current_city,city):
    if current_city == city and current_state_id == 1:
        visited_list = [city]
    else:
        visited_list = G.node[current_state_id]['state_info']['visited'][:]
        visited_list.append(city)
    return visited_list
    

def find_heuristic(current_city,city,visited_list):
    min_distance_option = []
    city_distances = mat[city] 
    for city , distance in enumerate(city_distances):
        if city not in visited_list:
            min_distance_option.append(city_distances[city])
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


#Getting node data 
#G.node[city]['state_info']['h']

initial_state_node(0)
#pass in a node and the ciy you want to add
def create_state(current_state_id,city):
    current_city = G.node[current_state_id]['state_info']['visited'][-1]
    state_id = find_state_id()
    visited_list = update_visited(current_state_id,current_city ,city)
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


create_state(1,1) 
    
    
    
    
    
    
    
    
    
        
        
            
            
            
            
    
        
        
    
    
    
    
def a_star_search(start_city):
    #
    minimum_history=[]
    
    



##finding heuristice values for each node
#h(x) = distacne to next node(smallest)
#
#def heuristic_values(mat, visited_cities):
#    #i want to get min value for each city unvisted city/row
#    #i dont know which cities are viested 
#    #but there was zero, becuase there was distacne connected to itslef
#    #so i said if, where valvue is greater than 5, do nothing,elese replace it with max value
#    #then just pick the min
#    #example [0,1,4,6]->[6,1,2,6] and now pick miniimun
#    #here I removed the zeros
#    mat = np.where(mat>0, mat,mat.max())
#    #i need to know where the minimum value came from
#    #[6,6,2,6]
#    #[2,1,3,5]
#    #may be i could replace the value with max (x,ycurrent) every time i pick a min
#    #so for (1,5) i will go to (1,5) and replace it with max value
#    #so it wound be choosen
#    rows = get_num_cities()
#    cols = get_num_cities()
#    h_values = []
#    print(rows, cols)
#    current_min = mat.max()
#    for  row in range(rows):
#        for col in range(cols):
#            if mat[row][col] < current_min:
#                current_min = mat[row][col]
#        h_values.append(current_min)           
#        mat[col][row] = mat.max()          
#        current_min = mat.max()
#    
#    return h_values

    
    
    





   
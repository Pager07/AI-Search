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
def initial_state_node(start_city):
    visited_list = [start_city]
    pc = 0
    min_distance_option = []
    city_distances = mat[start_city] 
    for city , distance in enumerate(city_distances):
        if city not in visited_list:
            min_distance_option.append(city_distances[city])
    print(min_distance_option)
    h_value = min(min_distance_option)
    feed_dict = {'h': h_value,
                 'pc': pc,
                 'visited':visited_list
                }
    G.add_node(0 ,state_info = feed_dict)
    print(h_value , pc , visited_list)


initial_state_node(0)
    
    
        
        
            
            
            
            
    
        
        
    
    
    
    
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

    
    
    





   
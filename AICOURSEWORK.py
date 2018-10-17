import numpy as np
file_path = "/Users/sandeep/Desktop/Year 2/SoftwareMethod/CourseWork/NEWAISearchfile012.txt"

f = open(file_path, "r")

#striping away empty lines

raw_text = [line for line in f.readlines() if line.strip()]

#striping away /r/n
raw_text = [string.rstrip() for string in raw_text] 



#make a function that makes the matrix
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


   
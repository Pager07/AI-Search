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
    matrix = [[] for i in range(num_cities)]
    
    
    distance_string = ""
    for i in range(2,len(raw_text)):
        distance_string += raw_text[i]
    
    distance_string = .split(",") 
        
    return distance_string

x = distance_matrix()
   
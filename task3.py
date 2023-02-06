""" 
Task 3:
Read the throughput values from a file and then use your jainsall function to calculate a JFI.
The text file contains:
7 Mbps
12 Mbps
15 Mbps
32 Mbps
You should only consider the numeric values. 
"""
import task2    #imports task2 (and its functions)

speedList = []  #defines a new list
with open("task3.txt") as file_name:    #opens the text document as file_name
    for line in file_name:  #loops through each line in the document
        #line.split splits the line in the document. We want the number in position 0
        #float casts the string number to a float number
        #append puts the float number in the list
        speedList.append(float(line.split()[0]))

    result = task2.jainsall(speedList)  #sends the list to the jainsall function
    print(result)   #prints the result
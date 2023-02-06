""" 
Task 4:
Read the throughput values from a file and then use your jainsall function to calculate a JFI. Note:
you must use the same units.
The text file contains:
7 Mbps
1200 Kbps
15 Mbps
32 Mbps 
"""

import task2    #imports task2 (and its functions)

speedList = []  #defines a new list
with open("task4.txt") as file_name:    #opens the text document as file_name
    for line in file_name:  #loops through each line in the document
        #line.split splits the line in the document based on spaces. We want the number in position 0
        #float casts the string number to a float number
        #append puts the float number in the list

        #if the line two after split is Kbps it divides the number by 1000 before adding it to the list
        if line.split()[1] == "Kbps":
            speedList.append((float(line.split()[0])) / 1000)
        else:
            speedList.append(float(line.split()[0]))
    print(speedList)    #prints the list to check that kbps have been converted
    result = task2.jainsall(speedList)  #sends the list to the jainsall function
    print(result)   #prints the result
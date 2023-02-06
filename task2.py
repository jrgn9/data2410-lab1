# Tekstlig beskrivelse av Jains Fairness Index formelen:
# Over brøkstreken: Summerer alle hastighetene, og opphøyer summen i 2
# Under brøkstreken: Summerer alle hastighetene opphøyd i 2, og ganger den summen med antall "hastigheter"

# Task 2: Write a new function jainsall function that takes a list of throughput values (integers and/or float) and returns a JFI.

def jainsall(x):    #defines function that takes list x
    sumSquared = 0 #needs to define variable first to not get UnboundLocalError in the for loop
    try:
        #tries to take sum of list x
        total = sum(x)
    except:
        #if there is no sum we get error message
        print("Something went wrong")
    else:   #code block runs when there are no errors
        overLine = total**2 #sum squared over the line of the expression
        for number in x: #for loop iterating the input list
            sumSquared += number**2  #adds the number in the list squared to sumSquared

        underLine = sumSquared * len(x) #sum of squares multiplied with length of list under the line of the expression
        jfi = overLine/underLine    #the formula is overLine divided by underLine
        #print(jfi)
        return jfi  #returns the jfi

""" list=[8, 2.5, 3, 1, 3]
listFeil=[8, 2.5, 3, 1, 'poopy']
jainsall(list)
jainsall(listFeil) """
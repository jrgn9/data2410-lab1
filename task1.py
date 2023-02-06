# Tekstlig beskrivelse av Jains Fairness Index formelen:
# Over brøkstreken: Summerer alle hastighetene, og opphøyer summen i 2
# Under brøkstreken: Summerer alle hastighetene opphøyd i 2, og ganger den summen med antall "hastigheter"

# Task 1: Write a function named jains that takes two throughput values (int and/or float) as arguments and returns a JFI.
def jains(x, y):    #defines function that takes two values: x,y
    #try, except, else for error handling.
    try:
        #tries to cast input to float and adds them together
        total = float(x) + float(y)
    except:
        print("Something went wrong") #error message to console if it cant cast input
    else: #code block to execute if casting succeeds
        sumSquared = x**2 + y**2    #adds the squares of x and y
        overLine = total**2    #sum squared over the line of the expression
        underLine = sumSquared * 2  #sum of squares multiplied with amount (2) under the line of the expression
        jfi = overLine/underLine  #the formula is overLine divided by underLine
        return jfi  #returns results
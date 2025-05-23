# data2410-lab1

> ## ⚠️ Migrated to Codeberg
>
> This project has [migrated to Codeberg](https://codeberg.org/jrgn9/cheater).

## Introduction
Fairness measures or metrics are used in computer networks to determine whether users or applications
are receiving a fair share of system resources. Commonly, the throughput of competing transfers
(“flows”) is measured in experiments or obtained via simulations, and they are used to calculate Jains
Fairness Index (JFI) [1], using the formula.

Here, N is the total number of flows, and xi (t) is the throughput of the ith connection — the
output ranges from 1/N to 1 where the value 1 indicates that all flows get the same allocation.

### Task 1
Write a function named jains that takes two throughput values (int and/or float) as arguments and
returns a JFI.

### Task 2
Write a new function jainsall function that takes a list of throughput values (integers and/or float)
and returns a JFI.

### Task 3
Read the throughput values from a file and then use your jainsall function to calculate a JFI.
The text file contains:
7 Mbps
12 Mbps
15 Mbps
32 Mbps
You should only consider the numeric values.

### Task 4
Read the throughput values from a file and then use your jainsall function to calculate a JFI. Note:
you must use the same units.
The text file contains:
7 Mbps
1200 Kbps
15 Mbps
32 Mbps

### Submission
This is a Group assignment. I’ve already created groups for you (click people and then click lab-
assignment to see the groups in canvas). Please choose your own group members (maximum: 5
members per group).
1. Submit group-name.zip. Your zip file should include 4 separate python files (task1.py, task2.py,
task3.py, task4.py).
2. document all the variables and definitions.
3. document the following for each function:
   
   • what the function does.
   
   • what input and output parameters mean and how they are used.
   
   • what the function returns.
   
   • how you handle exceptions.

# Things to use in this program
# List, list functions
# tuples
# functions, returns
# if statements
# comparators
#this is a test

from CalculatorFunctions import errorCheck
from CalculatorDictionaries import Menu

print("-------------------Multi Function Calculator-------------------")

print("\tAdd:\t\t1")
print("\tSubtract: \t2")
print("\tMultiply: \t3")
print("\tDivide: \t4")

userSelection = input("Entry: ")
userSelection = errorCheck(userSelection, 0)
print(Menu[userSelection](userSelection))

'''
    (*)Translate algorithm from matlab/python to C/C++

    (*)Profiling the code, understanding how long the functions take to execute, how much memory does the code take, break it down into sections. Clock speed, cycles. 

    Partial deployment. Get microcontroller working on the FPGA and talking to the sensors. Using I2c if desired. Reading sensor data on the microcontroller. 

    Full deployment. Talking to sensors, getting a state and reading a state estimation. 

    Stretch goals: applying algorithm and feeding it into controller. Taking current position of bee and using that to determine the next position in space. Drive actuator. 

    Taking all of profile data and determining where bottlenecks are and eliminate them with some sort of digital logic. 

    Number representations 
'''

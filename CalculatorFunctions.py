def errorCheck(userInputData, allowNegNumsSwitch):                              # errorCheck(someString, 1(on) / 0(off))
    isNumber = False                                                            # start by assuming string is not valid

    while not isNumber:                                                         # loop through input string each time the user provides a string
        if userInputData.isdigit():                                             # if the user's string is only numbers
            isNumber = True                                                     # set the check variable true and allow the loop to end

        if userInputData:                                                       # if the string is not empty
            if allowNegNumsSwitch == 1 and userInputData[0] == '-':             # check if the allowNegNums switch is on
                isNumber = True                                                 # allow negative numbers to pass through the error check

        if isNumber is False:                                                   # if the check variable is false
            print("ERROR, please select a valid computation\n")                 # ask the user to input entry again
            userInputData = input("Entry: ")
    # end while

    if allowNegNumsSwitch == 0:
        while int(userInputData) > 4 or int(userInputData) < 1:                 # if the user entered value is not an integer between 1-4
            print("ERROR, please select a valid computation")                   # throw an error
            userInputData = input("Entry: ")                                    # and ask the user to try again
            userInputData = errorCheck(userInputData, 0)      # validate user entered string again
        #end while

    return userInputData                                                        # return acceptable entry. e.g, no letters, symbols, spaces, empty entries
#end errorCheck()

def arithmetic(userInputData):                                                  # arithmetic(string value 1-4)

    addNum = 0                                                                  # initialize lists and variables to use
    i = 0
    userArithNum = []
    plusMinusSwitch = 0
    arithOutput = ""

    if int(userInputData) == 1:                                                 # if the user is adding numbers
        print("---------------------- SUM -----------------------")
        plusMinusSwitch = 0                                                     # set the plus minus switch to off (add numbers)

    elif int(userInputData) == 2:                                               # if the user is subtracting numbers
        print("------------------- DIFFERENCE -------------------")
        plusMinusSwitch = 1                                                     # set the plus minus switch to on (subtract numbers)

    print("Type \"=\" when done")

    userArithNum.append(input("Entry: "))                                       # add the first entry to the back of the list
    userArithNum[i] = errorCheck(userArithNum[i], 1)          # validate user entry
    if plusMinusSwitch == 1:                                                    # if the user is adding numbers
        addNum = int(userArithNum[0]) * 2                                       # begin the counting at twice the entered value
                                                                                # because line 68 will subtract one of these values

    while userArithNum[i] != "=":                                               # as long as the user hasn't entered '='

        if userArithNum[i] != "=" and plusMinusSwitch == 0:                     # if user does enter '=' and the plus minus switch is off
            userArithNum[i] = errorCheck(userArithNum[i], 1)  # check if the entry is a pos or neg number
            addNum += int(userArithNum[i])                                      # sum successive entries
                                                                                # 0 + n1 + n2 + n3

        elif userArithNum[i] != "=" and plusMinusSwitch == 1:                   # if user does enter '=' and the plus minus switch is on
            userArithNum[i] = errorCheck(userArithNum[i], 1)  # check if the entry is a pos or neg number
            addNum -= int(userArithNum[i])                                      # subtract successive entries
                                                                                # 2n1 - n1 - n2 - n3

        userArithNum.append(input("Entry: "))                                   # allow user to enter values

        i += 1                                                                  # increment the list
    #end while

    if plusMinusSwitch == 0:                                                    # display the correct header output for user
        arithOutput = f"Sum: {addNum}"
    elif plusMinusSwitch == 1:
        arithOutput = f"Difference: {addNum}"
    return arithOutput                                                          # display number sum to user
#end arithmetic()

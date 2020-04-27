number = str
number = raw_input ("what is number: ")
print ("The spin resulted in ", number, "...")
print ("Pay", number)
if (number in ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]):
    print ("Pay Black")
elif (number in ["0", "00"]):
    print ("Pay Green")
else:
    print ("Pay Red")
if (number in ["0", "00"]):
    print ("Pay", number)
elif (int (number) % 2 == 0):
    print ("Pay Even")
elif (int (number) % 2 != 0):
    print ("Pay Odd")
if (number in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18"]):
    print ("Pay 1 to 18")
elif (number == "0"):
    print ("Pay 0")
elif (number == "00"):
    print ("Pay 00")
else:
    print ("Pay 19 to 36")
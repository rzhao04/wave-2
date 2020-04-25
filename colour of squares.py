letter = str
letter = raw_input ("what is letter: ")
number = int
number = raw_input ("what is number: ")
if (letter in ["a", "c", "e", "g"] and int (number) % 2 != 0):
    print ("black")
elif (letter in ["a", "c", "e", "g"] and int (number) % 2 == 0):
    print ("white")
elif (letter in ["b", "d", "f", "h"] and int (number) % 2 != 0):
    print ("white")
else:
    print ("black")
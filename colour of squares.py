letter = str
letter = raw_input ("what is letter: ")
number = int
number = input ("what is number: ")
if ([letter in ["a", "c", "e", "g"] & number % 2 != 0):
    print ("black")
elif ([letter in ["a", "c", "e", "g"] & number % 2 == 0):
    print ("white")
if ([letter in ["b", "d", "f", "h"] & number % 2 != 0):
    print ("white")
else:
    print ("black")
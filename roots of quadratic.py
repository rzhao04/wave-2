a = float
a = input ("what is a: ")
b = float 
b = input ("what is b: ")
c = float
c = input ("what is c: ")
result = (b * b) - (4 * a * c)
if (result < 0):
    print ("there is not root")
root1 = float
root1 = (-b + (result ** 0.5)) / (2 * a)
root2 = float
root2 = (-b - (result ** 0.5)) / (2 * a)
root3 = float
root3 = (-b) / (2 * a)
if (result > 0):
    print ("there are two roots", root1, root2)
if (result == 0):
    print ("there is one root", root3)
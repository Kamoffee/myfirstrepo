a = int(input("Please enter first angle:"))
b = int(input("Please enter second angle:"))
c = int(input("Please enter third angle:"))

if (a + b + c != 180) or a < 0 or b < 0 or c < 0:
    print('The entered values are not valid')
else:
    if a > 90 or b > 90 or c > 90:
        print("The triangle is an obtuse triangle ")
    if a == 90 or b == 90 or c == 90: 
        print("The triangle is a right triangle ")
    else:
        print("The triangle is an acute triangle")

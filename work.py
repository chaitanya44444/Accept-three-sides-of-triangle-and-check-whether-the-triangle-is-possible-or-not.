side1 = float(input('Enter length for side 1: '))
side2 = float(input('Enter length for side 2: '))
side3 = float(input('Enter length for side 3: '))
if side1 >= side2 + side3:
    print('No')
elif side2>=side1 + side3:
    print('No')
elif side3>=side1 + side2:
    print('No')
else:
    print("triangle is valid")
 

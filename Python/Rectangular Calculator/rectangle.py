import calculate

length = float(input("Enter the length of the rectangle:" ))
width = float(input("Enter the width of rectangle: "))

area = calculate.area(length, width)
perimeter = calculate.perimeter(length, width)

print(f"The area of rectangle is: {area}")
print(f"The perimeter of rectangle is: {perimeter}")
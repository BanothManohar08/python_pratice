#default arguments
def area(length=8, width=5):
    print("Area of rectangle:", length * width)

area()  # Uses default values
print("---------")
area(10)
print("---------")
area(10, 6)
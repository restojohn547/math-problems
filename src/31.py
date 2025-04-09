def calculate_area(shape):
    if shape == "rectangle":
        length = int(input("Enter the length: "))
        width = int(input("Enter the width: "))
        area = length * width
        print(f"The area of {shape} is: {area}")
    elif shape == "circle":
        radius = float(input("Enter the radius: "))
        area = 3.14159 * (radius ** 2)
        print(f"The area of {shape} is: {area}")
    else:
        print("Unknown shape")

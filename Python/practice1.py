import math

def area_of_circle(radius):
    return math.pi * radius**2

def area_of_triangle(base, height):
    return 0.5 * base * height

def area_of_square(side):
    return side**2

def area_of_rectangle(length, width):
    return length * width

def area_of_parallelogram(base, height):
    return base * height

def area_of_trapezium(base1, base2, height):
    return 0.5 * (base1 + base2) * height

def area_of_ellipse(a, b):
    return math.pi * a * b

# Function to display menu
def calculate_area():
    print("\nSelect the shape to calculate the area:")
    print("1. Circle")
    print("2. Triangle")
    print("3. Square")
    print("4. Rectangle")
    print("5. Parallelogram")
    print("6. Trapezium")
    print("7. Ellipse")

    choice = input("\nEnter your choice: ")  # Input as string to match dictionary keys

    # Dictionary mapping user choice to corresponding function calls
    shape_functions = {
        "1": lambda: area_of_circle(float(input("Enter radius: "))),
        "2": lambda: area_of_triangle(float(input("Enter base: ")), float(input("Enter height: "))),
        "3": lambda: area_of_square(float(input("Enter side length: "))),
        "4": lambda: area_of_rectangle(float(input("Enter length: ")), float(input("Enter width: "))),
        "5": lambda: area_of_parallelogram(float(input("Enter base: ")), float(input("Enter height: "))),
        "6": lambda: area_of_trapezium(float(input("Enter base1: ")), float(input("Enter base2: ")), float(input("Enter height: "))),
        "7": lambda: area_of_ellipse(float(input("Enter semi-major axis (a): ")), float(input("Enter semi-minor axis (b): ")))
    }

    # Get the corresponding function from the dictionary and execute it
    result = shape_functions.get(choice, lambda: "Invalid input")()

    if isinstance(result, str):  # If invalid input was given
        print("\nError:", result)
    else:
        print(f"\nCalculated area is: {result:.2f}")

# Main function
if __name__ == "__main__":
    while True:
        calculate_area()
        again = input("\nDo you want to calculate area again? (yes/no): ").strip().lower()
        if again != "yes":
            print("Exiting program. Goodbye!")
            break

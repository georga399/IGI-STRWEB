from geometric_lib import circle, square

def main():
    try:
        with open('data/calc.txt', 'r') as f:
            arg = float(f.readline())
            print(f"Your input:{arg}")
            print(f"Circle.area: {circle.area(arg)}")
            print(f"Circle.perimetr: {circle.perimeter(arg)}")
            print(f"Square.area: {square.area(arg)}")
            print(f"Square.perimeter: {square.perimeter(arg)}")
    except:
        print("Something went wrong")

if __name__ == "__main__":
    main()

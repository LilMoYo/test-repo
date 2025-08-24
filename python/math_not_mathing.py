import math
def area_calc_menu():
    print("===============")
    print("Area Calculator")
    print("===============")

    print("1) Triangle")
    print("2) Rectangle")
    print("3) Square")
    print("4) Circle")
    print("5) Quit")
    
area_calc_menu()
option_prompt = "Enter your option: "
option = int(input(option_prompt))
while option != 5:

    if option == 1:
        base = float(input("Base: "))
        height = float(input("Height: "))
        Area = (base * height)/2
        print("------------------")
        print(f"The area is {Area}")
        area_calc_menu()
        option = int(input(option_prompt))
        
    elif option == 2:
        length = float(input("Length: "))
        width = float(input("Width: "))
        Area = length * width
        print("------------------")
        print(f"The area is {Area}")
        area_calc_menu()
        option = int(input(option_prompt))
        
    elif option == 3:
        side = float(input("Side: "))
        Area = side ** 2
        print("------------------")
        print(f"The area is {Area}")
        area_calc_menu()
        option = int(input(option_prompt))
        
    elif option == 4:
        radius = float(input("Radias: "))
        Area = math.pi * (radius ** 2)
        print("------------------")
        print(f"The area is {Area}")
        area_calc_menu()
        option = int(input(option_prompt))
        
    elif option == 5:
        print("Goodbye")
    else:
        print("Invalid option.")
        print("------------------")
        
        area_calc_menu()
        option = int(input(option_prompt))

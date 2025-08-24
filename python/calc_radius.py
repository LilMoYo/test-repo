def calculate_circle_area(radius):
    radius_s = float(radius) ** 2
    area = 3.14 * radius_s
    return area

r = input ("enter radius: ")
a = calculate_circle_area(r)
print(a)
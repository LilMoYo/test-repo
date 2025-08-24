mass = float(input('What is your mass (in kg) '))
height = float(input('What is your height? (in m) '))

bmi = mass / (height ** 2)
print(bmi)
print('Your BMI is: ' + str(bmi))
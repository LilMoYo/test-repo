# Write code below 💖

earth_weight = float(input('What is your Earth weight? (kg): '))
planet = int(input('What is the planet number?(1 to 7): '))

if planet == 1:
    destination_weight = (earth_weight * 0.38)
    print('Mercury', destination_weight , 'kg')
elif planet == 2:
    destination_weight = (earth_weight * 0.91)
    print('Venus', destination_weight , 'kg')
elif planet == 3:
    destination_weight = (earth_weight * 0.38)
    print('Mars', destination_weight , 'kg')
elif planet == 4:
    destination_weight = (earth_weight * 2.53)
    print('Jupiter', destination_weight , 'kg')
elif planet == 5:
    destination_weight = (earth_weight * 1.07)
    print('Saturn', destination_weight , 'kg')
elif planet == 6:
    destination_weight = (earth_weight * 0.89)
    print('Uranus', destination_weight , 'kg')
elif planet == 7:
    destination_weight = (earth_weight * 1.14)
    print('Neptune', destination_weight , 'kg')
else:
    print('Invalid planet number')

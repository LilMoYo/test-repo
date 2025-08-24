moonph_input = input("Enter the phase of the moon: ")
def moon_phase(moon):
  if moon == "New Moon":
    print ("🌑")
  elif moon == "Waxing Crescent":
    print ("🌒")
  elif moon == "First Quarter":
    print("🌓")
  elif moon == "Waxing Gibbous":
    print("🌔")
  elif moon == "Full Moon":
    print("🌕")
  elif moon == "Waning Gibbous":
    print("🌖")
  elif moon == "Last Quarter":
    print("🌗")
  elif moon == "Waning Crescent":
    print("🌘")
  else:
    print("Invalid moon phase")
    moonph_input = input("Enter the phase of the moon: ")
    moon_phase(moonph_input)
    
moon_phase(moonph_input)
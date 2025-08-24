def get_item(option):
  if option == 1:
    print('🍔 Cheeseburger')
  elif option == 2: 
    print('🍟 Fries')
  elif option == 3: 
    print('🥤 Soda')
  elif option == 4: 
    print('🍦 Ice Cream')
  elif option == 5:
    print('🍪 Cookie')
  else: 
    print('Please back later, we don\'t have that!')

def welcome():
  print('Welcome to Duraztrue')
  print(
    '\nThis is our menu!',
    '\n🍔 Cheeseburger',
    '\n🍟 Fries',
    '\n🥤 Soda',
    '\n🍦 Ice Cream',
    '\n🍪 Cookie'
  )
  
welcome()
get_item_no = int(input('What would you like to order? '))
get_item = get_item(get_item_no)
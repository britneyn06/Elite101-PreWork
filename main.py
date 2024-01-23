#Mechanics (importing)
#import random
program_loop = True

#Inventory
order_inventory = [
  {'orderNumber_id': 147, 'burger': 1, 'burger_type': 'cheeseburger', 'fries': 1, 'drink': 1},
  {'orderNumber_id': 193, 'burger': 2, 'burger_type': 'deluxe', 'fries': 0, 'drink': 2},
  {'orderNumber_id': 121, 'burger': 1, 'burger_type': 'classic', 'fries': 2, 'drink': 1},
  {'orderNumber_id': 180, 'burger': 5, 'burger_type': 'signature', 'fries': 5, 'drink': 5},
]

# Welcome the user and ask for their name and order number
print('Welcome to Food Drive Customer Support!')
name = input('What is your name? ')
print('Hello, ' + name + '!')
orderNumber = input('What is your 3 digit order number? #')

#When user put an order number that is not 3 digits
while int(orderNumber) > 999 or int(orderNumber) < 100:
  orderNumber = int(input('Invalid order numner. Please enter a 3 digit order number: #'))

print('How can I help you today, ' + name + '?\n\nPlease choose a number from the following options:')

# Design Conversation Menu
def display_menu():
  print('\n---------------------------------------')
  print('1. I did not receive my order')
  print('2. I am missing a part of my order')
  print('3. I do not want my order anymore')
  print('4. End the Conversation')
  print('---------------------------------------')

def user_selection():
  in_use = True
  user_choice = int(input('Enter the number of your choice: '))

  if user_choice == 1:
    order_not_received()
  elif user_choice == 2:
    print('Placeholder 2')
  elif user_choice == 3:
    print('Placeholder 3')
  elif user_choice == 4:
    print('Goodbye, ' + name + '! Have a great day!')
    in_use = False
  else:
    print('\nSorry, that is not a valid choice. Please pick a number 1-4.')
  return in_use
      
#When user did not recieve their order
def order_not_received():
  print('\nSorry to hear that your order was not recieved yet.')
  print('Here is the current list of the orders on file:')
  for orderNumber in order_inventory:
    print('---------------------------------------')
    for key, value in orderNumber.items():
      print(f"{key}: {value}")
  print('---------------------------------------')

while program_loop:
  display_menu()
  program_loop =user_selection()
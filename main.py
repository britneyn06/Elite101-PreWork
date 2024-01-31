#Mechanics (importing)
#import random
program_loop = True

#Inventory
order_inventory = [
  {'orderNumber_id': 147, 'burger': 1, 'burger_type': 'cheeseburger', 'fries': 1, 'drink': 1,},
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
  print('3. I want to refund my order')
  print('4. I want to check the list of orders')
  print('5. End the Conversation')
  print('---------------------------------------')

def user_selection():
  in_use = True
  user_choice = int(input('Enter the number of your choice: '))

  if user_choice == 1:
    order_not_received()
  elif user_choice == 2:
    order_missing()
  elif user_choice == 3:
    refund()
  elif user_choice == 4:
    display_inventory()
  elif user_choice == 5:
    print('Goodbye, ' + name + '! Have a great day!')
    in_use = False
  else:
    print('\nSorry, that is not a valid choice. Please pick a number 1-5.')
  return in_use

#Displays the orders inventory
def display_inventory():
  print('\nHere is the current list of the orders on file:')
  for orderNumber in order_inventory:
    print('---------------------------------------')
    for key, value in orderNumber.items():
      print(f"{key}: {value}")
  print('---------------------------------------')
  
#When user did not recieve their order
def order_not_received():
  print('\nSorry to hear that your order was not recieved yet.')
  display_inventory()
  print('Would you like to refund your order?')
  refund_order = input('Enter yes or no: ')
  if refund_order == "yes":
    refund()
  else:
    print('Do you need any further assistance?')
    assistance = input('Enter yes or no: ')
    if assistance == "no" or assistance == "No":
      print('Goodbye, ' + name + '! To exit this conversation, please enter the number 5.')
    else:
      print('Please choose a number from the following options: ')

#When user is missing a part of their order
def order_missing():
  print('\n---------------------------------------')
  print('Sorry to hear that you are missing a part of your order.')
#PRINTS the current order inventory
  display_inventory()
  
  try: 
    ONUM = int(input('What is the order number of the item you are missing? #'))
  except ValueError:
    ONUM = 0
 
  for i, orderNumber in enumerate(order_inventory):
    if order_inventory[i]['orderNumber_id'] == ONUM:
      print('\nWhat item are you missing? Burger (1), fries (2), or drink(3)?')
      missing_item = int(input('Please enter the number of the corressponding item: '))
      if missing_item == 1:
        order_inventory[i]['burger'] = order_inventory[i]['burger'] + 1
        print('The item was added to your order.')

      elif missing_item == 2:
        order_inventory[i]['fries'] = order_inventory[i]['fries'] + 1
        print('The item was added to your order.')

      elif missing_item == 3:
        order_inventory[i]['drink'] = order_inventory[i]['drink'] + 1
        print('The item was added to your order.')
        
      else:
        print('Invalid item number. Please try again.')
      break
  else:
    print('Invalid order number. Please try again.')

#When the user wants to refun their order
def refund():
  display_inventory()
  print('Sorry to hear that you do not want your order anymore.')
  ONUM = int(input('What is your order number? #'))
  for i, orderNumber in enumerate(order_inventory):
    if order_inventory[i]['orderNumber_id'] == ONUM:
      print('\nYour order has been refunded.')
      order_inventory.pop(i)
      break
  else:
    print('Invalid order number. Please try again.')
  
  class Order:
    def __init__(self, burger, burger_type, fries, drink):
      self.orderNumber_id = ONUM
      self.burger = burger
      self.burger_type = burger_type
      self.fries = fries
      self.drink = drink

  
while program_loop:
  display_menu()
  program_loop =user_selection()
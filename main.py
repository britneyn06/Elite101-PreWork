# Welcome the user and ask for their name and order number
print('Welcome to Food Drive Customer Support!')
name = input('What is your name? ')
print('Hello, ' + name + '!')
orderNumber = input('What is your 3 digit order number? #')

# Design Conversation Menu
print('How can I help you today, ' + name + '?\n\nPlease choose a number from the following options:')
print('1. I did not receive my order')
print('2. I am missing a part of my order')
print('3. I do not want my order anymore')
print('4. End the Conversation')
user_choice = int(input('Enter the number of your choice: '))

# Design Conversation Menu Options

#When user puts an option that is not available
while user_choice > 4 or user_choice < 1:
  user_choice = int(input('Invalid choice. Please enter a number from 1 to 4: '))

#When user chooses an available option
if user_choice > 0 and user_choice < 5:
  if user_choice == 1:
    print('Placeholder 1')
  elif user_choice == 2:
    print('Placeholder 2')
  elif user_choice == 3:
    print('Placeholder 3')
  elif user_choice == 4:
    print('Goodbye, ' + name + '! Have a great day!')

#When user did not recieve their order
def order_not_received():
  
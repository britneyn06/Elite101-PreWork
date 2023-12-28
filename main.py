# Welcome the user and ask for their name and age
print('Welcome to the Elite 101 Chatbot!')
name = input('What is your name? ')
print('Hello, ' + name + '!')
age = input('How old are you? ')

# Design Conversation Menu
print('How can I help you today, ' + name + '?\n\nPlease choose a number from the following options:')
print('1. Placeholder 1')
print('2. placeholder 2')
print('3. Placeholder 3')
print('4. End the Conversation')
user_choice = int(input('Enter the number of your choice: '))

# Design Conversation Menu Options

#When user puts an option that is not available
while user_choice > 4:
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
import os
import pyfiglet
import termcolor2
os.system('cls')
###################################################


def term_pyf_green(x):
    print((termcolor2.colored(pyfiglet.figlet_format(x), 'green')))


def term_pyf_red(x):
    print((termcolor2.colored(pyfiglet.figlet_format(x), 'red')))


def term_pyf_blue(x):
    print((termcolor2.colored(pyfiglet.figlet_format(x), 'blue')))


def term_pyf_cyan(x):
    print((termcolor2.colored(pyfiglet.figlet_format(x), 'cyan')))


def term_pyf_yellow(x):
    print((termcolor2.colored(pyfiglet.figlet_format(x), 'yellow')))


###################################################
def term_green(x):
    print(termcolor2.colored(x, 'green'))


def term_blue(x):
    print(termcolor2.colored(x, 'blue'))


def term_red(x):
    print(termcolor2.colored(x, 'red'))


def term_cyan(x):
    print(termcolor2.colored(x, 'cyan'))


def term_yellow(x):
    print(termcolor2.colored(x, 'yellow'))


###################################################


print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")
print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")
print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")

term_pyf_red('Welcome To Your Restaurant')

print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")
print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")
print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥 \n")


#################################################################


quantity=0
while True:
    choice1=0
    choice2=0
    choice3=0
    costumer=0
    term_red(' tab: \n\n 1:drinks \n\n 2:fastfood \n\n 3:salad \n\n 4:exit')
    costumer = input('Enter your menu tab for serving: ')
    if costumer == '1' or costumer == 'drinks':
        while True:
        
            term_pyf_cyan('Drinks')
            term_cyan(
                ' 1:water \n\n 2:soda \n\n 3:limoonad \n\n 4:apple juice \n\n 5:back')
            choice1 = input('Enter your drinks: ')
            if choice1 == '1' or choice1 == 'water':
                print('each one is 1 $')
                number1_choice1 = int(input('enter number of order: '))
                quantity+=number1_choice1
                term_cyan(f"money that you have to pay: {number1_choice1} $")

            elif choice1 == '2' or choice1 == 'soda':
                print('each one is 2 $')
                number2_choice1 = 2 * int(input('enter number of order: '))
                quantity+=number2_choice1
                term_cyan(f"money that you have to pay: {number2_choice1} $")

            elif choice1 == '3' or choice1 == 'limoonad':
                print('each one is 2 $')
                number3_choice1 = 2 * int(input('enter your number of order: '))
                quantity+=number3_choice1
                term_cyan(f"money that you have to pay: {number3_choice1} $")

            elif choice1 == '4' or choice1 == 'apple juice':
                term_cyan('each one is 4 $')
                number4_choice1 = 4 * int(input('enter number of order: '))
                quantity+=number4_choice1
                term_cyan(f"money that you have to pay: {number4_choice1} $")
            elif choice1 == '5' or choice1 == 'back':
                break 
        if choice1 == '5' or choice1 == 'back':
            continue     
                   
#################################################################################################
    if costumer == '2' or costumer == 'sanwiches':  
    
        while True:
        
            term_pyf_yellow('Fast Food')
            term_yellow(' 1:pizza \n\n 2:hotdog \n\n 3:hamburger \n\n 4:pasta \n\n 5:back')
            choice2 = input('Enter your food: ')
            if choice2 == '1' or choice2 == 'pizza':
                print('each one is 5 $')
                number1_choice2 = 5 * int(input('enter your number of order: '))
                quantity+=number1_choice2
                term_yellow(f"money that you have to pay: {number1_choice2} $")

            elif choice2 == '2' or choice2 == 'hotdog':
                print('each one is 3 $')
                number2_choice2 = 3 * int(input('enter your number of order: '))
                quantity+=number2_choice2
                term_yellow(f"money that you have to pay: {number2_choice2} $")

            elif choice2 == '3' or choice2 == 'hamburger':
                print('each one is 5 $')
                number3_choice2 = 5 * int(input('ente{r your number of order: '))
                quantity+=number3_choice2
                term_yellow(f"money that you have to pay: {number3_choice2} $")

            elif choice2 == '3' or choice2 == 'pasta':
                print('each one is 7 $')
                number4_choice2 = 7 * int(input('enter your number of order: '))
                quantity+=number4_choice2
                term_yellow(f"money that you have to pay: {number4_choice2} $")
            elif choice2 == '5' or choice2 == 'back':
                break
    if choice2 == '5' or choice2 == 'back':
        continue            

############################################################################
    if costumer == '3' or costumer == 'salad':
        while True:
        
            term_pyf_green('salad')
            term_green(' 1:sezar \n\n 2:alferedo \n\n 3:simple \n\n 4:back')
            choice3 = input('Enter your salad: ')
            if choice3 == '1' or choice3 == 'sezar':
                print('each one is 4 $')
                number1_choice3 = 4*int(input('enter your number of order: '))
                quantity+=number1_choice3
                term_green(f"money that you have to pay: {number1_choice3} $")

            elif choice3 == '2' or choice3 == 'alferedo':
                print('each one is 6 $')
                number2_choice3 = 6*int(input('enter your number of order: '))
                quantity+=number2_choice3
                term_green(f"money that you have to pay: {number2_choice3} $")

            elif choice3 == '3' or choice3 == 'simple':
                print('each one is 3 $')
                number3_choice3 = 3*int(input('enter your number of order: '))
                quantity+=number3_choice3
                term_green(f"money that you have to pay: {number3_choice3} $")
            elif choice3 == '4' or choice3 == 'back':
                break
    if choice3 == '4' or choice3 == 'back':
        continue            
############################################################################
    if costumer == '4' or costumer == 'exit':
        break

term_yellow(f'Your final factor: {quantity} $')
term_yellow("Have good time")

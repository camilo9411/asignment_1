from os import system, name

#Funtion main
def main():
    myList = []
    choise = ' '
    while (choise != 'Q'):
        system('cls')
        print('\t-----MENU----')
        print('P - Print numbers')
        print('A - Add a number')
        print('M - Display mean of the numbers') 
        print('S - Display the smallest number')
        print('L - Display the largest number')
        print('F - Search for a number in the list')
        print('Q - Quit')
        choise = input('Enter your Choice: ')
        choise = choise.upper()
        if choise == 'P':
            system('cls')
            if not myList:
                print('[] - the list is empty')
            else:
                print(myList)
            input('Press any key to continue...')
        elif choise == 'A':
                while True:
                    system('cls')
                    print('\t----ADDING----')
                    num = input('Enter a integer to add in the list: ')
                    try:
                        num = int(num)
                        break
                    except ValueError:
                        print('Not valid input...Try again')
                        input('Press any key to continue...')

                myList.append(int(num))
                print('Number {0} has been added.'.format(num))
                input('Press any key to continue...')


        elif choise == 'M':
            system('cls')
            print('\t----MEAN OF THE LIST----')
            if myList:
                mean_list = sum(myList) / len(myList)
                print('The mean is '+ str(round(mean_list, 2)))
                input('Press any key to continue...')
            else:
                print('Unable to calculate the mean - no data')
                input('Press any key to continue...')
        elif choise == 'S':
            system('cls')
            print('\t----SMALLEST NUMBER----')
            if myList:
                print('The smallest number is', min(myList))
                input('Press any key to continue...')  
            else:
                print('Unable to determine the smallest number - list is empty')
                input('Press any key to continue...')

        elif choise == 'L':
            system('cls')
            print('\t----LARGEST NUMBER----')
            if myList:
                print('The largest number is', max(myList))
                input('Press any key to continue...')  
            else:
                print('Unable to determine the largest number - list is empty')
                input('Press any key to continue...')
        elif choise == 'F':           
            while True:
                system('cls')
                print('\t----FIND A NUMBER----')
                num_to_find = input('Enter the number you want to find: ')
                try:
                    num_to_find = int(num_to_find)
                    break
                except ValueError:
                    print('Not valid input...Try again')
                    input('Press any key to continue...')
            if int(num_to_find) in myList:
                frecuency = 0
                for item in myList:
                    if item == int(num_to_find):
                        frecuency = frecuency + 1
                print('The number ' + str(num_to_find) + ' is in the list '
                    + str(frecuency) + ' times.')
                input('Press any key to continue...')
            else:
                print('The number ' + str(num_to_find) +' is not in the list')
                input('Press any key to continue...')
        elif choise == 'Q':
            system('cls')
            print('Thank you for using this program!')
            input('Press any key to continue...')
        else:
            system('cls')
            print('Unknown selection, please try again\n')
            input('Press any key to continue...')

#call main()...
main()



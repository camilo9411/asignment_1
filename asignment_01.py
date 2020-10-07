from os import system, name

#Funtion main
def main():
    myList = []
    choise = ' '
    while (choise != 'Q'):
        print('\t-----MENU----')
        print('P - Print numbers')
        print('A - Add a number')
        print('M - Display mean of the numbers')
        print('S - Display the smallest number')
        print('L - Display the largest number')
        print('F - Search for a number in the list')
        print('Q - Quit')
        choise = input('Enter your Choice: ').upper()

        if choise == 'P':
            print('\t----DISPLAY----')
            if not myList:
                print('[] - the list is empty')
            else:
                print(str(myList).replace(",", ""))
        elif choise == 'A':
            print('\t----ADDING----')
            while True:
                num = input('Enter a integer to add in the list: ')
                try:
                    num = int(num)
                    break
                except ValueError:
                    print('Not valid input...Try again')
            myList.append(int(num))
            print('Number {0} added.'.format(num))
        elif choise == 'M':
            print('\t----MEAN OF THE LIST----')
            if myList:
                mean_list = sum(myList) / len(myList)
                print('The mean is '+ str(round(mean_list, 2)))
            else:
                print('Unable to calculate the mean - no data')
        elif choise == 'S':
            print('\t----SMALLEST NUMBER----')
            if myList:
                print('The smallest number is', min(myList))
            else:
                print('Unable to determine the smallest number - list is empty')
        elif choise == 'L':
            print('\t----LARGEST NUMBER----')
            if myList:
                print('The largest number is', max(myList))
            else:
                print('Unable to determine the largest number - list is empty')
        elif choise == 'F':
            while True:
                print('\t----FIND A NUMBER----')
                num_to_find = input('Enter the number you want to find: ')
                try:
                    num_to_find = int(num_to_find)
                    break
                except ValueError:
                    print('Not valid input...Try again')
            if int(num_to_find) in myList:
                print('The number ' + str(num_to_find) + ' is in the list ' + str(myList.count(num_to_find)) + ' times.')
            else:
                print('The number ' + str(num_to_find) +' is not in the list')
        elif choise == 'Q':
            print('Goodbye')
            break
        else:
            print('Unknown selection, please try again')
        input('Press any key to continue...')

#call main()...
main()

print('Enter 0 to 5 for the following options:')
print('0 -> Issue new ticket number.')
print('1 -> Assign first ticket in queue to counter 1.')
print('2 -> Assign first ticket in queue to counter 2.')
print('1 -> Assign first ticket in queue to counter 3.')
print('4 -> Assign first ticket in queue to counter 4.')
print('5 -> Quit program.')
index, second, third, fourth = ['Not assigned,', 'Not assigned,','Not assigned,','Not assigned']
queue = []
ticket = 1000
while True:
    print('Tickets in queue:', queue)
    print("Counter assignment: {'Counter 1':", index, "'Counter 2':", second, "'Counter 3':", third, "'Counter 4':", fourth, '}')
    try:
        userInput = int(input('Enter your option:'))
        ticket += 1
        print('\n')
    except ValueError:
        print('You have not entered a valid number. Please try again.')
        print('\n')
        continue
    if userInput == 0:
        queue.append(ticket)
    elif userInput == 5:
        print('Quitting program...')
        break
    elif userInput >= 6:
        print('Invalid option, try again...')
        ticket -= 1
    elif queue == []:
        print('There are no tickets in the queue. Please add a new ticket.')
        ticket -= 1
    elif userInput == 1:
        index = queue[0]
        queue.pop(0)
        ticket -= 1
    elif userInput == 2:
        second = queue[0]
        queue.pop(0)
        ticket -= 1
    elif userInput == 3:
        third = queue[0]
        queue.pop(0)
        ticket -= 1
    elif userInput == 4:
        fourth = queue[0]
        queue.pop(0)
        ticket -= 1
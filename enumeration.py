goal = int(input('Write a number: '))
answer = 0

while answer**2 < goal:
    answer += 1

if answer**2 == goal:
    print(f'The square root of {goal} is {answer}')
else:
    print(f'{goal} doesn`t have an exact square root')
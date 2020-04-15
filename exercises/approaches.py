goal = int(input('Write a number: '))
epsilon = 0.0001
step = epsilon**2
answer = 0.0


while abs(answer**2 - goal) >= epsilon and answer <= goal:
    answer += step

if abs(answer**2 - goal) >= epsilon:
    print(f'The square root of {goal} was not found')
else:
    print(f'The square root of {goal} is {answer}')
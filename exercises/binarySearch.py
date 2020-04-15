goal = int(input('Write a number: '))
epsilon = 0.01
low = 0.0
high = max(1.0, goal)
answer = (high + low) / 2

while abs(answer**2 - goal) >= epsilon:
    if answer**2 < goal:
        low = answer
    else:
        high = answer
    
    answer = (high + low) / 2

print(f'The square root of {goal} is {answer}')
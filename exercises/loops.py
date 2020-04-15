counter_outside = 0
counter_inside = 0

while counter_outside < 5:
    while counter_inside < 6:
        print(counter_outside, counter_inside)
        counter_inside += 1

    counter_outside += 1
    counter_inside = 0

fruits = ['apple', 'grapefruit', 'pear', 'watermelon']

for f in fruits:
    print(f)
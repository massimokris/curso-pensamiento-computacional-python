my_str = 'Platzi'

print(my_str)

## length
len_my_str = len(my_str)
print(len_my_str)

## print the first element
print(my_str[0])

## slicing string

## starts on 2 to the end
print(my_str[2:])

## from the start to the third position
print(my_str[:3])

## from the start to the last two characters 
print(my_str[:-2])

## from the start to the end jumping two by two
print(my_str[::2])

## concat
f'I love {my_str}'
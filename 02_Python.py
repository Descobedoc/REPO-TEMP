
# Dificultad extra

def fizzbuzz():
    first_string = input("Introduce la primera palabra: ")
    second_string = input("Introduce la segunda palabra: ") 
    number = 0
    for index in range(1, 101):
        if index % 3 == 0 and index % 5 == 0:
            print(first_string + second_string)
        elif index % 3 == 0:
            print(first_string)
        elif index % 5 == 0:
            print(second_string)
        else:
            print(index)
            number = number + 1
    print(number)

fizzbuzz()
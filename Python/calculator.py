#A simple calculator

def sum_of_numbers(list_of_numbers):
    k = 0
    for i in range(len(list_of_numbers)):
        k = k + list_of_numbers[i]
    return k

def sum_of_even(list_of_numbers):
    k = 0
    for i in range(len(list_of_numbers)):
        if list_of_numbers[i]%2 == 0:
            k = k + list_of_numbers[i]
    return k

def sum_of_two(first_number, second_number):
    return first_number + second_number

def product_of_numbers(list_of_numbers):
    k = 1
    for i in range(len(list_of_numbers)):
            k = k * list_of_numbers[i]
    return k

def main():
    numbers = [5,7,8,11,15,13]
    print('Sum of numbers:',sum_of_numbers(numbers))
    print('Sum of even numbers in list:',sum_of_even(numbers))
    print('Sum of first two numbers:', sum_of_two(numbers[0],numbers[1]))
    print('Product of numbers in list:',product_of_numbers(numbers))

    #example of functions being really useful
    group1 = [6,8,24,11,2,3]
    group2 = [3,2,9,14,11,12]
    group3 = [13,14,17,19,4]

    big_group = [group1, group2, group3]
    for group in big_group:
        print('-----')
        print('For numbers:',group)
        print('Sum of numbers:',sum_of_numbers(group))
        print('Sum of even numbers in list:',sum_of_even(group))
        print('Product of numbers in list:',product_of_numbers(group))

main()

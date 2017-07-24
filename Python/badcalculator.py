#A program that calculates the same without functions
def main():
    numbers = [5,7,8,11,15,13]
    k = 0
    for i in range(len(numbers)):
        k = k + numbers[i]
    print('Sum of numbers:',k)
    f = 0
    for i in range(len(numbers)):
        if numbers[i]%2 == 0:
            f = f + numbers[i]
    print('Sum of even numbers in list:',f)
    g = 1
    for i in range(len(numbers)):
            g = g * numbers[i]
    print('Product of numbers',g)
    group1 = [6,8,24,11,2,3]
    group2 = [3,2,9,14,11,12]
    group3 = [13,14,17,19,4]
    print('-----')
    print('For numbers:',group1)
    k = 0
    for i in range(len(group1)):
        k = k + group1[i]
    print('Sum of numbers:',k)
    f = 0
    for i in range(len(group1)):
        if group1[i]%2 == 0:
            f = f + group1[i]
    print('Sum of even numbers in list:',f)
    g = 1
    for i in range(len(group1)):
            g = g * group1[i]
    print('Product of numbers',g)
    print('-----')
    print('For numbers:',group2)
    k = 0
    for i in range(len(group2)):
        k = k + group2[i]
    print('Sum of numbers:',k)
    f = 0
    for i in range(len(group2)):
        if group2[i]%2 == 0:
            f = f + group2[i]
    print('Sum of even numbers in list:',f)
    g = 1
    for i in range(len(group2)):
            g = g * group2[i]
    print('Product of numbers',g)
    print('-----')
    print('For numbers:',group3)
    k = 0
    for i in range(len(group3)):
        k = k + group3[i]
    print('Sum of numbers:',k)
    f = 0
    for i in range(len(group3)):
        if group3[i]%2 == 0:
            f = f + group3[i]
    print('Sum of even numbers in list:',f)
    g = 1
    for i in range(len(group3)):
            g = g * group3[i]
    print('Product of numbers',g)

main()

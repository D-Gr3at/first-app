if __name__ == '__main__':
    # Indentation
    first_value = 20
    second_value = 5
    print(f'The sum = {first_value + second_value}')

    first_value = 3.5
    second_value = 5
    print(f'The product = {first_value * second_value}')

    first_value = 20
    second_value = 5
    print(f'The division = {first_value / second_value}')

    first_value = 20
    second_value = 5
    print(f'The subtraction = {first_value - second_value}')

    initial_principal = 700
    rate = 1.5  # per annum
    n = 1
    t = 5
    #precedence of operation - operators
    final_amount = initial_principal * (1 + rate/n) ** (n*t)

    print(f'The final amount = {final_amount}')

    my_bool = False

    if my_bool:
        print('Hey!!')
    else:
        print("sorry, we're not available")

    number = 10

    if 20 > number > 10:
        print('Less "than" 20!')

    #others: >, !=, and, or



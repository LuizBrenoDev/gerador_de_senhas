import initial_population


def generate():
    chars = int(input('Insert the number of characters of the password: '))
    nums = input('Insert the quantity of numbers needed: ')
    symbols = input('Insert the quantity of symbols needed: ')
    initial_population.population(chars)


def generate_for_test():
    chars = int(input('Insert the number of characters of the password: '))
    nums = input('Insert the quantity of numbers needed: ')
    symbols = input('Insert the quantity of symbols needed: ')
    initial_population.population_for_test(chars)


def flush_registers():
    with open('files/codes.txt', 'w') as file:
        file.flush()
        file.close()

    with open('files/values.txt', 'w') as file:
        file.flush()
        file.close()


print('Welcome to password generator 0.0.0 main file')
print('Please, insert the keyword for an command:')
print('''
1 - Generate new password
2 - Generate new password for test
3 - Flush Registers
4 - Convert Genes to password
5 - Convert password to Gene
0 - Exit Application
''')
keyword = int(input('> '))

match keyword:
    case 1:
        generate()
    case 2:
        generate_for_test()
    case 3:
        flush_registers()
    case 0:
        print('Exiting...')

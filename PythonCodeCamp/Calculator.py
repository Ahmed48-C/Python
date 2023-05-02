import operator
import inquirer

ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,  # use operator.div for Python 2
    '%' : operator.mod,
    '^' : operator.pow,
}

def calculator():

    while True:
        try:
            num1 = int(input("Enter a number: "))

            num2 = int(input("Enter a second number: "))
            break
        except ValueError:

            print('Invalid Input. Only integers accepted.')
    
    # operations = ['+', '-', '*', '/', '%', '^']
    operations = list(ops.keys())

    questions = [
    inquirer.List('operations',
                  message="Choose an operation",
                  choices=operations,
                  ),
    ]
    operation = inquirer.prompt(questions)

    user_input = operation['operations']

    # user_input = ''

    # input_message = "Pick an operation:\n"

    # for index, item in enumerate(operations):
    #     input_message += f'{index+1}) {item}\n'

    # input_message += 'Your operation: '

    # while user_input.lower() not in operations:
    #     user_input = input(input_message)

    result = ops[user_input](num1, num2)
    print("The result is", result)
    
calculator()
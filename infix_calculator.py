def precedence(op):

    '''
    Function to find precedence of operators.
    '''

    if op == '+' or op == '-':
        return 1
    if op == '*' or op == '/':
        return 2
    return 0

def apply_op(a, b, op):

    '''Function to perform arithmetic operations.'''

    if op == '+': return a + b
    if op == '-': return a - b
    if op == '*': return a * b
    if op == '/': return a / b

def evaluate(tokens):

    '''
    Function that implements infix calculator,
    where tokens are separated by space.
    Time complexity: O(N)
    Space complexity: O(N)
    '''

    # stack to store integer values.
    values = []

    # stack to store operators.
    ops = []
    i = 0

    while i < len(tokens):

        # Space delimited
        if tokens[i] == ' ':
            i += 1
            continue

        # push opening brace to 'ops'
        elif tokens[i] == '(':
            ops.append(tokens[i])

        # push number to stack for numbers.
        elif tokens[i].isdigit():
            val = 0

            while (i < len(tokens) and
                   tokens[i].isdigit()):
                val = (val * 10) + int(tokens[i])
                i += 1

            values.append(val)

            i -= 1

        # Closing brace encountered,
        # solve entire brace.
        elif tokens[i] == ')':

            while len(ops) != 0 and ops[-1] != '(':
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(apply_op(val1, val2, op))

            # pop opening brace.
            ops.pop()

        # Current token is an operator.
        else:

            while (len(ops) != 0 and
                   precedence(ops[-1]) >=
                   precedence(tokens[i])):
                val2 = values.pop()
                val1 = values.pop()
                op = ops.pop()

                values.append(apply_op(val1, val2, op))

            # Push current token to 'ops'.
            ops.append(tokens[i])

        i += 1

    # Entire expression has been parsed
    # at this point, apply remaining ops
    # to remaining values.
    while len(ops) != 0:
        val2 = values.pop()
        val1 = values.pop()
        op = ops.pop()

        values.append(apply_op(val1, val2, op))

    # Top of 'values' contains result,
    # return it.
    return values[-1]



if __name__ == "__main__":

    print(f'Function that implements infix calculator')
    print(f'Time Complexity: O(N)')
    print(f'Space Complexity: O(N)')
    print(f'Some test cases:')
    input = '( 1 + 2 )'
    print(f'input: {input}  output: {evaluate(input)}')
    input = '( 1 + ( 2 * 3 ) )'
    print(f'input: {input}  output: {evaluate(input)}')
    input = '( ( 1 * 2 ) + 3 )'
    print(f'input: {input}  output: {evaluate(input)}')
    input = '( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )'
    print(f'input: {input}  output: {evaluate(input)}')


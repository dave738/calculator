from collections import deque

def parse(tokens):

  '''
  Function that implements infix calculator,
  where tokens are separated by space.
  Time complexity: O(N)
  Space complexity: O(N)
  '''

  token=tokens.popleft()
  if token=='+':
    return parse(tokens)+parse(tokens)
  elif token=='-':
    return parse(tokens)-parse(tokens)
  elif token=='*':
    return parse(tokens)*parse(tokens)
  elif token=='/':
    return parse(tokens)/parse(tokens)
  else:
    # number
    return int(token)



if __name__ == "__main__":

  print(f'Function that implements prefix calculator (using recursion)')
  print(f'Time Complexity: O(N)')
  print(f'Space Complexity: O(N)')
  print(f'Some test cases:')
  input = '3'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '+ 1 2'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '+ 1 * 2 3'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '+ * 1 2 3'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '- / 10 + 1 1 * 1 2'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '- 0 3'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
  input = '/ 3 2'
  print(f'input: {input}  output: {parse(deque(input.split()))}')
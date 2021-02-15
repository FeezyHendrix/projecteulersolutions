def create_fibonacci_sequence(n):
  sequence = [1,2]

  while sequence[-1] < n:
    sequence.append(sequence[-1] + sequence[-2])
  
  return sequence

def calculatesum(n):
  sequence = create_fibonacci_sequence(n)
  sequence = [x for x in sequence if x % 2 == 0]
  return sum(sequence)


print(calculatesum(4000000))


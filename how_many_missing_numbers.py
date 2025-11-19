def howManyMissing(numbers: list) -> int:
  try:
    numbers = list(map(int,numbers))
  except ValueError as e:
    print(f'An error occured during execution: {e}')
    return None

  return len([missing for missing in range(int(numbers[0]),int(numbers[-1])) if missing not in numbers])
print(howManyMissing([1,4,'f']))
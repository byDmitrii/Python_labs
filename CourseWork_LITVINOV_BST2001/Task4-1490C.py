

for _ in range(int(input())):
  a = {i ** 3 for i in range(1, 10001)}
  number = int(input())
  for n in a:
    if number - n in a:
      print("\nYES")
      break
  else:
    print("\nNO")



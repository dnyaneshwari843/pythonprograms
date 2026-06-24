arr = [7,9,67,90]   # Store the number in an array

for num in arr:
 count = 0
 if num<2:
    print("num is not proime number")
 else:

  for i in range(1,num+1):
    if num % i == 0:
        count += 1

  if count == 2:
    print(num, "is a Prime Number")
  else:
    print(num, "is Not a Prime Number")


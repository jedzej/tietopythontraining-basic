# cupcake costs a.b how much n cupcakes cost?

dollars = int(input())
pennies = int(input())
count = int(input())

print(str(count * dollars + int(count * pennies / 100)) + " " +
      str(count * pennies % 100))

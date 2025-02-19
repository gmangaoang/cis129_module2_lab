muffin = input('How many muffins would you like?')
coffee = input('How many cups of coffee would you like?')

muffinPrice = 4 * int(muffin)
coffeePrice = 5 * int(coffee)
total = muffinPrice + coffeePrice
tax = total * .06
print('\nMy Coffee and Muffin Shop Receipt'
     '\n',str(muffin), 'muffins at $4 each: $',str(muffinPrice),
     '\n',str(coffee), 'coffee at $5 per cup: $',str(coffeePrice),
      '\n 6% tax: $', str(tax),
      '\n------',
      '\nTotal: $', str(tax + total)
     )

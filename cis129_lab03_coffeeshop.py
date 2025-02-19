muffin = input('How many muffins would you like?')
coffee = input('How many cups of coffee would you like?')
cupcake = input('How much cupckaes would you like?')
tea = input('How many cuops of coffee would you like?')

muffinPrice = 4 * int(muffin)
coffeePrice = 5 * int(coffee)
teaPrice = 3 * int(tea)
cupcakePrice = 3 * int(cupcake)
total = muffinPrice + coffeePrice + cupcakePrice + teaPrice
tax = total * .06
print('\nMy Coffee and Muffin Shop Receipt'
     '\n',str(muffin), 'muffins at $4 each: $',str(muffinPrice),
     '\n',str(coffee), 'coffee at $5 per cup: $',str(coffeePrice),
     '\n',str(cupcake), 'cupcake at $3 per cup: $',str(cupcakePrice),
      '\n',str(tea), 'tea at $3 per cup: $',str(teaPrice),
      '\n 6% tax: $', str(tax),
      '\n------',
      '\nTotal: $', str(tax + total)
     )

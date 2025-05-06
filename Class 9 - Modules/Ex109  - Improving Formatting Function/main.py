import currency

price = float(input('Type a price: '))
tax = int(input('Type the tax: '))

print(f'The original price is {currency.currency(price)} and the half price is '
      f'{currency.currency(currency.half(price))}')
print(f'The original price is {currency.currency(price)} and the increased price with tax is '
      f'{(currency.increase(price,tax,True))}')

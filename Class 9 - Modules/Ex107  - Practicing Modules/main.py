import currency

price = float(input('Type a price: '))
tax = int(input('Type the tax: '))
print(f'The original price is ${price} and the half price is ${currency.half(price)}')
print(f'The original price is ${price} and the increased price with tax is ${currency.increase(price, tax)}')


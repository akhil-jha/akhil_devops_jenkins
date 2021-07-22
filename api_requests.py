from forex_python.converter import CurrencyRates
import datetime

c = CurrencyRates()

dt = datetime.datetime(2020, 3, 27, 11, 21, 13, 114505)

print(c.get_rate('USD', 'INR', dt))

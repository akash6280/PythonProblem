
import pandas as pd
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Addition")
print(ds)
print("Subtraction")
ds = ds1 - ds2
print(ds)
print("Multiplication")
ds = ds1 * ds2
print(ds)
print("Division")
ds = ds1 / ds2
print(ds)
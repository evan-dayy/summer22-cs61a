import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)

# ----- Series
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)


import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

print(myvar["y"])

# ---- Dict to Series

import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories, index = ["day1", "day2"])

print(myvar)


# ------
import pandas as pd

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)

print(df.loc[0])
print(df.loc[range(2)])


# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string())  -- print entire table

# ------- Data analysis
print(df.info())


import pandas as pd

df = pd.read_csv('data.csv')

new_df = df.dropna() # df.dropna(inplace = True) to replace the original one

print(new_df.to_string())


import pandas as pd

df = pd.read_csv('data.csv')

df.fillna(130, inplace = True)

import pandas as pd

df = pd.read_csv('data.csv')

df["Calories"].fillna(130, inplace = True) # only on that column

df.dropna(subset=['Date'], inplace = True) # drop the entire row with a NaT in one column


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data.csv')

df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')

plt.show()

df["Duration"].plot(kind = 'hist')







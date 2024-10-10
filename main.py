import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Basket': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
    'Apples': [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36, 39, 42, 45, 48],
    'Bananas': [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32],
    'Oranges': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
}

df = pd.DataFrame(data)

sum_apples = df['Apples'].sum()
sum_bananas = df['Bananas'].sum()
sum_oranges = df['Oranges'].sum()

x = ['Apples', 'Bananas', 'Oranges']

y = [sum_apples, sum_bananas, sum_oranges]

plt.bar(x, y, color=['green', 'blue', 'Orange'])

plt.title('Comparison of total Apples and Bananas and Oranges')

plt.show()

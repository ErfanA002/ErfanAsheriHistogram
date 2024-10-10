import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Basket': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'],
    'Apples': [10, 20, 30, 56, 40, 40, 67, 47, 40, 4, 49, 52, 5, 56, 35, 45],
    'Bananas': [15, 6, 3, 45, 67, 44, 45, 11, 14, 18, 13, 12, 1, 34, 12, 12],
    'Oranges': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160]
}

df = pd.DataFrame(data)

sum_apples = df['Apples'].sum()
sum_bananas = df['Bananas'].sum()
sum_oranges = df['Oranges'].sum()

x = ['Apples', 'Bananas', 'Oranges']

h = [sum_apples, sum_bananas, sum_oranges]

plt.bar(x, h, color=['green', 'blue', 'Orange'])

plt.title('Comparison of total Apples and Bananas')

plt.show()

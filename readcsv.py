import pandas as pd

df = pd.read_csv('output_results.csv')
name = df['Title'].tolist()
price = df['Price'].tolist()
image = df['Image URL'].tolist()
link = df['Affiliate URL'].tolist()

for x in range(len(name)):
    print(name[x] + "   " + price[x] + "   " + image[x] + "   " + link[x] + "\n")

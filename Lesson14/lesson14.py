import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('avgIQpercountry.csv')


avg_iq_continent = df.groupby('Continent')['Average IQ'].mean()

plt.figure(figsize=(10,8))


avg_iq_continent.plot(kind='line', marker='o', color='skyblue')

plt.title('Average IQ per Continent')
plt.xlabel('Continent')
plt.ylabel('Average IQ')

plt.grid(axis='both', linestyle='--', alpha='0.7')

plt.show()

# filtered_df = df[df['Average IQ'] >= 100]
#
# filtered_df = filtered_df.sort_values(by="Average IQ", ascending=False)
#
# print(filtered_df)
#
#
# plt.figure(figsize=(14,8))
#
# bars = plt.bar(filtered_df['Country'], filtered_df['Average IQ'], color="skyblue")
#
# plt.title("Average IQ by Country (IQ >= 100)", fontsize=16)
#
# plt.xlabel('Country', fontsize=14)
# plt.ylabel('Average IQ', fontsize=14)
#
# plt.xticks(rotation=90, fontsize=10)
# plt.yticks(fontsize=10)
#
# plt.grid(axis='y', linestyle='--', alpha=0.8)
#
# plt.bar_label(bars, fmt='%.2f', fontzise=10, color='black')
#
# plt.tight_layout()
#
# plt.show()


import pandas as pd

data = {
    "Name": ["Nikhil", "Ravi", "Aman"],
    "Marks": [80, 70, 90]
}

df = pd.DataFrame(data)

print(df)
print("\nAverage Marks:", df["Marks"].mean())
print("Highest Marks:", df["Marks"].max())
print("Lowest Marks:", df["Marks"].min())
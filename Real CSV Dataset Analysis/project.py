import pandas as pd

df = pd.read_csv("students.csv")


print(df.shape)
# print(df["Marks"].mean())
# print(df[df["City"] == "Delhi"])
# print("Name:", df.loc[df["Marks"].idxmax(), "Name"])
# print(df.sort_values("Marks", ascending=False).head(1))

# top_students = df[df["Marks"] >= 80]

# top_students = top_students.sort_values(by="Marks", ascending=False)

# print(top_students)
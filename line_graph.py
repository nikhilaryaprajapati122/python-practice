import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
hours = [2, 3, 5, 4, 6]

plt.plot(days, hours)

plt.title("Study Hours Per Day")
plt.xlabel("Days")
plt.ylabel("Hours")

plt.show()
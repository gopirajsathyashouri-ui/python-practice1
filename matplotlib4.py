import matplotlib.pyplot as plt

cities = ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Kolkata"]
complaints = [120, 340, 290, 150, 95]

# Sort smallest to largest (barh draws the first item at the bottom)
pairs = list(zip(cities, complaints))
sorted_pairs = sorted(pairs, key=lambda p: p[1])
cities_sorted = [p[0] for p in sorted_pairs]
complaints_sorted = [p[1] for p in sorted_pairs]

# Color: above 200 is crimson, the rest steelblue
colors = ['crimson' if c > 200 else 'steelblue' for c in complaints_sorted]

bars = plt.barh(cities_sorted, complaints_sorted, color=colors, edgecolor='black')

plt.title("Complaints by City (Highest First)")
plt.xlabel("Number of Complaints")
plt.ylabel("City")

# Values at the end of each bar
plt.bar_label(bars, padding=3)

# Light vertical gridlines only, behind the bars
plt.grid(axis='x', alpha=0.3)
plt.gca().set_axisbelow(True)

# Bonus: dashed line at the average
avg = sum(complaints) / len(complaints)
plt.axvline(avg, color='black', linestyle='--', label=f'Average: {avg:.0f}')
plt.legend()

plt.show()

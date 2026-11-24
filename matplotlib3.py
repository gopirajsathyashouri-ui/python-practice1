import matplotlib.pyplot as plt 

cities = ["Hyderabad", "Mumbai", "Delhi", "Chennai", "Kolkata"]
complaints = [120, 340, 290, 150, 95]

colors = ['darkred' if c== max(complaints) else 'salmon' for c in complaints]
bars = plt.bar(cities, complaints, color=colors, edgecolor='black')

plt.title("Network Complaints by City") 
plt.xlabel("City")
plt.ylabel("Number of Complaints")

plt.bar_label(bars)

plt.grid(axis= 'y', alpha=0.3)
plt.gca().set_axisbelow(True)

plt.show()
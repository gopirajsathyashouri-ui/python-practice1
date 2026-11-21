prices = [120, 45, 300, 80, 510]
discounted = [round(p * 0.9, 2) for p in prices if p > 100]
print(discounted)
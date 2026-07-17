#Determine Temperature Status Based on City Weather

temp = float(input())
if temp > 0 :
    print("The temperature is above freezing (positive)")
elif temp <0 :
    print("The temperature is below freezing (negative)")
else:
    print("The temperature is exactly at freezing point (zero)")
    
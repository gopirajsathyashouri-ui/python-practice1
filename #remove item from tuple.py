#remove item from tuple

vehicles = ("car", "bike", "truck", "boat")
vehicle_list = list(vehicles)
vehicle_list.remove("bike")
vehicles = tuple(vehicle_list) 

print(vehicle_list)
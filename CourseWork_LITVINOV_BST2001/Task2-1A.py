import math

height = int(input("\nEnter height - "))
width = int(input("\nEnter width - "))
side = int(input("\nEnter the side of the plate - "))


height_min = math.floor((height+side-1)/side)
width_min = math.floor((width+side-1)/side)
result = height_min * width_min

print("\nDesired number of plates - " + str(result))
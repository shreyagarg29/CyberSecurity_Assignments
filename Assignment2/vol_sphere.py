# Write a function that computes the volume of a sphere given its radius
pi = 3.14
def volume(radius):
    vol = (4 / 3) * pi * radius ** 3
    return vol
radius = int(input("Enter the radius: "))
print("Volume of sphere is ")
print(round(volume(radius),2))
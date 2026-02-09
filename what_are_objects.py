class Point:
    x: int = 0
    y: int = 0

p1 = Point()

print(p1.x)
print(p1.y)

p1.x = 10
p1.y = 20

print(p1.x)
print(p1.y)

p1.x = "toto"
p1.z = 0

print(p1.z)

class Person:
    last_name: str = ""

p = Person()
p.lastname = "Doe" # werkt zonder die underscore, maar is nieuwe key

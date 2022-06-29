class GFG:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __repr__(self):
        return str((self.a, self.b))


# list of objects
gfg = [GFG("Hello ", 1),
       GFG("Guys, ", 3),
       GFG("This ", 2),
       GFG("is ", 4),
       GFG("Deepak", 3)]

# sorting objects on the basis of value
# stored at variable b
print(sorted(gfg, key=lambda x: x.b))
# Shipping calculation
def shippingCost(wght):
    cost = weight * 4.00 + 20.00
    return cost


# Premimum Ground
premGround = 120.00

# Weight of package
weight = 41.5

# Ground Shipping
if weight:
    print("Optional Premium Ground Rate: " + str(premGround))
    print(str(shippingCost(weight)))
else:
    print("Error")


def droneShipping(weight):
    cost = weight * 4.50 + 0.00
    return cost


# Drone Shipping option
if weight < 40.0:
    print("Drone Shpping Cost " + str(droneShipping(weight)))
else:
    print("Drone Shipping not optional to heavy")

# Uncomment this when you reach the "Use the Force" section
train_mass = 22680
train_acceleration = 10
train_distance = 100
bomb_mass = 1


# Write your code below:
# Temp function
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5 / 9
    return round(c_temp, 2)


f100_in_celsius = f_to_c(100)
print("Temp from F to C " + str(f100_in_celsius))


def c_to_f(c_temp):
    f_temp = c_temp * 5 / 9 + 32
    return round(f_temp, 2)


c0_in_fahrenheit = c_to_f(0)
print("Temp from C to F " + str(c0_in_fahrenheit))


# Force Section
def get_force(mass, acceleration):
    return mass * acceleration


train_force = get_force(train_mass, train_acceleration)

# Force Continued
print("The GE train supplies " + str(train_force) + " Newtons of force")


def get_energy(mass, c=3 * 10**8):
    bomb_energy = mass * (c**2)
    return bomb_energy


print("A 1kg bomb supplies " + str(get_energy(bomb_mass)) + " Joules")


def get_work(mass=train_mass, acceleration=train_acceleration, distance=train_distance):
    train_work = get_force(mass, acceleration) * distance
    return train_work


print(
    "The GE train does "
    + str(get_work())
    + " Joules of work over "
    + str(train_distance)
    + " meters"
)

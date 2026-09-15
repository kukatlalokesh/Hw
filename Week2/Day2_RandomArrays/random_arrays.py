import numpy as np

# Generate random integers from 1 through 100
random_integers = np.random.randint(1, 101, size=10)

# Generate random floating-point values between 0 and 1
random_floats = np.random.random(10)

print("Random integers:")
print(random_integers)
print("Minimum integer:", random_integers.min())
print("Maximum integer:", random_integers.max())

print("\nRandom floats:")
print(random_floats)
print("Minimum float:", random_floats.min())
print("Maximum float:", random_floats.max())

print("\nInteger range: 1 to 100")
print("Float range: 0 to 1")

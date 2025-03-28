import numpy as np

# arr_1 = np.array([10,20,30,40])
# arr_1_norm = (arr_1 - np.min(arr_1)) / (np.max(arr_1 - np.min(arr_1)))

# print(arr_1_norm)
# print(np.linalg.norm(arr_1))

# dataset = np.array([10, 20, 30, 40, 50])
# sample = np.random.choice(dataset, size=3, replace=False)
# print(sample)


x = np.random.rand(5)
print(x)

x2 = np.random.randn(5)
print(x2)

x3 = np.random.randint(1,5, size=5)
print(x3)

dataset = np.array([10, 20, 30, 40, 50])
print(np.random.choice(dataset, size=3, replace=False))


print(np.random.uniform(1, 5, size=4))
print(np.random.normal(loc=10, scale=2, size=5))
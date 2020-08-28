print(np.inf > 1000000)

arr = np.array([np.inf, 5])
print(repr(arr))

arr = np.array([-np.inf, 1])
print(repr(arr))

# Will result in an OverflowError
np.array([np.inf, 3], dtype=np.int32)

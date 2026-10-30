# Tests if ExampleModule could be used

# Initializing ExampleModule as "ex"
import ExampleModule as ex

# Test if ex.pi could be appended in result
result = ex.pi

# Outputs result. Should be pi
print(result)
# Tests if outputting directly is possible
print(ex.pi)

# Tests functions from ExampleModule
result1 = ex.square(3)
result2 = ex.cube(3)

# Outputs results from functions above
print(result1)
print(result2)
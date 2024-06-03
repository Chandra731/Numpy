# NumPy Exercises

# Import NumPy
import numpy as np

# Create an array of 10 zeros
zeros_array = np.zeros(10)
print("Array of 10 zeros:", zeros_array)

# Create an array of 10 ones
ones_array = np.ones(10)
print("Array of 10 ones:", ones_array)

# Create an array of 10 fives
fives_array = np.ones(10) * 5
print("Array of 10 fives:", fives_array)

# Create an array of the integers from 10 to 50
integers_array = np.arange(10, 51)
print("Array of integers from 10 to 50:", integers_array)

# Create an array of all the even integers from 10 to 50
even_integers_array = np.arange(10, 51, 2)
print("Array of even integers from 10 to 50:", even_integers_array)

# Create a 3x3 matrix with values ranging from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("3x3 matrix with values from 0 to 8:\n", matrix_3x3)

# Create a 3x3 identity matrix
identity_matrix = np.eye(3)
print("3x3 identity matrix:\n", identity_matrix)

# Generate a random number between 0 and 1
random_number = np.random.rand(1)
print("Random number between 0 and 1:", random_number)

# Generate an array of 25 random numbers sampled from a standard normal distribution
random_array = np.random.randn(25)
print("Array of 25 random numbers from standard normal distribution:\n", random_array)

# Create a 10x10 matrix with values from 0.01 to 1
matrix_10x10 = np.arange(0.01, 1.01, 0.01).reshape(10, 10)
print("10x10 matrix with values from 0.01 to 1:\n", matrix_10x10)

# Create an array of 20 linearly spaced points between 0 and 1
linear_spaced_array = np.linspace(0, 1, 20)
print("Array of 20 linearly spaced points between 0 and 1:", linear_spaced_array)

# Numpy Indexing and Selection

# Create the matrix for indexing and selection
mat = np.arange(1, 26).reshape(5, 5)
print("Original matrix:\n", mat)

# Reproduce the output: array([[12, 13, 14, 15],
#                             [17, 18, 19, 20],
#                             [22, 23, 24, 25]])
print("Matrix slice:\n", mat[2:, 1:])

# Reproduce the output: 20
print("Element at row 4, column 5:", mat[3, 4])

# Reproduce the output: array([[ 2],
#                             [ 7],
#                             [12]])
new = mat[:3, 1]
print("New reshaped array:\n", new.reshape(3, 1))

# Reproduce the output: array([21, 22, 23, 24, 25])
print("Last row of the matrix:", mat[4])

# Reproduce the output: array([[16, 17, 18, 19, 20],
#                             [21, 22, 23, 24, 25]])
print("Last two rows of the matrix:\n", mat[3:])

# Matrix Operations

# Get the sum of all the values in mat
total_sum = np.sum(mat)
print("Sum of all values in the matrix:", total_sum)

# Get the standard deviation of the values in mat
std_deviation = np.std(mat)
print("Standard deviation of the matrix:", std_deviation)

# Get the sum of all the columns in mat
column_sum = mat.sum(axis=0)
print("Sum of each column in the matrix:", column_sum)

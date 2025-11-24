import numpy as np
import time

"""A quick deep dive into the performance benefits of NumPy vectorization over traditional nested for loops for matrix addition."""

"""Direct implementation of non-vectorized and vectorized addition of two matrices."""
def direct():
    a = np.random.randint(0, 5, (4, 3))
    print(f"a is a 2-D matrix with the Shape {a.shape} and is: \n{a}\n") # a.shape is 4,3: prints a 4x3 array of random integers between 0 and 9
    b = np.random.randint(0, 5, (4, 1)) 
    print(f"b is a 2-D matrix with the Shape {b.shape} and is: \n{b}\n") # b.shape is 4,1: prints a 4x1 array of random integers between 0 and 9
    c = np.zeros((a.shape[0], a.shape[1])) # c.shape is 4,3: initializes a 4x3 array of zeros
    print(f"c is a 2-D matrix with the Shape {c.shape} and is: \n{c}\n")

    def non_vectorized_addition(a, b):
        start_time = time.time()
        c = np.zeros((a.shape[0], a.shape[1]))
        for i in range(a.shape[0]):          # iterate over rows (top to bottom)
            for j in range(a.shape[1]):      # iterate over columns (left to right)
                c[i, j] = a[i, j] + b[i, 0] # Adds the sameb[i, 0] to each element in row i of a and stores in c
        end_time = time.time()
        print(f"Non-Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        return c

    def vectorized_addition(a, b):
        start_time = time.time()
        c = a + b  # NumPy automatically broadcasts b to match the shape of a
        end_time = time.time()
        print(f"Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        return c

    # Perform Non-Vectorized Addition
    c_non_vectorized = non_vectorized_addition(a, b)
    print(f"Result c using Non-Vectorized Addition: \n{c_non_vectorized}\n")

    # Perform Vectorized Addition
    c_vectorized = vectorized_addition(a, b)
    print(f"Result c using Vectorized Addition: \n{c_vectorized}\n")

    # Verify that both methods yield the same result
    print("Are both methods equal? ", np.array_equal(c_non_vectorized, c_vectorized))



# Trying to be fancy and encapsulate in a class
"""A class encapsulating non-vectorized and vectorized addition of two matrices using NumPy."""
class Small_Numpy_Vectorization:
    def __init__(self):
        # Initialize two matrices a and b and an empty matrix c
        self.a = np.random.randint(0, 5, (3, 2))
        print((f"a is a 2-D matrix with the Shape {self.a.shape} and is: \n{self.a}\n") )# a.shape is 4,3: prints a 4x3 array of random integers between 0 and 9
        self.b = np.random.randint(0, 5, (3, 1)) 
        print(f"b is a 2-D matrix with the Shape {self.b.shape} and is: \n{self.b}\n") # b.shape is 4,1: prints a 4x1 array of random integers between 0 and 9
        self.c = np.zeros((self.a.shape[0], self.a.shape[1])) # c.shape is 4,3: initializes a 4x3 array of zeros
        print(f"c is a 2-D matrix with the Shape {self.c.shape} and is: \n{self.c}\n")
        # Initialize result attributes so they always exist; they'll be computed on demand
        self.c_non_vectorized = None
        self.c_vectorized = None

    def non_vectorized_addition(self, quiet: bool = False):
        a = np.copy(self.a)
        b = np.copy(self.b)
        c = np.copy(self.c)
        start_time = time.time()
        for i in range(a.shape[0]):          # iterate over rows (top to bottom)
            for j in range(a.shape[1]):      # iterate over columns (left to right)
                c[i, j] = a[i, j] + b[i, 0] # Adds the same b[i, 0] to each element in row i of a and stores in c
        end_time = time.time()
        if not quiet:
            print(f"Non-Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        self.c_non_vectorized = c
        return self.c_non_vectorized

    def vectorized_addition(self, quiet: bool = False):
        a= np.copy(self.a)
        b = np.copy(self.b)
        c = np.copy(self.c)
        start_time = time.time()
        c = a + b  # NumPy automatically broadcasts b to match the shape of a
        end_time = time.time()
        if not quiet:
            print(f"Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        self.c_vectorized = c
        return self.c_vectorized
    
    def report(self, quiet: bool = False):
        """Ensure results exist, optionally print them, and return the pair.
        Parameters:
            quiet (bool): If True, suppress printing. Defaults to False.
        Returns:
            tuple: (c_non_vectorized, c_vectorized)
        """
        # Ensure the results exist; compute lazily if not yet produced
        if self.c_non_vectorized is None:
            self.non_vectorized_addition(quiet=quiet)
        if self.c_vectorized is None:
            self.vectorized_addition(quiet=quiet)

        # Optionally print results
        if not quiet:
            # Perform Non-Vectorized Addition
            print(f"Result c using Non-Vectorized Addition: \n{self.c_non_vectorized}\n")
            # Perform Vectorized Addition
            print(f"Result c using Vectorized Addition: \n{self.c_vectorized}\n")
            # Verify that both methods yield the same result
            if self.c_non_vectorized is not None and self.c_vectorized is not None:
                print("Are both methods equal? ", np.array_equal(self.c_non_vectorized, self.c_vectorized))

        # Return the computed results so callers can use them programmatically
        return (self.c_non_vectorized, self.c_vectorized)


def vector_exercise():
    direct()
    print("----- Now using the class -----\n")
    vectorization_instance = Small_Numpy_Vectorization()
    vectorization_instance.report()

"""A small utility function to demonstrate some basic properties of NumPy arrays."""
def np_array_info():
    """A small utility function to demonstrate some basic properties of NumPy arrays."""
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    print(f"Array:\n{arr}") # Print the array
    print(f"Shape: {arr.shape}") # Shape of the array
    print(f"Data Type: {arr.dtype}") # Data type of the array elements
    print(f"Number of Dimensions: {arr.ndim}") # Number of dimensions of the array
    print(f"Size (Total number of elements): {arr.size}") # Total number of elements in the array
    print(f"Item Size (in bytes): {arr.itemsize}") # Size of each element in bytes
    print(f"Total Bytes: {arr.nbytes}") # Total bytes consumed by the array
    print(f"Array Strides: {arr.strides}") # Strides indicate the number of bytes to step in each dimension when traversing the array
    print(f"Is the array C-contiguous? {arr.flags['C_CONTIGUOUS']}") # Check if the array is stored in C-contiguous order

def np_array_exercise():
    # Creation of 1 Dimensional Array
    arr_1d = np.array([10, 20, 30, 40, 50])
    print("---1-D ARRAY---")
    print(f"1D Array with shape {arr_1d.shape}:\n{arr_1d}",end="\n\n")

    # Creation of 2 Dimensional Array
    arr_2d = np.array( [ [1, 2, 3],[4, 5, 6] ] )
    print("---2-D ARRAY---")
    print(f"2D Array with shape {arr_2d.shape}:\n{arr_2d}",end="\n\n")

    # Creation of 3 Dimensional Array
    arr_3d = np.array([ [ [1],[2] ], [ [3],[4] ], [ [5], [6] ] ])
    print("---3-D ARRAY---")
    print(f"3D Array with shape {arr_3d.shape}:\n{arr_3d}",end="\n\n")
    print(f"It has depth: {arr_3d.shape[0]}, rows: {arr_3d.shape[1]}, and columns: {arr_3d.shape[2]}",end="\n\n")

    # Creation of 4 Dimensional Array
    print("---4-D ARRAY---")
    """Looking at the colored brackets seriously helps here - each additional set of brackets adds a new dimension."""
    arr_4d = np.array([  [  [ [1],[2] ] , [ [3],[4]]  ] , [  [ [5],[6] ] , [ [7],[8] ]  ]  ])
    print(f"4D Array with shape {arr_4d.shape}:\n{arr_4d}",end="\n\n")
    print(f"It has rows: {arr_4d.shape[0]}, columns: {arr_4d.shape[1]}, depth: {arr_4d.shape[2]}, and blocks: {arr_4d.shape[3]}")
    
    # Creation of 5 Dimensional Array
    """
    Turning this off because it's a bit excessive for most use cases and clutters the output.
    Uncomment if you want to see the 5D array example.
    print("\n---5-D ARRAY---")
    arr_5d = np.array([[[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]], [[[[9], [10]], [[11], [12]]], [[[13], [14]], [[15], [16]]]]])
    print(f"5D Array with shape {arr_5d.shape}:\n{arr_5d}",end="\n\n")
    print(f"It has rows: {arr_5d.shape[0]}, columns: {arr_5d.shape[1]}, depth: {arr_5d.shape[2]}, blocks: {arr_5d.shape[3]}, and hyper-blocks: {arr_5d.shape[4]}")
    """

np_array_exercise()
print("\n--- NumPy Array Info ---\n")
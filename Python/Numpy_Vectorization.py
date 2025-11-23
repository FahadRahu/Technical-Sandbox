import numpy as np
import time

"""A quick deep dive into the performance benefits of NumPy vectorization over traditional nested for loops for matrix addition."""

def main():
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
            print("Are both methods equal? ", np.array_equal(self.c_non_vectorized, self.c_vectorized))

        # Return the computed results so callers can use them programmatically
        return (self.c_non_vectorized, self.c_vectorized)


if __name__ == "__main__":
    main()
    print("----- Now using the class -----\n")
    vectorization_instance = Small_Numpy_Vectorization()
    vectorization_instance.report()
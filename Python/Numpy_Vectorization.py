import numpy as np
import time

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

    def non_vectorized_addition(self):
        a = np.copy(self.a)
        b = np.copy(self.b)
        c = np.copy(self.c)
        start_time = time.time()
        for i in range(a.shape[0]):          # iterate over rows (top to bottom)
            for j in range(a.shape[1]):      # iterate over columns (left to right)
                c[i, j] = a[i, j] + b[i, 0] # Adds the same b[i, 0] to each element in row i of a and stores in c
        end_time = time.time()
        print(f"Non-Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        return c

    def vectorized_addition(self):
        a= np.copy(self.a)
        b = np.copy(self.b)
        c = np.copy(self.c)
        start_time = time.time()
        c = a + b  # NumPy automatically broadcasts b to match the shape of a
        end_time = time.time()
        print(f"Vectorized Addition took time: {(end_time - start_time)*1000000} microseconds")
        return c
    
    def report(self):
        # Perform Non-Vectorized Addition
        c_non_vectorized = non_vectorized_addition(self)
        print(f"Result c using Non-Vectorized Addition: \n{c_non_vectorized}\n")
        # Perform Vectorized Addition
        c_vectorized = vectorized_addition(a, b)
        print(f"Result c using Vectorized Addition: \n{c_vectorized}\n")
        # Verify that both methods yield the same result
        print("Are both methods equal? ", np.array_equal(c_non_vectorized, c_vectorized))
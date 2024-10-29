#1
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return None
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
        else:
            print("on Stack:", " , ".join(map(str, self.stack)))

#2
class Queue:
    def __init__(self):
        self.queue = []
    
    def push(self, item):
        self.queue.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        return None
    
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def print_queue(self):
        if self.is_empty():
            print("Queue empty")
        else:
            print("Queue:", " , ".join(map(str, self.queue)))

#3
class Matrix:
    def __init__(self, n, m, fill=0):
        self.n = n
        self.m = m
        self.data = [[fill] * m for _ in range(n)]
    
    def get(self, i, j):
        return self.data[i][j]
    
    def set(self, i, j, value):
        self.data[i][j] = value
    
    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.n)] for i in range(self.m)]
        transposed_matrix = Matrix(self.m, self.n)
        transposed_matrix.data = transposed_data
        return transposed_matrix
    
    def multiply(self, other):
        if self.m != other.n:
            raise ValueError("Incompatible matrix dimensions for multiplication")
        
        result = Matrix(self.n, other.m)
        for i in range(self.n):
            for j in range(other.m):
                result.data[i][j] = sum(self.data[i][k] * other.data[k][j] for k in range(self.m))
        return result
    
    def apply(self, func):
        for i in range(self.n):
            for j in range(self.m):
                self.data[i][j] = func(self.data[i][j])
    
    def print_matrix(self):
        for row in self.data:
            print(" ".join(map(str, row)))


print("STACK")

s = Stack()
s.push(1)
s.push(2)
s.print_stack()

print(s.peek())
print(s.pop())
s.print_stack()

print(s.pop())
s.print_stack()

print("QUEUE")


q = Queue()
q.push(1)
q.push(2)
q.print_queue()

print(q.peek())
print(q.pop())
q.print_queue()

print(q.pop())
q.print_queue()

print("MATRIX")

matrix = Matrix(2, 3)
matrix.set(0, 0, 1)
matrix.set(0, 1, 2)
matrix.set(0, 2, 3)
matrix.set(1, 0, 4)
matrix.set(1, 1, 5)
matrix.set(1, 2, 6)

print("Original Matrix:")
matrix.print_matrix()

transposed = matrix.transpose()
print("\nTransposed Matrix:")
transposed.print_matrix()

matrix_b = Matrix(3, 2)
matrix_b.set(0, 0, 7)
matrix_b.set(0, 1, 8)
matrix_b.set(1, 0, 9)
matrix_b.set(1, 1, 10)
matrix_b.set(2, 0, 11)
matrix_b.set(2, 1, 12)

print("\nMatrix B:")
matrix_b.print_matrix()

result = matrix.multiply(matrix_b)
print("\nMatrix A * Matrix B:")
result.print_matrix()

matrix.apply(lambda x: x * 2)
print("\nMatrix after applying lambda (each element * 2):")
matrix.print_matrix()

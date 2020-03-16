def pox(A):
    print("initial position: ",  A[0])
    print("final position: ", len(A)-1)
    for i in range(len(A)-1, 0, -1):
        print(A[i])

if __name__ == "__main__":
    numbers = [0, 1, 2, 3, 4, 5]
    pox(numbers)
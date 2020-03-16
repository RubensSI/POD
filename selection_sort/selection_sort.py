def select_max(A, left, right):
    max_pos = left
    i = left
    while i <= right:
        if A[i] > A[max_pos]:
            max_pos = i
        i = i + 1
    return max_pos

def selection_sort(A):
    for i in range(len(A)-1, 0, -1):
        index = select_max(A, 0, i)
        if index != i:
            tmp = A[index]
            A[index] = A[i]
            A[i] = tmp

def inverter(A):
    for i in range(len(A)//2):
        tmp = A[i]
        A[i] = A[len(A)-1 -i]
        A[len(A)-1 -i] = tmp

if __name__ == "__main__":
    numbers = [12, 2, 4, 18, 6, 5]
    n = select_max(numbers, 0, len(numbers) - 1)

    
    # index of the position with the highest value
    print("highest position", n)

    # ordered list
    selection_sort(numbers)
    print(numbers)

    
    # inverted ordered list
    inverter(numbers)
    print(numbers)
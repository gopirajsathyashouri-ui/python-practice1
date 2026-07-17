# largest even number

def find_largest_even(start, end):
    largest = -1

    for i in range(start, end + 1):
        if i % 2 == 0 :
            largest = i

    return largest        

m = int(input())
n = int(input())


print(find_largest_even(m, n))

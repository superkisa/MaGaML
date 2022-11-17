# Function to check a subsequence can
# be formed with min difference mid

# %%
def can_place(A, n, B, mid):

    count = 1
    last_position = A[0]

    # If a subsequence of size B
    # with min diff = mid is possible
    # return true else false
    for i in range(1, n):
        if A[i] - last_position >= mid:
            last_position = A[i]
            count = count + 1

            if count == B:
                return bool(True)

    return bool(False)


# Function to find the maximum of
# all minimum difference of pairs
# possible among the subsequence
def find_min_difference(A, n, B):

    # Sort the Array
    A.sort()

    # Stores the boundaries
    # of the search space
    s = 0
    e = A[n - 1] - A[0]

    # Store the answer
    ans = 0

    # Binary Search
    while s <= e:
        mid = int((s + e) / 2)

        # If subsequence can be formed
        # with min diff mid and size B
        if can_place(A, n, B, mid):
            ans = mid

            # Right half
            s = mid + 1

        else:

            # Left half
            e = mid - 1

    return ans


# Driver code
# %%
cin = []

with open("algo/input3.txt", "r") as i_f:
    for s in i_f.readlines():
        cin.append(list(map(int, s.rstrip("\n").split())))

# A = [int(i) for i in '1000000000 0 1 10 11 100'.split()]
A = cin[1]
n = len(A)
B = cin[0][1]

min_difference = find_min_difference(A, n, B)

print(A, B)
print(min_difference)
# %%

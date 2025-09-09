#Array Mutation

#Given an integer n and an array a of length n, your task is to apply the following mutation to a:

#    Array a mutates into a new array b of length n.
#    For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
#    If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].

#Example

#For n = 5 and a = [4, 0, 1, -2, 3], the output should be solution(n, a) = [4, 5, -1, 2, 1].

def array_mutate(inputArray: [int]):
    mutated = []
    for i in range(len(inputArray)):
        if i == 0:
            mutated.append(inputArray[i] + inputArray[i + 1])
        elif i == len(inputArray) - 1:
            mutated.append(inputArray[i - 1] + inputArray[i])
        else:
            mutated.append(inputArray[i - 1] + inputArray[i] + inputArray[i + 1])
    return mutated

print(array_mutate([4,0,1,-2,3]))

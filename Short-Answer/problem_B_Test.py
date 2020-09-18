def problemB(n):
    sum = 0
    for i in range(n):
        j = 1
        while j < n:
            j *= 2
            sum += 1
    return f'the for loop ran {n} times, the while loop ran {sum} times'

print(problemB(1))
print(problemB(2))
print(problemB(3))
print(problemB(4))
print(problemB(5))
print(problemB(10))
print(problemB(20))
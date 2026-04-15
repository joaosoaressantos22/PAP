def sum(N):
    if N == 0:
        return 0
    else:
        return N + sum(N - 1)

print(sum(5))

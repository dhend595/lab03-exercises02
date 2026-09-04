def check(l: list):
    bool_pair = len(l) != len(set(l))
    return bool_pair

print(check([1, 2, 3, 2]))          # should print True
print(check([5, 2, -10, 44, 90]))   # should print False

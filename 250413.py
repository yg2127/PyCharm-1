def truth_function(p, q, r, s):
    return (p or q) and (r or s)

print(truth_function(False, True, True, False))
print(truth_function(True, False, False, True))
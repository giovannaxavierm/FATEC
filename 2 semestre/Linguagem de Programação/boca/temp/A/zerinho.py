A, B, C = str(input()).split(" ")

A = int(A)
B = int(B)
C = int(C)

if A == B == C:
    print("*")
if A != B and A != C:
    print("A")
if B != A and B != C:
    print("B")
if C != A and C != B:
    print("C")
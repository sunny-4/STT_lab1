# Simple Python Pattern Printer
# This program prints some basic patterns

print("=== Pattern 1: Triangle of Stars ===")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n=== Pattern 2: Square of Stars ===")
for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

print("\n=== Pattern 3: Right-Aligned Triangle ===")
for i in range(1, 6):
    print(" " * (5 - i), end="")
    print("*" * i)

print("\n=== Pattern 4: Numbers Triangle ===")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n=== Pattern 5: Reverse Numbers Triangle ===")
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

print("\n=== Done Printing Patterns ===")

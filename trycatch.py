import sys

try:
    nama = input("Enter your name: ")
    if not nama.strip():
        raise ValueError("Name must contain only letters")
    else:
        print("Hello, " + nama)
except ValueError as e:
    print(f"ValueError caught: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
    sys.exit(1)

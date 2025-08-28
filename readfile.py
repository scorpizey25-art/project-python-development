try:
    with open('examp/example.txt', 'r') as file:
        ambil = file.read()
        print(ambil)
except IOError as e:
    print(f"An IOError occurred: {e}")

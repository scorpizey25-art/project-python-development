try:
    with open('examp/example.txt', 'w') as file:
        file.write("Apps Name : Scorpizey25-art\n")
        file.write("Version : 1.0\n")
        file.write("Developer : Scorpizey25\n")
except IOError as e:
    print(f"An IOError occurred: {e}")

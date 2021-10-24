print("program started")
print("Please enter a standard character")
charactar = input()
if len(charactar) == 1:
    print(f" the ascii code for {charactar} is {ord(charactar)}")

else:
    print("error message")

print("program ended")
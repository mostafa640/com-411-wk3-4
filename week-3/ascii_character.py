print("Program Started")
print("Please enter an ASCII code")
code = int(input())
if code >= 32 and code <= 126:
    print(f"The character represented by the Ascii code {code} is {chr(code)}")
else:
    print("message error")
print("program ended")


print("enter phone number")
phone = input()
digits_mapping = {
    "1": "one",
    "2": "two",
    "3": "three"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch) + " "
print(output)
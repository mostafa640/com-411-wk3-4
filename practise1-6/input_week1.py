# print("\n Displays a new line")
# print("\t Displays a tab space")
# print("\\ Displays a back slash")
# print("\" Displays a double quote")
# print("\' Displays a single quote")

lives = int(input("Please enter the number of lives"))
energy_level = int(input("please enter energy level"))
sh_level = int(input("please enter the shild level"))

print(f"Health has been set \nLives: {'♥' * lives} \nEnergy: {'♥' * energy_level} \nShield: {'♥' * sh_level}")

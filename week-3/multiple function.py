# # # def display_box(name):
# # #     message = f"* Hello {name} *"
# # #     print("*" * len(message))
# # #     print(message)
# # #     print("*" * len(message))
# # #
# # #
# # # def greet_user():
# # #     print("Please enter your name")
# # #     name = input()
# # #     display_box(name)
# # #
# # #
# # # greet_user()
# #
# # def display_ladder(steps):
# #     for step in range(steps):
# #         print("| |")
# #         print("***")
# #     print("done")
# #
# # def create_ladder():
# #     print("how many steps remaining")
# #     steps = int(input())
# #     display_ladder(steps)
# # create_ladder()
# #
# # return value:::
# #
# # def get_name():
# #     print("Please enter your name")
# #     name = input()
# #     return name
# #
# #
# # print("Retrieved name:", get_name())
#
# def sum_weights(beep_weight, bop_weight):
#     total_weight = beep_weight + bop_weight
#     return total_weight
# def calc_avg_weight(beep_weight, bop_weight):
#     avg_weight = sum_weights(beep_weight, bop_weight) / 2
#     return avg_weight
# def run():
#     print("please enter beep weight")
#     beep_weight = float(input())
#     print("please enter bop weight")
#     bop_weight = float(input())
#     print("please enter the action")
#     action = input()
#     if action == "sum":
#         answer = sum_weights(beep_weight, bop_weight)
#         print(f"The sum of Beep's and Bop's weight is {answer:.2f}")
#     elif action == "average":
#         answer = calc_avg_weight(beep_weight, bop_weight)
#         print(f"The average of Beep's and Bop's weight is {answer:.2f}")
#     else:
#         print("I am not sure what you would like to do.")
#
# run()
# def display_box(word):
#     num_dashes = 4 + len(word)
#     print("-" * num_dashes)
#     print(f"| {word} |")
#     print("-" * num_dashes)
# def display_lower_case(word):
#     print(word.lower())
# def display_upper_case(word):
#     print(word.upper())
# def display_mirrored(word):
#     mirrored = ""
#     for letter in reversed(word):
#         mirrored += letter
#     print(f"{word} | {mirrored}")
# def display_repeated(word):
#     print("how many times should the word be displayed")
#     repetitions = int(input())
#
#     for repetition in range(repetitions):
#         if (repetition % 2 == 0):
#             print(display_lower_case(word))
#         else:
#             print(display_upper_case(word))
# def run():
#     print("pleease enter a word")
#     word = input()
#     print("What would you like to do with this word")
#     print("[1] Display in a box")
#     print("[2] Display lower-case")
#     print("[3] Display upper-case")
#     print("[4] Display mirrored")
#     print("[5] Display repeated")
#     print("[6] Quit")
#
#     response = int(input())
#     if response == 1:
#         display_box(word)
#     elif response == 2:
#         display_lower_case(word)
#     elif response == 3:
#         display_upper_case(word)
#     elif response == 4:
#         display_mirrored(word)
#     elif response == 5:
#         display_repeated(word)
#     else:
#         print("unknown option")
#
# run()
#
def display_box(word):
    num_dashes = 4 + len(word)
    print("-" * num_dashes)
    print(f"| {word} |")
    print("-" * num_dashes)


def display_lower_case(word):
    print(word.lower())


def display_upper_case(word):
    print(word.upper())


def display_mirrored(word):
    mirrored = ""
    for letter in reversed(word):
        mirrored += letter
    print(f"{word} | {mirrored}")


def display_repeated(word):
    print("How many times should the word be displayed?")
    repetitions = int(input())

    for repetition in range(repetitions):
        # even repetition
        if (repetition % 2 == 0):
            print(display_lower_case(word))
        # odd repetition
        else:
            print(display_upper_case(word))


def run():
    print("Please enter a word:")
    word = input()
    is_looping = True

    while (is_looping):



    # get the user's selection
        print("What would you like to do with this word?")
        print("[1] Display in a box")
        print("[2] Display lower-case")
        print("[3] Display upper-case")
        print("[4] Display mirrored")
        print("[5] Display repeated")
        print("[6] Quit")

        response = int(input())

    # determine and execute action
        if response == 1:
            display_box(word)
        elif response == 2:
            display_lower_case(word)
        elif response == 3:
            display_upper_case(word)
        elif response == 4:
            display_mirrored(word)
        elif response == 5:
            display_repeated(word)
        else:
            print("Unknown option.")


run()
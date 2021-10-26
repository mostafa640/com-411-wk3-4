def display_chars(file_path, num_char):
    print("The first 5 characters are:")
    with open(file_path) as file:
        data = file.read(num_char)
        print(data)

def display_line(file_path):
    with open(file_path) as file:
        print("\nThe first line is:")
        data = file.readline().strip()
        print(data)
def display_l(file_path):
    with open(file_path) as file:
        data = file.read()
        lines = data.split()
        print(lines)


def display_text(file_path):
    print("The full text is:")
    with open(file_path) as file:
        data = file.read()
        print(data)




def run():
    display_chars("library.txt", 5)
    display_line("library.txt")
    display_text("library.txt")
    display_l("library.txt")

if __name__ == "__main__":
    run()





def directions():
    direction = ["Move forwade", "Move backward", "Turn left", "Turn right"]
    return direction
def menu():
    print("please select a direction")
    direc = directions()
    for index in range(len(direc)):
        print(f"{index}: {direc[index]}")

def run():
    menu()
if __name__ == "__main__":
    run()
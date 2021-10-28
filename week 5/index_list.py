def movements():
    return ["Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
def run():
    print("Moving...")

    directions = movements()
    print(f"{directions[0]} for {directions[1]} steps")
    print(f"{directions[2]} for {directions[3]} steps")
    print(f"{directions[4]} for {directions[5]} steps")
    print(f"{directions[6]} for {directions[7]} steps")

if __name__ == "__main__":
    run()
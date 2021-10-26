def export(file_path, num_bots):
    print("Exporting...")
    with open(file_path, "a") as file:
        for count in range(num_bots):
            bot_id = int(input("Please enter the bots id"))
            bot_name = input("Please enter the bots name")
            bot_paint = input("Please enter the bots paint")
        data = f"{bot_id},{bot_name},{bot_paint}"
        file.write(data)
    print("done!")
def run():
    export("exported_bots.cvs", 2)
if __name__ == "__main__":
  run()

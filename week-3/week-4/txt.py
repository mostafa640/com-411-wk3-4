import os
def cwd():
    path = os.getcwd()
    print(f"current working directory: {path}")
    print(f"directory contains the following:")
    for file in os.listdir(path):
        print(file)

def run():
    print("processing...")
    cwd()
if __name__ == "__main__":
    run()


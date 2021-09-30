import time
import shutil
import os

def main():
    while True:
        path = r"/home/igor/Рабочий стол/"
        end_path = "/home/igor/FromDesktop/" 
        for item in os.listdir(path):
            if item[0] != '.':
                item_path = f"{path}/{item}"
                shutil.move(item_path, end_path)
        time.sleep(10)

if __name__ == "__main__":
    main()
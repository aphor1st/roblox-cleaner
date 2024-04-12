import os
colors = {
    "green": "\033[92m",
    "red": "\033[91m",
    "reset": "\033[0m"
}
dir = f"C:/Users/{os.getlogin()}/AppData/Local/Roblox/logs"
os.system('cls')
for file in os.listdir(dir):
    try:
        os.remove(dir+"/"+file)
    except:
        print(f'{colors["red"]}Could not remove:{colors["reset"]}', dir+"/"+file)

print(f"{colors['green']}Finished clearing logs directory!{colors['reset']}")
input("ENTER to exit")
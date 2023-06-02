import json, os
from colorama import Fore, Style

print(f"{Fore.CYAN}Config Gen: v1.0{Style.RESET_ALL}")


# define functions
def info(text: str):
    print(f"{Fore.GREEN}[Info]{Style.RESET_ALL} {text}")


def warn(text: str):
    print(f"{Fore.YELLOW}[Warn]{Style.RESET_ALL} {text}")


def prompt(prompt: str, default_yes: bool = True):
    p = ""
    while True:
        p = input(
            prompt + f" [{'Y' if default_yes else 'y'}/{'n' if default_yes else 'N'}]: "
        )
        if not p.lower() in ["y", "n"]:
            print("Please respond with only 'y' or 'n'")
        else:
            return True if p.lower() == "y" else False


# import config and check existing values
config = {}
info("Checking for config.json")
if not os.path.exists("config.json"):
    info("Config does not exist, skip load file...")
else:
    info("Loading values from config...")
    with open("config.json", "r") as f:
        config = json.load(f)

# prompt for settings, then save
try:
    if not config["Message"] in ["YOUR MESSAGE HERE", ""]:
        warn("Message in config already has value! Continuing will overwrite the value")
        if not prompt("Continue anyway?"):
            exit()
except KeyError:
    pass

config["Message"] = input("Message to be spammed: ")

try:
    if not config["Webhook"] in ["YOUR WEBHOOK HERE", ""]:
        warn("Webhook in config already has value! Continuing will overwrite the value")
        if not prompt("Continue anyway?"):
            exit()
except KeyError:
    pass

config["Webhook"] = input("Webhook to send message to: ")

# Save config to file
info("Saving config...")
warn("This will overwrite anything already in config!")
if not prompt("Proceed?"):
    exit()
with open("config.json", "w") as f:
    json.dump(config, f, indent=4)
info("Saved config successfully!")

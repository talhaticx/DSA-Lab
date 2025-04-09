def cprint(text, color, bold=False, underline=False):
    colors = {
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "reset": "\033[0m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m",
        "green_bg": "\033[1;42m",
        "red_bg": "\033[1;41m",
        "yellow_bg": "\033[1;43m"
    }
    
    style = ""
    if bold:
        style += "\033[1m"
    if underline:
        style += "\033[4m"
    
    color_code = colors.get(color, "")
    print(f"{style}{color_code}{text}\033[0m", end="")

def cPass(msg=""):
    cprint(" PASS ", "green_bg", bold=True)
    if msg:
        print(f" - {msg}")
    else:
        print()

def cFail(msg=""):
    cprint(" FAIL ", "red_bg", bold=True)
    if msg:
        print(f" - {msg}")
    else:
        print()

def cWarn(msg=""):
    cprint(" WARNING ", "yellow_bg", bold=True)
    if msg:
        print(f" - {msg}")
    else:
        print()

def cInfo(text):
    cprint(text, "cyan", bold=True)
    print()
    
import sys
import time

def progress_loader(current, total, length=30, prefix="Progress"):
    """
    Displays a dynamic progress bar.
    
    :param current: Current progress count
    :param total: Total count to reach
    :param length: Length of the progress bar (default 30)
    :param prefix: Label before the progress bar
    """
    percent = f"{(current / total) * 100:.1f}"
    filled = int(length * current // total)
    bar = "█" * filled + "-" * (length - filled)
    sys.stdout.write(f"\r{prefix}: [{bar}] {percent}%")
    sys.stdout.flush()

if __name__ == '__main__':
    cPass("Hello")
    cFail("Something went wrong")
    cWarn("Be careful!")
    cInfo("This is an info message")

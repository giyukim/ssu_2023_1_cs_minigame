import os
import platform

def clear_screen() -> None:
    now_system = platform.system()
    if now_system == "Windows":
        os.system("cls")
    elif now_system == "Linux" or now_system == "Darwin":
        os.system("clear")
    else:
        from .error import raise_error as error
        error("Unable to detect OS")
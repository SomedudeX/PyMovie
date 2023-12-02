import os
import sys
import bootstrapper

from time import sleep as wait
from sys import exit as terminate
from multiprocessing import freeze_support as fix_pyinstaller_multiprocessing_issue

try: 
	from colorama import just_fix_windows_console as fix_windows_color_output
except ImportError as e:
	print()
	print(f" [Error] Required package not installed: {str(e).lower()}")
	print(f" > Program cannot continue, make sure you have installed all required packages in your current python version. ({sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro})")
	print(f" > All required packages can be installed through 'pip' (Windows) or 'pip3' (macOS/Linux) command. ")
	print(f" > ")
	input(f" > Press [Enter/Return] to quit... ")


class COLOR:

	PURPLE = '\033[95m'
	CYAN = '\033[96m'
	DARKCYAN = '\033[36m'
	BLUE = '\033[94m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	END = '\033[0m'


def clear():

	if sys.platform == "win32":
		os.system("cls")
	else: 
		os.system("clear")


if __name__ == "__main__": 
	fix_windows_color_output()
	fix_pyinstaller_multiprocessing_issue()
	clear()
	print(f"{COLOR.BOLD}\b [Log] Initializing bootstrapper{COLOR.END}")
	wait(0.5)
	bootstrapper.initialize()

	from main import mainloop
	print(f"{COLOR.BOLD}\b [Log] Entering mainloop{COLOR.END}")
	wait(0.2)
	try: mainloop()
	except: pass
	clear()
	print(" [Log] Terminated by user request...")
	print(" [Log] Finishing script...")
	if sys.platform == "win32":
		print()
		print(" > Press [Return/Enter] to quit...")
	terminate(0)

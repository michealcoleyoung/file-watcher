import sys
import time
import logging
import watchdog.events
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from tkinter import filedialog as fd


def user_instructions():
    """
 /$$$$$$$$ /$$ /$$                 /$$      /$$             /$$               /$$
| $$_____/|__/| $$                | $$  /$ | $$            | $$              | $$
| $$       /$$| $$  /$$$$$$       | $$ /$$$| $$  /$$$$$$  /$$$$$$    /$$$$$$$| $$$$$$$   /$$$$$$   /$$$$$$
| $$$$$   | $$| $$ /$$__  $$      | $$/$$ $$ $$ |____  $$|_  $$_/   /$$_____/| $$__  $$ /$$__  $$ /$$__  $$
| $$__/   | $$| $$| $$$$$$$$      | $$$$_  $$$$  /$$$$$$$  | $$    | $$      | $$  \ $$| $$$$$$$$| $$  \__/
| $$      | $$| $$| $$_____/      | $$$/ \  $$$ /$$__  $$  | $$ /$$| $$      | $$  | $$| $$_____/| $$
| $$      | $$| $$|  $$$$$$$      | $$/   \  $$|  $$$$$$$  |  $$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$
|__/      |__/|__/ \_______/      |__/     \__/ \_______/   \___/   \_______/|__/  |__/ \_______/|__/

Instructions:
1. Create a plain text file with a list of filepaths that you would like to monitor. Make sure the path is exact.

EXAMPLE:
C:/Documents/Newsletters/Summer2018.pdf
C:/Documents/Newsletters/Summer2019.pdf
C:/Documents/Newsletters/Summer2020.pdf
C:/Documents/Newsletters/Summer2021.pdf

2. As changes are made you will see updates to these files in realtime

    """


print(user_instructions.__doc__)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # TODO: ask user to specify a few files they would like to watch from top to bottom as read from text file
    # TODO: retrieve filepath and store via a dictionary
    # TODO: output any modifications made to these files in the terminal

    input('Press enter to continue...')

    # set path
    path = fd.askopenfilename()
    print("*** Watching Files ***")

    # reads from txt file with list of
    with open(path) as f:
        new_list = [x.strip('\n') for x in f]

        # intiliaze logging event handler
        event_handler = LoggingEventHandler()

        # initialize observer
        observer = Observer()

        for path in new_list:
            observer.schedule(event_handler, path, recursive=True)

        # start observer
        observer.start()
        try:
            while True:
                time.sleep(1)
        finally:
            observer.stop()
            observer.join()
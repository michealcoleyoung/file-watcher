import sys
import time
import logging
import watchdog.events
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler
from tkinter import filedialog as fd


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # TODO: ask user to specify a few files they would like to watch from top to bottom as read from text file
    # TODO: retrieve filepath and store via a dictionary
    # TODO: output any modifications made to these files in the terminal

    # set path
    # user_input = input("Enter the name of the files you would like to watch: ")
    # paths = user_input.split()
    # print(paths)

    with open('/Users/michealyoung/Downloads/test-file-list.txt') as f:
        print(f.readlines())

    # intiliaze logging event handler
    event_handler = LoggingEventHandler()

    # initialize observer
    observer = Observer()

    for path in paths:
        observer.schedule(event_handler, path, recursive=True)

    # start observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
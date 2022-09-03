import sys
import time
import logging
import watchdog.events
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')

    # TODO: ask user to specify a few files they would like to monitor
    # TODO: retrieve filepath and store via a dictionary
    # TODO: output any modifications made to these paths in the terminal

    # set path
    path = "/Users/michealyoung/Desktop/test-change/test-spreadsheet.ods"

    # intiliaze logging event handler
    event_handler = LoggingEventHandler()

    # initialize observer
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)

    # start observer
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
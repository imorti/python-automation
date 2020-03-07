from watchdog import observers
from watchdog.events import FileSystemEventHandler
import json
import time
import os

class FileHandler(FileSystemEventHandler):
    i = 1
    def on_modified(self, event):
        for filename in os.listdir(home):
            source = home +"/"+ filename
            new_folder = destination +"/"+ filename
            os.rename(source, new_folder)


home = "/Users/imorti/work/python/automation/1"
destination = "/Users/imorti/work/python/automation/2"

event_handler = FileHandler()
observer = observers.Observer()
observer.schedule(event_handler, home, recursive=True)
observer.start()

try: 
    while True: 
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
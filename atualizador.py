import subprocess
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        super().__init__()
        self.command = command
        self.process = None
        self.start_process()

    def start_process(self):
        if self.process:
            self.process.kill()
        self.process = subprocess.Popen([sys.executable] + self.command)

    def on_modified(self, event):
        if event.src_path.endswith('.py'):
            print(f'{event.src_path} changed, restarting...')
            self.start_process()

if __name__ == "__main__":
    path = "."
    command = ["Main.py"]  # Nome do seu arquivo principal
    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    

import os
import time

class SystemMonitor:
    def __init__(self, watch_directory):
        self.watch_directory = watch_directory
        self.last_modified = {}

    def monitor_changes(self):
        while True:
            for file in os.listdir(self.watch_directory):
                filepath = os.path.join(self.watch_directory, file)
                if os.path.isfile(filepath):
                    last_modified_time = os.path.getmtime(filepath)
                    if filepath not in self.last_modified or self.last_modified[filepath] != last_modified_time:
                        self.last_modified[filepath] = last_modified_time
                        print(f"File changed: {filepath}")
                        # Trigger test case update logic here
            time.sleep(5)
import threading
import os
import sys

class ProgressPercentage(object):
    def __init__(self, file_name):
            self._file_name = file_name
            self._size = float(os.path.getsize(file_name))
            self._seen_so_far = 0
            self._lock = threading.Lock()
    
    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s %s / %s (%.2f%%)" % (self._file_name, self._seen_so_far, self._size, percentage)
                )
            sys.stdout.flush()
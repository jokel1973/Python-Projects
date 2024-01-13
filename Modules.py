

import os

from os.path import join, getmtime
from datetime import datetime

def get_latest_mtime(directory):
    files = [f for f in os.listdir(directory) if f.endswith(".txt")]
    for file in files:
        file_path = join(directory, file)
        mtime = getmtime(file_path)
        formatted_mtime = datetime.fromtimestamp(mtime).strftime('%Y-%m-%d %H:%M:%S')
        print(f"File: {file}, Last Modified Time: {formatted_mtime}")

if __name__ == "__main__":
    directory_path = "C:\\Python_projects\\Modules_python\\"
    get_latest_mtime(directory_path)

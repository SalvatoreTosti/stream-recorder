import os
import time
import subprocess
from datetime import datetime

url = os.environ.get('STREAM_URL')
if not url:
    print("No stream URL specified, set the 'STREAM_URL' variable")
    exit(1)

while True:
    _now_str = f'{datetime.utcnow():%Y%m%d_%H%M%S}'
    filename = f"output_{_now_str}.ts"

    print(f"[{_now_str}] - Establishing connection to {url}...")
    out = subprocess.run(["streamlink", "-o", "out" + os.sep + filename, url, "1080p,best"], capture_output=True) 
    print(f"[{_now_str}] - Closed connection to {url}... (return code {out.returncode})")
    time.sleep(300) #5 minutes


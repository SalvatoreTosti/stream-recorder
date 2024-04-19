# Overview
This program attempts to connect to the target stream every five minutes.
If a connection is established, the program will start recording the stream and save the recording into the `/out` directory with a name corresponding to the current time.
If connection to the stream is interrupted, the program will attempt to reconnect every five minutes.
The target stream is provided to the program via the `STREAM_URL` variable. (ex. `export STREAM_URL=https://www.twitch.tv/saltybet`)
Note: The recordings are saved in the `.ts` file format, these can be viewed or re-encoded with programs like [VLC](https://www.videolan.org/vlc/) or [handbrake](https://handbrake.fr/).

# Running the program via Python
1. `python3 -m venv env`
2. `source env/bin/activate`
3. `pip install -r requirements.txt`
4. `export STREAM_URL=<target-stream-url>`
5. `python3 main.py`

# Running the program via Docker
1. `docker build --tag stream-watcher -f Dockerfile .`
2. `docker run -e STREAM_URL=<target-stream-url>  -v ./out:/home/app/out --name stream-watcher-container --rm stream-watcher`
Note: The above command will bind the `/out` directory on the host OS to the `/out` directory in the docker container, so the recordings will appear in the host OS.

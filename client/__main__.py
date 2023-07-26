from pathlib import Path
from dotenv import dotenv_values
import datetime

from backend import get_id_token, get_device, get_pattern

# 1s between polling
BACKEND_POLL_PERIOD = datetime.timedelta(seconds=1)

path = Path(__file__).parent / "../env/user.env"
config = dotenv_values(path)

# get firebase token
id_token = get_id_token(config["username"], config["password"])

content = None
last_polled_content = datetime.datetime.now() - BACKEND_POLL_PERIOD

while True:

    # poll backend
    now = datetime.datetime.now()
    if now > last_polled_content + BACKEND_POLL_PERIOD:
        last_polled_content = now

        # retrieve info
        device = get_device(id_token)
        pattern = device["Pattern"]

        if not pattern is None:
            new_content = device["Pattern"]["content"]
            if new_content != content:
                print(new_content)

            content = new_content


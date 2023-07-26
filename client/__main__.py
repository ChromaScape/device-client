from pathlib import Path
from dotenv import dotenv_values
import time

from backend import get_id_token, get_device

# comment to run locally
from led_control import set_color, show

# def set_color(i, color):
#     print(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))


# def show():
#     pass


# these should come from model and backend respectively
import dummy_pos
import dummy_fragment
light_pos = dummy_pos.light_pos
fragment = dummy_fragment.fragment

# 1hz backend polling rate
BACKEND_POLL_PERIOD = 1

# 10hz led refresh rate
LED_POLL_PERIOD = 1/10

path = Path(__file__).parent / "../env/user.env"
config = dotenv_values(path)

# get firebase token
id_token = get_id_token(config["username"], config["password"])

content = None

now = time.time()
last_polled_content = now - BACKEND_POLL_PERIOD
last_polled_led = now - LED_POLL_PERIOD

while True:

    # poll backend
    now = time.time()
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

    # update lights
    if now > last_polled_led + LED_POLL_PERIOD:
        for i, p in enumerate(light_pos):
            color = fragment(p, now)
            set_color(i, color)

        show()



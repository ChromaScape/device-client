from argparse import ArgumentParser
from pathlib import Path
import sys
import requests
import json


# duplicated code from client/backend.py, but I couldn't figure out how to import :'(
def get_firebase_api_key():
    path = Path(__file__).parent / "../firebase_config.json"
    firebase_config = json.load(open(path, "r"))
    return firebase_config["apiKey"]

def create_user(user, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signUp?key=" + get_firebase_api_key()
    payload = '{"email":"%s","password":"%s","returnSecureToken":true}' % (
        user,
        password,
    )
    headers = {"content-type": "application/json"}
    r = requests.post(url, data=payload, headers=headers)
    if not r.status_code == 200:
        raise Exception("couldn't create firebae user")

    return r.json()["idToken"]

def create_device(firebase_token):
    url = "https://chromascape-api-adrienpringle.vercel.app/api/device"
    headers = {"content-type": "application/json", "Authorization": firebase_token}
    r = requests.post(url, headers=headers)
    if not r.status_code == 200:
        sys.exit("couldn't update backend")

# get params
parser = ArgumentParser()
parser.add_argument(
    "-u", "--user", help="email used to create firebase credentials for device"
)
parser.add_argument(
    "-p", "--password", help="password used to create firebase credentials for device"
)
args = parser.parse_args()


# create firebase user
firebase_token = create_user(args.user, args.password)

# create device in backend
create_device(firebase_token)

# export device credentials to file
content = """
username=%s
password=%s
""" % (
    args.user,
    args.password,
)
path = Path(__file__).parent / "../env/user.env"
with open(path, "w") as file:
    file.write(content)

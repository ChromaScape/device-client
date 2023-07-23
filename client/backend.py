from pathlib import Path
import json
import requests

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


def get_id_token(user, password):
    url = "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=" + get_firebase_api_key()
    payload = '{"email":"%s","password":"%s","returnSecureToken":true}' % (
        user,
        password,
    )
    headers = {"content-type": "application/json"}
    r = requests.post(url, data=payload, headers=headers)
    if not r.status_code == 200:
        raise Exception("couldn't sign in firebae user")

    return r.json()["idToken"]


def get_device(firebase_token):
    url = "https://chromascape-api-adrienpringle.vercel.app/api/device"
    headers = {"content-type": "application/json", "Authorization": firebase_token}
    r = requests.get(url, headers=headers)
    if not r.status_code == 200:
        raise Exception("http error")

    return r.json()
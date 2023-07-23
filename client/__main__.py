#####################################
### example of retrieving device info
#####################################

from pathlib import Path
from dotenv import dotenv_values

from backend import get_id_token, get_device

path = Path(__file__).parent / "../env/user.env"
config = dotenv_values(path)

# get token
id_token = get_id_token(config["username"], config["password"])

# retrieve info
print(get_device(id_token))

#####################################
### light control goes here
#####################################

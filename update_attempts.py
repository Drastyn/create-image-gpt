import requests
from os import getenv

GH_TOKEN = getenv("GH_TOKEN")
GH_URL = "https://api.github.com/repos/Drastyn/curso-prompt-coderhouse/actions/variables/ATTEMPTS"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GH_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}

def main():
  current_attempts = requests.get(GH_URL, headers=HEADERS).json()['value']
  new_attempts = int(current_attempts) + 1
  requests.patch(GH_URL, headers=HEADERS, data={ "name":"ATTEMPTS", "value"; str(new_attempts) })

main()

import requests
from os import getenv

GH_TOKEN = getenv("GH_TOKEN")
ATTEMPTS = getenv("ATTEMPTS")
GH_URL = "https://api.github.com/repos/Drastyn/curso-prompt-coderhouse/actions/variables/ATTEMPTS"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": f"Bearer {GH_TOKEN}",
    "X-GitHub-Api-Version": "2022-11-28"
}


def main():
  new_attempts = int(ATTEMPTS) + 1
  requests.patch(GH_URL, headers=HEADERS, json={ "name":"ATTEMPTS", "value": str(new_attempts) })


main()

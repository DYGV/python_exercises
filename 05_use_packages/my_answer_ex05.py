# encoding : utf-8
import requests
import json

def main(user_name, repo_name):
    BASE_URL = 'https://api.github.com/repos/{0}/{1}/issues'
    url = BASE_URL.format(user_name, repo_name)

    req = requests.get(url)
    if req.ok:
        issues = req.json()
        for issue in issues:
            print(issue['title'])

if __name__ == "__main__":
    user_name = 'tensorflow'
    repo_name = 'tensorflow'
    main(user_name, repo_name)

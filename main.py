import requests
from requests import Response
import hashlib


def request_api_data(query_char: str):
    url = f'https://api.pwnedpasswords.com/{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching:{response.status_code}, check the api and try again.')

    return response


def get_password_leaks_count(hashes: Response, hash_to_check):
    hashed_passwords = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashed_passwords:
        print(h)


def pwned_api_check(password: str):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_chars = sha1password[:5]
    tail = sha1password[5:]
    response = request_api_data(first_five_chars)
    return get_password_leaks_count(response, tail)

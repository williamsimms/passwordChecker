import requests


def request_api_data(query_char: str):
    url = f'https://api.pwnedpasswords.com/{query_char}'
    response = requests.get(url)
    if response.status_code != 200:
        raise RuntimeError(
            f'Error fetching:{response.status_code}, check the api and try again.')


def pwned_api_check(password: str):
    pass

import requests
from requests.structures import CaseInsensitiveDict
import json

def _request_colourhunt_data(step):
    URL = "https://colorhunt.co/php/feed.php"

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/x-www-form-urlencoded"

    data = "step="+str(step)+"&sort=popular&timeframe=4000"

    response = requests.post(URL, headers=headers, data=data)
    response_list = json.loads(response.text)

    return response_list


if __name__ == "__main__":
    data = []
    for n in range(25):
        data +=_request_colourhunt_data(n)

    with open('palletes.json', 'w') as f:
        json.dump(data, f)

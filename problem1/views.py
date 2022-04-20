import requests
from requests.exceptions import HTTPError
from rest_framework.decorators import api_view
from rest_framework.response import Response
import re


# Create your views here.


def is_url_valid(url):
    regex = ("((http|https)://)(localhost:8090/)?" + "(primes|odd|fibo|rand)")

    if re.match(regex, url):
        return True
    return False


def get_response(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        jsonResponse = response.json()
        return dict(jsonResponse)

    except HTTPError as http_err:
        return None
    except Exception as e:
        return None


@api_view(['GET'])
def numbers(request):
    if request.method == 'GET':
        path = request.get_full_path()

        path = path.replace("http://localhost:port/numbers?url", "")

        url_list = path.split('&url=')

        valid_url_list = []

        for url in url_list:
            if is_url_valid(url):
                valid_url_list.append(url)

        numbers_list = []

        for url in valid_url_list:
            response = get_response(url)
            if response is not None:
                numbers_list += response['numbers']

        numbers_set = set(numbers_list)

        return Response(sorted(numbers_set))

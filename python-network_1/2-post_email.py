import requests
import sys

def post_email(url=sys.argv[1], email=sys.argv[2]):
    data = {'email': email}
    response = requests.post(url, data=data)
    print(response.text)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
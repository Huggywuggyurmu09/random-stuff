import requests
import time

URL = "https://gofile.io/d/..." # normally 6 digits long, but may be more.

def ping_gofile():
    try:
        response = requests.head(URL, timeout=10)
        if response.status_code == 200:
            print("Pinged successfully. File is still alive.")
        else:
            print(f"Unexpected status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging file: {e}")

if __name__ == "__main__":
    ping_gofile()

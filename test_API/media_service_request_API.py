import requests
import json
from time import time
import argparse

parser = argparse.ArgumentParser(description='List of uuid, id_type, test')
parser.add_argument("-uuid", default="0b312e9f-068c-4943-a9ee-0e0911e31b21", help="The uuid")
parser.add_argument("-id_type", default="1", help="The type  of ID")
parser.add_argument("-test", default="1", help="is testing, 1: True, 0: False")
args = parser.parse_args()


if __name__ == '__main__':
    print("Starting request to media service API...")
    url = 'http://0.0.0.0:5000/media_service'
    info = {"uuid": args.uuid, "id_type": args.id_type, "test": args.test}
    r = requests.post(url, data=info)
    print(r.json())

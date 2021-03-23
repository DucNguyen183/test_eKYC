import requests
import json
from time import time
import argparse

parser = argparse.ArgumentParser(description='List of face matching version, uuid and testing flag')
parser.add_argument("-version", default="face_matching", help="face_matching or face_matching_v2")
parser.add_argument("-uuid", default= "0b312e9f-068c-4943-a9ee-0e0911e31b21", help="The uuid")
parser.add_argument("-test", default="1", help="is testing, 1: True, 0: False")
args = parser.parse_args()


if __name__ == '__main__':
    version = args.version
    print("Starting request to {} API...".format(version))
    url = 'http://0.0.0.0:5000/{}'.format(version)
    uuid = args.uuid
    test = args.test
    info = {"uuid": uuid, "test": test}
    r = requests.post(url, data=info)
    print(r.json())
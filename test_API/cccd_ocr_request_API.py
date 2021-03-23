import requests
import json
from time import time
import argparse

parser = argparse.ArgumentParser(description='List of images path')
parser.add_argument("-front", default= "./test/1.jpg", help="The path to front image")
parser.add_argument("-back", default= "./test/2.jpg", help="The path to back image")
args = parser.parse_args()


if __name__ == '__main__':
    print("Starting request to cccd ocr API...")
    url = 'http://0.0.0.0:5000/cccd_ocr'
    files = {'front': open(args.front, 'rb'),
             'back': open(args.back, 'rb')}
    r = requests.post(url, files=files)
    print(r.json())

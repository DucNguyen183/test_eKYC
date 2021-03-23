import requests
import json
from time import time
import argparse

parser = argparse.ArgumentParser(description='List of images path')
parser.add_argument("-img1", default="./test/1.jpg", help="Path of ID image")
parser.add_argument("-img2", default="./test/3.jpg", help="Path of selfie image")
args = parser.parse_args()


if __name__ == '__main__':
    print("Starting request to face matching raw API...")
    url = 'http://0.0.0.0:5000/face_match_raw'
    files = {'img1': open(args.img1, 'rb'),
             'img2': open(args.img2, 'rb')}
    r = requests.post(url, files=files)
    print(r.json())

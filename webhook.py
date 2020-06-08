import requests
import json
import sys
from os import system

name = input('Enter name: ')
choice = input("What you want to post? (video/comment/livestream)")

def sendWebhook(text, name):
    url = input("Enter your webhook url: ")

    data = {}

    data["username"] = name
    data["content"] = text
    
    print(json.dumps(data))
    requests.post(url, data=json.dumps(data), headers={"Content-Type": "application/json"})

if choice == 'video':
    video = input("Your video: ")
    sendWebhook("@everyone " + name + " has uploaded a new video!\n" + video, name)
if choice == 'comment':
    comment = input("Your comment: ")
    sendWebhook("@everyone " + comment, name)
if choice == 'livestream':
    stream = input("Your livestream: ")
    sendWebhook("@everyone " + name + " is live on YouTube!\n" + stream, name)

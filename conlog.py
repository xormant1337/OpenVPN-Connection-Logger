import os
import requests
import json
import datetime
import time

webhook = 'https://discord.com/api/webhooks/962119261382393887/42fjfQ-k00M-g6DUVnk1kuqZzZYgtHCMwsdQPXGYSv6K6-oOpg5T8e3Di547n0aUBmSP'
true = 'true'
false = 'false'

while True:
    lmfao = os.popen(''' cat /var/log/syslog | grep -n "Incoming Data Channel" | wc -l ''').readline()
    lmfao2 = os.popen(''' cat /var/log/syslog | grep -n "Incoming Data Channel" ''').readline()
    if (int(lmfao)) >= 1:
        date = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M")
        webhookstuff = {
    "embeds": [
    {
      "title": "boobs",
      "url": "boobs",
      "color": 0xFF5733,
      "fields": [
        {
          "name": "boobs",
          "value": f"{lmfao2}",
          "inline": true
        },
        ],
      "author": {
        "name": "boobs",
        "url": "boobs",
        "icon_url": "boobs"
      },
      "footer": {
        "text": f"Client Connected • {date}",
      },
      "thumbnail": {
        "url": "boobs"
      }
    }
  ]
}
        headers = {'content-type': 'application/json'}
        requests.post(webhook, json.dumps(webhookstuff), headers=headers)
        os.system("truncate -s 0 /var/log/syslog")

    else:
        print("snooping connections")
        time.sleep(1.5)
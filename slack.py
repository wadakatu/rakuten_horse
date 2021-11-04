from config import CONFIG
import requests
import json
import traceback

class Slack:

    SLACK = CONFIG['slack']
    USER = CONFIG['slackUser']

    def start(self):
        requests.post(self.SLACK, data=json.dumps({
            "text": "<@" + self.USER + ">" + " " + '自動入金開始'
        }))

    def finish(self):
        requests.post(self.SLACK, data=json.dumps({
            "text": "<@" + self.USER + ">" + " " + '自動入金終了'
        }))

    def error(self):
        requests.post(self.SLACK, data=json.dumps({
            "text": "<@" + self.USER + ">" + " " + 'エラー発生！:' + traceback.format_exc()
        }))

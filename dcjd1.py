"""
cron: 30 7 * * * dcjd.py
new Env("微信小程序-东呈酒店")
env add dcjd_data
----更新记录----
1.01版本 自己修订可以跑一个CK
1.02版本 支持多CK
"""
import os
import json
import ApiRequest
from notify import send

title = '微信小程序-东呈酒店'


class dcjd(ApiRequest.ApiRequest):
    def __init__(self, data):
        super().__init__()
        self.sec.headers = {
            'Host': 'campaignapi.dossen.com',
            'Connection': 'keep-alive',
            'Dossen-Platform': 'WxMiniApp',
            'DOSSENSESSIONID': '6CE5FC8619ED4D5485CC9CE83C9CD3EC1709561843233',
            'access_token': data,
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 MicroMessenger/8.0.47(0x18002f2b) NetType/WIFI Language/zh_CN',
            'Content-Type': 'application/json',
            'Referer': 'https://servicewechat.com/wxa4b8c0bda7f71cfc/276/page-frame.html',
            'Accept-Language': 'zh-CN,zh',
        }

    def login(self):
        params = {
            'blackbox': 'nWPHd1709562305WnuAGSODaSa',
        }
        response = self.sec.get('https://campaignapi.dossen.com/selling/checkin/do', params=params, verify=False)
        if response.status_code == 200:
            rj = response.json()
            if rj['code'] == 0:
                msg = f"签到成功\n获得{rj['results']}积分！"
            else:
                msg = f"签到失败\n" + json.dumps(rj, ensure_ascii=False)
        else:
            msg = f"签到失败\n" + json.dumps(response.json(), ensure_ascii=False)

        print(msg)
        send(title, msg)


if __name__ == '__main__':
    tokens = os.getenv('DCJD_TOKENS').split(',')
    for token in tokens:
        dcjd_instance = dcjd(token.strip())
        dcjd_instance.login()
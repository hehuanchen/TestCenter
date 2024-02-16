import os
import logging
import requests

PUSH_TOKEN=os.environ.get("PUSH_TOKEN")
Test_title = 'testing'
Test_content = 'This is a test'

# 消息推送
def send_msg(title, content):
    if PUSH_TOKEN is None:
        return
    url = 'http://www.pushplus.plus/send'
    r = requests.get(url, params={'token': PUSH_TOKEN,
                                  'title': title,
                                  'content': content})
    logging.info(f'通知推送结果：{r.status_code, r.text}')


send_msg(Test_title, Test_content)

  

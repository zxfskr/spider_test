import json
import os
import time
import requests

root_path = "/home/zxfeng/git/project/spider_test/tutorial"


def main():
    # resp = requests.get("http://www.google.com", timeout=5)
    # print(resp)
    with open(root_path + "/test.json") as f:
        data = json.load(f)

    i = 0
    for tmp in data:
        time.sleep(1)
        headers = {
            'User-Agent': (
                'Mozilla/5.0 (Windows NT 10.0; WOW64) '
                'AppleWebKit/537.36 (KHTML, like Gecko) '
                'Chrome/51.0.2704.63 Safari/537.36'
            )
        }
        # proxies = {
        #     'http': 'http://127.0.0.1:12333',
        #     'https': 'http://127.0.0.1:12333'
        # }
        resp = requests.get(tmp["image_url"], headers=headers)
        if resp.status_code == 200:
            image_path = os.path.join(root_path, "image")
            if not os.path.exists(image_path):
                os.makedirs(image_path)
            tmp_file = os.path.join(image_path, "detail" + str(i) + ".jpg")
            i += 1
            with open(tmp_file, "wb") as f:
                f.write(resp.content)
        else:
            print(resp)


if __name__ == "__main__":
    main()

import requests

# TODO 简单付费代理的使用
# url = 'http://ip.hahado.cn/ip'
# proxy = {'http':'http://H211EATS9O5745KC:F8FFBC929EB7D5A7@http-cla.abuyun.com:9030'}
# response = requests.get(url=url,proxies=proxy)
# print(response.text)

# TODO 免费代理或者付费代理的使用

PROXY_POOL_URL = 'http://localhost:5555/random'


def get_proxy():
    try:
        response = requests.get(PROXY_POOL_URL)
        if response.status_code == 200:
            return response.text
    except ConnectionError:
        return None

def ceshi():
    daili = get_proxy()
    proxies = {
        "http": "http://"+daili,
    }
    try:
        response = requests.get('http://httpbin.org/get', proxies=proxies)
        if response.status_code == 200:
            print(response.text)
    except ConnectionError:
        return None


if __name__ == '__main__':
    ceshi()

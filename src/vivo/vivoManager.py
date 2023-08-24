import http.client
import ssl

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    conn = http.client.HTTPSConnection("api-de-dev.myrightone.com")
    payload = ''
    headers = {
        'ali-env-mark': 'dev-googleapi',
        'x-isuda-profile-access-token': '[1,2]',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Accept': '*/*',
        'Host': 'api-de-dev.myrightone.com',
        'Connection': 'keep-alive'
    }
    conn.request("GET", "/api/admin/attr/ads/google-delivery-datas?startDate=2023-08-18&entDate=2023-08-18&sign=123",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))

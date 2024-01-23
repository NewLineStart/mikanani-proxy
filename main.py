import requests
import uvicorn
from fastapi import FastAPI, Response
from lxml import etree
import os


run_host = "0.0.0.0"
run_port = 9115
# 内网代理的ip（梯子的）
proxy_ip = ''
host_name = ''

app = FastAPI()

mikan_base_url = "https://mikanani.me/RSS/MyBangumi?token="
mikan_token = ""
user_token = ""

mikan_url = f"{mikan_base_url}{mikan_token}"


@app.get("/")
def root(token: str):
    if token != user_token:
        return {}
    content = requests.get(mikan_url, proxies=proxies, timeout=30).content
    doc = etree.fromstring(content)

    links = doc.xpath("//enclosure")
    print(len(links), "links")

    for link in links:
        url = link.get("url")
        url = url.replace(
            "https://mikanani.me",
            f"{host_name}/get?token={user_token}&link=https://mikanani.me",
        )
        link.set("url", url)

    content = etree.tostring(doc)
    return Response(content, media_type="application/xml")


@app.get("/get")
def get(token: str, link: str):
    if token != user_token:
        return {}
    response = requests.get(link, proxies=proxies, timeout=30)
    media_type = response.headers.get("Content-Type")
    return Response(response.content, media_type=media_type)


if __name__ == "__main__":
    proxy_ip = os.environ.get('proxy_ip') if not proxy_ip else proxy_ip
    host_name = os.environ.get('host_name') if not host_name else host_name
    mikan_token = os.environ.get('mikan_token') if not mikan_token else mikan_token
    user_token = os.environ.get('user_token') if not user_token else user_token
    proxies = {"http": proxy_ip, "https": proxy_ip} if proxy_ip else None
    uvicorn.run(app, host=run_host, port=run_port)

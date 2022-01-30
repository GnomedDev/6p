from fastapi import FastAPI, Response, Request
import ipaddress
import aiohttp
import random
from dotenv import load_dotenv
import os

load_dotenv()

IPV6_BLOCK = os.getenv("IPV6_BLOCK")

def get_random_ipv6():
    network = ipaddress.IPv6Network(IPV6_BLOCK)
    size = int(network[-1]) - int(network[0]) + 1 
    random_index = random.randint(0, size)
    return str(network[random_index])

app = FastAPI()

@app.get("/{url:path}")
async def root(request: Request, url: str):
    headers = dict(request.headers)
    headers.pop("host", None)
    headers.pop("Host", None)

    if not IPV6_BLOCK:
        return Response(status_code=500, content="IPV6_BLOCK not set")

    connector = aiohttp.TCPConnector(local_addr=(get_random_ipv6(), 0))
    async with aiohttp.ClientSession(headers=headers, connector=connector) as session:
        async with session.get(url) as response:
            return Response(content=await response.read(), status_code=response.status)
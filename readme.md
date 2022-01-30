# 6p
incredibly simple IPv6 proxy

it's not perfect in any way, but it works 

## setup
```sh
git clone https://github.com/aleclol/6p
cd 6p
python3.9 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

you'll need to configure your ipv6 block on your own, and then either:
1. make an .env file and put `IPV6_BLOCK = <YOUR_IPV6_BLOCK>`
2. set your ipv6 block to the env var IPV6_BLOCK

## running
```sh
source .venv/bin/activate
uvicorn main:app --reload
```

## usage

just GET http://localhost:8000/https%3A%2F%2Fnginx.org

## warning
DO NOT EXPOSE THIS TO THE INTERNET AS THERE IS NO AUTHENTICATION AND IT WILL BE ABUSED BY MALICIOUS ACTORS

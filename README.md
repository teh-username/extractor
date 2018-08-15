# Extractor

HTTP body extractor based on [scapy](https://scapy.net/)

### Prerequisites

* Python 2.x
* [virtualenv](https://virtualenv.pypa.io/en/latest/)

### Installation

```bash
# clone repository
git clone https://gitlab.com/upd-samsung-nfv/extractor

cd extractor

# setup virtual env
virtualenv -p python venv

# install requirements
venv/bin/pip install -r requirements.txt

# run the extractor (sudo is required)
sudo ./venv/bin/python extractor.py

# sample curl
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://jsonplaceholder.typicode.com/posts
```

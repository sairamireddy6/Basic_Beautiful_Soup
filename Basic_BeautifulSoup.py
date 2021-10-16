from bs4 import BeautifulSoup
import requests

req = requests.get("https://sairamireddy.000webhostapp.com/")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title


for i in res:
    print(i)
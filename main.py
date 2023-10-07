import requests
from bs4 import BeautifulSoup

response = requests.get("https://bank.gov.ua/ua/markets/currency-market")

if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    #print(soup)
    soupList = soup.findAll("div", {"class": "row data-index"})
    #print(soupList)
    result= soupList[0].find("div", {"class": "value"})
    USD = float(result.text.replace(',', '.'))
    print(f"USD = {USD} UAH\n")
    while True:
        try:
            UAH = float(input("UAH amount to convert to USD - "))
            break
        except:
            print("Incorrect input")
    print(f"\n{UAH} UAH converted to {round(UAH / USD, 4)} USD")

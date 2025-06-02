import json
import requests
import time


class TRY():
    rates = list()

    def __init__(self, r):
        # if(TRY.rates[-1] != r):
        TRY.rates.append(r)

    def ls(self):
        # print("TRY: "+TRY.rates[e] for e in range(1, len(TRY.rates)))
        print(f"TRY: {TRY.rates}")


class USD():
    rates = list()

    def __init__(self, r):
        # if(USD.rates[-1] != r):
        USD.rates.append(r)

    def ls(self):
        # print("TRY: "+TRY.rates[e] for e in range(1, len(TRY.rates)))
        print(f"USD: {USD.rates}")


class RUB():
    rates = list()

    def __init__(self, r):
        # if(RUB.rates[-1] != r):
        RUB.rates.append(r)

    def ls(self):
        # print("TRY: "+TRY.rates[e] for e in range(1, len(TRY.rates)))
        print(f"RUB: {RUB.rates}")


class INR():
    rates = list()

    def __init__(self, r):
        # if(INR.rates[-1] != r):
        INR.rates.append(r)

    def ls(self):
        # print("TRY: "+TRY.rates[e] for e in range(1, len(TRY.rates)))
        print(f"INR: {INR.rates}")


class Factory():
    def getExchange(self, currency, rates):
        if currency == "TRY":
            return TRY(rates)
        elif currency == "USD":
            return USD(rates)  # abd doları
        elif currency == "RUB":
            return RUB(rates)  # rusya rublesi
        elif currency == "INR":
            return INR(rates)  # hindistan rupisi
        else:
            return None


def main(urlAPI):
    resp = requests.get(urlAPI)
    if(resp.ok is True):

        # print(resp.ok)
        data = resp.text
        jsonData = json.loads(data)
        parsedData = jsonData['rates']

        factory = Factory()
        # print(parsedData)

        for c in parsedData:
            f = factory.getExchange(c, parsedData[c])

        TRY.ls(f)
        USD.ls(f)
        RUB.ls(f)
        INR.ls(f)
    else:
        print(resp.ok)


if __name__ == '__main__':
    for i in range(3):
        # time.sleep(10)
        main("https://api.exchangeratesapi.io/latest")

import requests,json

def getCurrenceValueOfMoney(type):
  try:
     res = requests.get("https://api.hgbrasil.com/finance?key=c89b5f1f")
     if res.status_code==200:
        obj = json.loads(res.text)
        return False,obj["results"]["currencies"][type]["buy"]
     else: 
        return True,"Api fora do ar..."   
  except Exception as e:
     return True,e
  

def convertRealToDollar(real):
  err,ret = getCurrenceValueOfMoney("USD")
  print(f"O valor em dolares é {real*ret}")
  


def convertRealToEuro(real):
  err,ret = getCurrenceValueOfMoney("EUR")
  print(f"O valor em euros é {real*ret}")
  



real= float(input("Digite o valor em reais : "))
convertRealToDollar(real)
convertRealToEuro(real)
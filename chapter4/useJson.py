import json
from urllib.request import urlopen


def getCountry(ipAddress):
    response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode("utf-8")
    responseJson = json.loads(response)
    return responseJson.get("country_code")


print(getCountry("50.78.253.58"))

jsonString = '{"arrayOfNums":[{"number":0},{"number":1},{"number":2}],"arrayOfFruits":[{"fruit":"apple"},' \
             '{"fruit":"banana"},{"fruit":"pear"}]} '
jsonObj = json.loads(jsonString)
print(jsonObj.get("arrayOfNums"))
print(jsonObj.get("arrayOfNums")[0])
import requests
import re
from datetime import date

with requests.Session() as session:
    url = 'https://smsc.ru/login/'
    values = {'login': '',
          'psw': ''}

    session.get(url)
    session.post(url, data=values)

    today = date.today()
    d1 = today.strftime("%d.%m.%Y")
    url2 = "https://smsc.ru/smsops/?date1=%s&date2=&mcc=&mnc=&min=5&phone=&sender=&fmt=" % (d1)
    with session.get(url2) as response:
        operators = re.findall(r"(Теле2|МТС|Мегафон|Билайн) \(Россия\)<td>(\d+)<td>(\d+)<td>(\d+)<td>", response.text)
        summ = re.findall(r"align=left>Всего:<th>(\d+)<th>(\d+)<th>(\d+)<th>", response.text)
        summm = summ[0]
        print("Delivered", summm[1])
        print("NotDelivered", summm[2])
        print("Total", summm[0])
        for list in operators:
            print(list[0], list[2], list[3], list[1])

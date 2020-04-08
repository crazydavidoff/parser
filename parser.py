import requests
import re

with requests.Session() as session:
    url = ' https://sms.e-vostok.ru/main.php'
    values = {'login': '',
          'password': '',
          'Enter': 'Enter'}

    session.post(url, data=values)

    with session.get('https://sms.e-vostok.ru/bulk/archive/outgoing/') as response:
        sent = re.findall(r"			<strong>Отправлено частей SMS:</strong> (\d+)<br/>", response.text)
        delivered = re.findall(r"				<strong>Доставлено частей SMS:</strong> (\d+)</p><br/><div class=\"paging\"><p>", response.text)
        print("Sent: ", str(sent[0]))
        print("Delivered: ", str(delivered[0]))
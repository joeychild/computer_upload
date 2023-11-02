import webbrowser
import datetime
from datetime import date

d = 0

while d < 16:
    date = datetime.datetime.strptime(str(date.today()),"%Y-%m-%d") + datetime.timedelta(days=21)
    url = "https://www.united.com/ual/en/us/flight-search/book-a-flight/results/rev?f=SFO&t=PVG&d=" + date + "&tt=1&sc=7&px=1,2,,,,,,&taxng=1&idx=1")
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    
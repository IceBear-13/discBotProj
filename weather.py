from requests_html import HTMLSession

def get_weather(str):
    s = HTMLSession()
    
    url = f'https://www.google.com/search?q=weather+{str}'
    
    r = s.get(url, headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "Accept-Language": "en-US,en;q=0.5"})
    
    temp = r.html.find('span#wob_tm', first=True).text
    
    return temp


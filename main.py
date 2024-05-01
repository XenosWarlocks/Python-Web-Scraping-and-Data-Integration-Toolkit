import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

#Add the desired UNI website
url = ""

def visit_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            dd_tags = soup.find_all('dd')
            with open('extracted_text.txt', 'w', encoding='utf-8') as file:
                for dd in dd_tags:
                    a_tags = dd.find_all('a', href=True)
                    for a in a_tags:
                        text = a.get_text(strip=True)
                        file.write(text + '\n')
        else:
            print("Failed to retrieve page. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Error:", e)

visit_page(url)


import requests
from bs4 import BeautifulSoup

def scrape_table_td(url, table_selector=None):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()      
        soup = BeautifulSoup(response.content, 'html.parser')   
        if table_selector:
            table = soup.select_one(table_selector)
        else:
            table = soup.find('table')        
        if not table:
            print("Таблица не найдена")
            return []        
        data = []
        rows = table.find_all('tr')       
        for row in rows:
            cells = row.find_all(['td', 'th'])
            if cells:
                row_data = [cell.get_text(strip=True) for cell in cells]
                data.append(row_data)        
        return data        
    except Exception as e:
        print(f"Ошибка: {e}")
        return []
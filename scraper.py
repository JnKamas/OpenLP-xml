import requests
from bs4 import BeautifulSoup

def get_paragraphs():
    url = "http://spevnik.szm.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        soup = BeautifulSoup(response.content, 'html.parser')
        
        paragraphs = []
        for paragraph in soup.find_all('p'):
            text = paragraph.get_text().strip()
            if text:
                paragraphs.append(text)
        
        return paragraphs[2:453] # this may vary since more songs can be added

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

if __name__ == "__main__":
    paragraphs = get_paragraphs()
    
    if paragraphs:                                                                                                                    
        for paragraph in paragraphs:
            print(f"{paragraph}\n")
    else:
        print("No paragraphs found on the webpage.")
from requests import get
from bs4 import BeautifulSoup


def GrabTwisted(url:str="https://dandys-world-robloxhorror.fandom.com/wiki/Daily_Twisted_Board") -> str:
    response = get(url)

    soup = BeautifulSoup(response.text, "html.parser")
    web_text = soup.get_text()

    target_text = "the board is occupied by"
    index_start = web_text.find(target_text)
    index_end = web_text.find('.', index_start)

    return web_text[index_start:index_end+1]
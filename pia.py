from bs4 import BeautifulSoup
import sys

html = sys.stdin.read()
parsed=BeautifulSoup(html, "html.parser")
print(parsed.head.find('meta', attrs={'http-equiv':'refresh'})['content'].split("; url=")[-1])

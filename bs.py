from bs4 import BeautifulSoup
import re
import sys

html = sys.stdin.read()
parsed = BeautifulSoup(html, "html.parser")
if len(sys.argv) > 1:
    print(eval(sys.argv[1]))

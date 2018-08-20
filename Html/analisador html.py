
from bs4 import BeautifulSoup
import urllib.request

with urllib.request.urlopen('Relatorio de Professores.html') as response:
   webpage = response.read()
   soup = BeautifulSoup(webpage,'html.parser')
   for anchor in soup.find_all('a'):
       print(anchor.get('href', '/'))
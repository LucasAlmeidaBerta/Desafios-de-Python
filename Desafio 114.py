import urllib.error
import urllib.request
try:
    urllib.request.urlopen('http://pudim.com.br/')
except urllib.error.URLError:
    print('\033[31mNão consegui acessa o Site Pudim!\033[m')
else:
    print('\033[32m o Site está no ar e operante!\033[m')

"""import webbrowser
try:
    webbrowser.open("http://pudim.com.br/")
except:
    print('\033[31mNão consegui acessa o Site Pudim!\033[m')
else:
    print('\033[32m o Site está no ar e operante!\033[m')
"""
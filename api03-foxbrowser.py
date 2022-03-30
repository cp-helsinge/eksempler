import sys
import requests
from PyQt5.Qt import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtWidgets import QApplication

#
# Husk at installere ovenstaaende python plugins (requests, pyqt5, qtwebenginewidget)
#
# Inspiration fra:
# https://stackoverflow.com/questions/63102395/displaying-web-page-with-pyqt5-webengine
# https://www.youtube.com/watch?v=hpc5jyVpUpw
#

get_content = requests.get("http://randomfox.ca/floof")
content = get_content.json()
url = content['image']

app = QApplication(sys.argv)

web = QWebEngineView()
web.load(QUrl(url))
web.show()

sys.exit(app.exec_())

import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sqlite3

# Initialize SQLite database
conn = sqlite3.connect('browser_history.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS history (url TEXT)''')
conn.commit()

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.browser.urlChanged.connect(self.update_url_bar)

        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        self.addToolBar(navtb)

        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navtb.addAction(forward_btn)

        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.url_bar)

    def update_url_bar(self, q):
        self.url_bar.setText(q.toString())

    def navigate_home(self):
        self.browser.setUrl(QUrl("https://www.google.com"))

    def navigate_to_url(self):
        url = self.url_bar.text()
        if url.lower().startswith('http://') or url.lower().startswith('https://'):
            self.browser.setUrl(QUrl(url))
            cursor.execute("INSERT INTO history (url) VALUES (?)", (url,))
            conn.commit()
        else:
            self.browser.setUrl(QUrl("http://" + url))
            cursor.execute("INSERT INTO history (url) VALUES (?)", ("http://" + url,))
            conn.commit()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("PyBrowser")

    window = WebBrowser()
    window.show()

    app.exec_()

    conn.close()
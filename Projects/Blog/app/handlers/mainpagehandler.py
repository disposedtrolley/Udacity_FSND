from app.handlers.basehandler import *


class MainPage(BlogHandler):
    def get(self):
        self.write("Hello, Udacity!")

from app.handlers.basehandler import *


class Profile(BlogHandler):
    def get(self, username):
        self.render("profile.html", username=username)

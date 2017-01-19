from app.handlers.basehandler import *


class ProfileHandler(BlogHandler):
    def get(self, username):
        self.render("profile.html", username=username)

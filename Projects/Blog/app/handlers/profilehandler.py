from app.handlers.basehandler import *


class ProfileHandler(BlogHandler):
    def get(self, username):
        if User.by_name(username):
            self.render("profile.html", username=username)
        else:
            self.redirect("/blog")

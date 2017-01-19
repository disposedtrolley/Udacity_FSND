from app.handlers.basehandler import *


class BlogFrontHandler(BlogHandler):
    def get(self):
        posts = greetings = Post.all().order("-created")
        user_cookie_id = self.read_secure_cookie("user_id")
        if self.user:
            self.render("home.html", posts=posts)
        else:
            self.render("home.html", posts=posts)

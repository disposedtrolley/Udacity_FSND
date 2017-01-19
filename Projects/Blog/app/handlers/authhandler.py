from app.handlers.basehandler import *


class LoginHandler(BlogHandler):
    def get(self):
        self.render("login.html")

    def post(self):
        username = self.request.get("username")
        password = self.request.get("password")

        u = User.login(username, password)
        if u:
            self.login(u)
            self.redirect("/blog")
        else:
            msg = "Invalid login"
            self.render("login.html", error=msg)


class LogoutHandler(BlogHandler):
    def get(self):
        self.logout()
        self.redirect("/blog")

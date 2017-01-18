import os
import jinja2
import webapp2
from google.appengine.ext import db

import validate
import hash
import database as my_db


template_dir = os.path.join(os.path.dirname(__file__), 'templates')

jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class WelcomePage(Handler):
    def get(self):
        # check for cookies
        user_cookie_str = self.request.cookies.get('user_id')
        if user_cookie_str:
            # validate cookie
            cookie_val = hash.check_secure_val(user_cookie_str)
            if cookie_val:
                # retrieve username from database
                user = my_db.User.get_by_id(long(cookie_val))

                # show welcome page with username
                self.render("welcome.html",
                            username=user.username)
            else:
                self.redirect("/blog/signup")
        else:
            self.redirect("/blog/signup")


class SignupPage(Handler):
    def write_form(self, valid_username="", valid_password="", valid_verify="", valid_email="",
                   username="", email=""):
        self.render("registration.html",
            valid_username = valid_username,
            valid_password = valid_password,
            valid_verify = valid_verify,
            valid_email = valid_email,
            username = username,
            email = email)

    def get(self):
        self.write_form(valid_username=True,
                        valid_password=True,
                        valid_verify=True,
                        valid_email=True)

    def post(self):
        # get user input
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        # validate user input
        valid_username = validate.verify_username(username)
        valid_password = validate.verify_password(password)
        valid_verify = validate.verify_verify(password, verify)
        valid_email = validate.verify_email(email)

        # re-render the form with errors if invalid data entered
        if not (valid_username and valid_password and valid_verify and valid_email):
            self.write_form(valid_username=valid_username,
                            valid_password=valid_password,
                            valid_verify=valid_verify,
                            valid_email=valid_email,
                            username=username,
                            email=email)
        else:
            # hash password
            password_hashed = hash.make_pw_hash(username, password)
            # add user to the database
            new_user = my_db.User(username=username, password=password_hashed)
            new_user.put()
            user_id = str(new_user.key().id())
            # make cookie value
            new_user_cookie = str(hash.make_secure_val(user_id))
            # set cookie
            self.response.headers.add_header("Set-Cookie", "user_id=%s; Path=%s" % (new_user_cookie, "/"))
            # redirect to welcome page
            self.redirect("/blog/welcome")


class LoginPage(Handler):
    def write_form(self, valid_login=""):
        self.render("login.html", valid_login=valid_login)

    def get(self):
        self.write_form(valid_login=True)

    def post(self):
        # get credentials
        username = self.request.get("username")
        password = self.request.get("password")
        # validate username and password
        user = self.find_user(username)
        if user:
            # validate password
            if hash.valid_pw(username, password, user.password):
                # set cookie and redirect to welcome page
                user_id = str(user.key().id())
                new_user_cookie = str(hash.make_secure_val(user_id))
                self.response.headers.add_header("Set-Cookie", "user_id=%s; Path=%s" % (new_user_cookie, "/"))
                self.redirect("/blog/welcome")
            else:
                # re-render login page with error
                self.write_form(valid_login=False)
        else:
            # re-render login page with error
            self.write_form(valid_login=False)

    def find_user(self, username):
        """Function searches the database for a given username.
        Returns the user instance if found, and None otherwise.
        """
        all_users = db.GqlQuery("SELECT * FROM User")
        for user in all_users:
            if user.username == username:
                return user
        return None


class LogoutPage(Handler):
    def get(self):
        # clear cookie and redirect to signup page
        self.response.headers.add_header("Set-Cookie", "user_id=%s; Path=%s" % ("", "/"))
        self.redirect("/blog/signup")


app = webapp2.WSGIApplication([
    ("/blog/signup", SignupPage),
    ("/blog/welcome", WelcomePage),
    ("/blog/login", LoginPage),
    ("/blog/logout", LogoutPage)
    ],
    debug=True)

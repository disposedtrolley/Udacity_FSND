import os
import re

import jinja2
import webapp2

template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)

USER_RE = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
PASS_RE = re.compile(r"^.{3,20}$")
EMAIL_RE = re.compile(r"^[\S]+@[\S]+.[\S]+$")

def verify_username(username):
    """Verifies usernames based on a regular expression.

    Args:
        username (string): The username entered by the user.

    Returns:
        boolean: Verification result.

    """
    return USER_RE.match(username) is not None

def verify_password(password):
    """Verifies passwords based on a regular expression. Also checks if
        original password and verification passwords are identical.

    Args:
        password (string): The password entered by the user.
        verify (string): The verification password entered by the user.

    Returns:
        boolean: Verification result.

    """
    return PASS_RE.match(password) is not None

def verify_verify(password, verify):
    """Verifies that the password and verifiction password are identical.

    Args:
        password (string): The password entered by the user.
        verify (string): The password verification entered by the user.

    Returns:
        boolean: Verification result.

    """
    return password == verify

def verify_email(email):
    """Verifies email addresses based on a regular expression.

    Args:
        email (string): The email address entered by the user.

    Returns:
        boolean: Verification result. Also returns True if the email is blank.

    """
    return EMAIL_RE.match(email) is not None or not email


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
        username = self.request.get("username")
        self.render("welcome.html",
                username=username)


class MainPage(Handler):
    def write_form(self, valid_username="", valid_password="", valid_verify="", valid_email="",
                   username="", email=""):
        self.render("user_signup.html",
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
        username = self.request.get("username")
        password = self.request.get("password")
        verify = self.request.get("verify")
        email = self.request.get("email")

        valid_username = verify_username(username)
        valid_password = verify_password(password)
        valid_verify = verify_verify(password, verify)
        valid_email = verify_email(email)

        if not (valid_username and valid_password and valid_verify and valid_email):
            self.write_form(valid_username=valid_username,
                            valid_password=valid_password,
                            valid_verify=valid_verify,
                            valid_email=valid_email,
                            username=username,
                            email=email)
        else:
            self.redirect("/welcome?username=" + username)

app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/welcome', WelcomePage)
    ],
    debug=True)

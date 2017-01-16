import os
import string

import jinja2
import webapp2

template_dir = os.path.dirname(__file__)
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


def rotate(data, n):
    """Function takes a string input consisting of letters of the alphabet
    and shifts each letter by n.
    Solution from
        http://stackoverflow.com/questions/1185775/using-a-caesarian-cipher-on-a-string-of-text-in-python

    """
    alphabet = list("abcdefghijklmopqrstuvwxyz")

    n = n % len(alphabet)
    target = alphabet[n:] + alphabet[:n]

    translation = dict(zip(alphabet, target))
    result = ""
    for c in data:
        if translation.has_key(c):
            result += translation[c]
        else:
            result += c
    return result


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

class MainPage(Handler):
    def get(self):
        self.render("rot13.html")
    def post(self):
        text = self.request.get("text")
        text = rotate(text, 13)
        self.render("rot13.html", text = text)

app = webapp2.WSGIApplication([
    ('/rot13', MainPage)
    ],
    debug=True)

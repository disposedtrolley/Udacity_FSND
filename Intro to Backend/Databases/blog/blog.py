import os

import jinja2
import webapp2

from google.appengine.ext import db

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
                               autoescape = True)


class Post(db.Model):
    """This class defines the data model for blog posts.
    """
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))


class MainPage(Handler):
    """Handler class for the home page of the blog.
    """
    def render_front(self, posts=""):
        self.render("front.html", posts=posts)

    def get(self):
        """
        Retrieves all blog posts from the database sorted in descending order
        of creation date, and calls the render function to display the page.
        """
        all_posts = db.GqlQuery("SELECT * FROM Post "
                                "ORDER BY created DESC")
        self.render_front(posts=all_posts)


class NewPostPage(Handler):
    """Handler class for the new post page.
    """
    def render_new(self, subject="", content="", error=""):
        self.render("new.html", subject=subject, content=content, error=error)

    def get(self):
        self.render_new()

    def post(self):
        """Retreives and validates the user's input. If both subject and
        content provided, redirects to the permalink for the blog post,
        otherwise re-renders the form with an error message.
        """
        post_subject = self.request.get("subject")
        post_content = self.request.get("content")
        if not post_subject or not post_content:
            error = "subject and content, please!"
            self.render_new(post_subject, post_content, error)
        else:
            new_post = Post(subject=post_subject, content=post_content)
            new_post.put()
            post_id = new_post.key().id()
            self.redirect("/blog/post/" + str(post_id))


class PostPage(Handler):
    """Handler class for the permalink post pages.
    """
    def render_post(self, post=""):
        self.render("post.html", post=post)

    def get(self, post_id):
        """Retrieves the Post object in the datastore corresponding to the
        id captured from the URL. Returns a 404 if the link is invalid,
        otherwise renders the blog post permalink page.
        """
        post_id = long(post_id)
        post = Post.get_by_id(post_id)

        if not post:
            self.error(404)
            return

        self.render_post(post)


app = webapp2.WSGIApplication([
    ('/blog', MainPage),
    ('/blog/newpost', NewPostPage),
    ('/blog/post/(\d+)', PostPage)
    ],
    debug=True)

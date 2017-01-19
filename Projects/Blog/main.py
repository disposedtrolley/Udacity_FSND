import webapp2

from app.models.post import Post
from app.models.comment import Comment
from app.models.user import User

from app.handlers.basehandler import BlogHandler
from app.handlers.mainpagehandler import MainPage
from app.handlers.blogfronthandler import BlogFront
from app.handlers.posthandler import PostPage, NewPost
from app.handlers.authhandler import Login, Logout
from app.handlers.welcomehandler import Welcome
from app.handlers.profilehandler import Profile
from app.handlers.signuphandler import Signup

app = webapp2.WSGIApplication([("/", MainPage),
                               ("/blog/?", BlogFront),
                               ("/blog/post/([0-9]+)", PostPage),
                               ("/blog/newpost", NewPost),
                               ("/blog/signup", Signup),
                               ("/blog/login", Login),
                               ("/blog/logout", Logout),
                               ("/blog/welcome", Welcome),
                               ("/blog/profile/(\w+)", Profile)
                               ],
                              debug=True)

from google.appengine.ext import db


class Post(db.Model):
    subject = db.StringProperty(required=True)
    content = db.TextProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)
    last_modified = db.DateTimeProperty(auto_now=True)
    author = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, pid):
        return Post.get_by_id(int(pid))

    @classmethod
    def by_username(cls, username):
        p = Post.all().filter('author = ', username)
        return p
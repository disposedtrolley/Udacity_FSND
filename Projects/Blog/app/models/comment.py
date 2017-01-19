from google.appengine.ext import db


class Comment(db.Model):
    post_id = db.StringProperty(required=True)
    username = db.StringProperty(required=True)
    comment = db.StringProperty(required=True)
    created = db.DateTimeProperty(auto_now_add=True)

    @classmethod
    def by_id(cls, cid):
        return Comment.get_by_id(cid)

    @classmethod
    def by_username(cls, username):
        q = Comment.all().filter('username = ', username)
        q.order('-created')
        return q

    @classmethod
    def by_post_id(cls, pid):
        c = Comment.all().filter("post_id = ", pid)
        if c:
            c.order("-created")
        else:
            c = None
        return c

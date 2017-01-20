from google.appengine.ext import db


class Like(db.Model):
    post_id = db.StringProperty(required=True)
    username = db.StringProperty(required=True)

    @classmethod
    def by_id(cls, lid):
        return Like.get_by_id(int(lid))

    @classmethod
    def by_username(cls, username):
        l = Like.all().filter('username = ', username)
        return l

    @classmethod
    def by_post_id(cls, pid):
        l = Like.all().filter("post_id = ", pid)
        return l

    @classmethod
    def by_post_id_uid(cls, pid, uid):
        """Checks if the currently logged in user has liked the post they're
        viewing.
        RETURNS SINGLE ENTITY
        """
        l = Like.all().filter("post_id = ", pid) \
            .filter("username = ", uid).get()
        return l

    @classmethod
    def by_post_id_ex_uid(cls, pid, uid):
        """Gets likes of this post by users other than currently logged in user.
        """
        l = Like.all().filter("post_id = ", pid) \
            .filter("username != ", uid)
        return l

    @classmethod
    def by_post_id_ex_uid_num(cls, pid, uid):
        """As above but returns the number of likes.
        """
        n_l = 0
        l = cls.by_post_id_ex_uid(pid, uid)
        if l:
            for x in l:
                n_l += 1
        return n_l

    @classmethod
    def by_post_id_num(cls, pid):
        n_l = 0
        l = cls.by_post_id(pid)
        if l:
            for x in l:
                n_l += 1
        return n_l

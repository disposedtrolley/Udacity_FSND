from app.handlers.basehandler import *


class PostPageHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)

        if post:
            comments = Comment.by_post_id(post_id)
            like_self = None
            like_others = None
            if self.user:
                like_self = Like.by_post_id_uid(post_id, self.user.name)
                like_others = Like.by_post_id_ex_uid_num(post_id, self.user.name)
            self.render("post.html", post=post, comments=comments,
                        like_self=like_self, like_others=like_others)
        else:
            self.redirect("/blog")


class NewPostHandler(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/blog/login")

    def post(self):
        if not self.user:
            self.redirect("/blog")

        subject = self.request.get("subject")
        content = self.request.get("content")

        if subject and content:
            p = Post(subject=subject, content=content,
                     author=self.user.name)
            p.put()
            self.redirect("/blog/post/%s" % str(p.key().id()))
        else:
            error = "Please enter subject and content."
            self.render("newpost.html", subject=subject, content=content,
                        error=error)

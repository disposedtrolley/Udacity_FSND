from app.handlers.basehandler import *


class PostPageHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)

        if post:
            comments = Comment.by_post_id(post_id)
            self.render("post.html", post=post, comments=comments)
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

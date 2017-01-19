from app.handlers.basehandler import *


class PostPage(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)

        comments = Comment.by_post_id(post_id)

        if not self.post:
            self.error(404)
            return

        self.render("post.html", post=post, comments=comments)

    def post(self, post_id):
        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)
        comment_text = self.request.get("comment")
        if comment_text:
            new_comment = Comment(post_id=post_id, username=self.user.name,
                                  comment=comment_text)
            new_comment.put()
            self.redirect("/blog/post/%s" % post_id)
        else:
            self.render("post.html", post=post,
                        error="Comment can't be empty!")


class NewPost(BlogHandler):
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
            error = "subject and content, please!"
            self.render("newpost.html", subject=subject, content=content,
                        error=error)
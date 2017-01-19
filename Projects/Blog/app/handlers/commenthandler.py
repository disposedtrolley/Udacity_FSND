from app.handlers.basehandler import *


class CommentHandler(BlogHandler):
    def get(self):
        self.redirect("/blog")

    def post(self):
        referrer = self.request.referer
        post_id = referrer.split("/")[-1]

        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)

        comment_text = self.request.get("comment")
        self.write(comment_text)
        if comment_text:
            new_comment = Comment(post_id=post_id, username=self.user.name,
                                  comment=comment_text)
            new_comment.put()
            self.redirect(referrer)
        else:
            # @TODO should alert uset with error
            self.redirect(referrer)

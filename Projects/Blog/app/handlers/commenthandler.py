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


class EditCommentHandler(BlogHandler):
    def post(self, post_id, comment_id):
        comment = Comment.by_id(int(comment_id))
        if self.user and self.user.name == comment.username:
            save_clicked = self.request.get("save")
            cancel_clicked = self.request.get("cancel")
            delete_clicked = self.request.get("delete")

            edited_comment = self.request.get("comment")

            if save_clicked:
                self.save_edit(edited_comment, comment, post_id)
            elif cancel_clicked:
                self.cancel_edit(post_id)
            elif delete_clicked:
                self.delete_edit(comment, post_id)
            else:
                self.redirect("/blog")
        else:
            self.redirect("/blog")

    def save_edit(self, edited_comment, comment, post_id):
        if edited_comment:
            comment.comment = edited_comment
            comment.put()
            self.redirect("/blog/post/%s" % post_id)
        else:
            self.write("error")

    def cancel_edit(self, post_id):
        self.redirect("/blog/post/%s" % post_id)

    def delete_edit(self, comment, post_id):
        comment.delete()
        self.redirect("/blog/post/%s" % post_id)

from app.handlers.basehandler import *


class PostPageHandler(BlogHandler):
    def get(self, post_id):
        key = db.Key.from_path("Post", int(post_id))
        post = db.get(key)

        if post:
            comments = Comment.by_post_id(post_id)
            if self.user:
                like_self = Like.by_post_id_uid(post_id,
                                                self.user.name)
                like_others_num = Like.by_post_id_ex_uid_num(post_id,
                                                             self.user.name)
                like_others = Like.by_post_id(post_id)
                username = self.user.name
                self.render("post.html",
                            post=post,
                            comments=comments,
                            like_self=like_self,
                            like_others_num=like_others_num,
                            like_others=like_others, username=username)
            else:
                self.render("post_unauthed.html", post=post, comments=comments)
        else:
            self.redirect("/blog")


class NewPostHandler(BlogHandler):
    def get(self):
        if self.user:
            self.render("newpost.html")
        else:
            self.redirect("/blog/login")

    def post(self):
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


class EditPostHandler(BlogHandler):
    def get(self, post_id):
        post = Post.get_by_id(int(post_id))
        if self.user and self.user.name == post.author:
            self.render("editpost.html", post=post)
        else:
            self.redirect("/blog")

    def post(self, post_id):
        post = Post.get_by_id(int(post_id))

        edited_subject = self.request.get("subject")
        edited_content = self.request.get("content")

        save_clicked = self.request.get("save")
        delete_clicked = self.request.get("delete")

        if save_clicked:
            self.save_edit(edited_subject, edited_content, post, post_id)
        elif delete_clicked:
            self.delete_edit(post)
        else:
            self.redirect("/blog")

    def save_edit(self, edited_subject, edited_content, post, post_id):
        if edited_subject and edited_content:
            post.subject = edited_subject
            post.content = edited_content
            post.put()
            self.redirect("/blog/post/%s" % post_id)
        else:
            error = "Please enter subject and content."
            self.render("editpost.html", post={"subject": edited_subject,
                                               "content": edited_content},
                        error=error)

    def delete_edit(self, post):
        post.delete()
        self.redirect("/blog")

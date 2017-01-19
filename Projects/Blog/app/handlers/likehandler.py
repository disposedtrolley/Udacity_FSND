from app.handlers.basehandler import *


class LikeHandler(BlogHandler):

    def post(self):
        referrer = self.request.referer
        post_id = referrer.split("/")[-1]

        # if existing like, delete like from db
        like = Like.by_post_id_uid(post_id, self.user.name)
        if like:
            like.delete()
        else:
            # add Like to database
            new_like = Like(username=self.user.name,
                            post_id=post_id)
            new_like.put()
        self.redirect(referrer)

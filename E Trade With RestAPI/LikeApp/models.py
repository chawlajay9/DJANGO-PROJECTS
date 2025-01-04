from django.db import models
from CommentApp.models import ModelComment
from django.conf import settings


class CommentLikeModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        verbose_name="User",
        help_text="User"
    )
    comment = models.ForeignKey(
        ModelComment,
        on_delete=models.CASCADE,
        verbose_name="Comment",
        help_text="Comment",
        related_name="likes"
    )

    def __str__(self):
        return f"{self.user} -> {self.comment}"

    class Meta:
        verbose_name = "CommentLike"
        verbose_name_plural = "CommentsLikes"
        db_table = "CommentsLikes"

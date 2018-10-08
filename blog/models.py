from django.db import models
from django.utils import timezone


class Post(models.Model):
    # Link to 'auth.User'
    # ON DELETE CASCADE: deletes the object containing the ForeignKey.
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        # DB에 저장
        self.save()

    # Print할 때 self.title이 print됨
    def __str__(self):
        return self.title


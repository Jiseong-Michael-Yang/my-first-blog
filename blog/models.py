from django.conf import settings
from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    """Properties"""
    # (Foreign) Links to other models; 
    # when the referenced object is deleted, objected that have references will also be deleted
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # Text field with length
    title = models.CharField(max_length=200)

    # Text field without length
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now
        )
    
    published_date = models.DateTimeField(
        # The field is not required
        blank=True, 

        # Blank value will be stored as null in the DB
        null=True
        )

    """Methods"""
    def publish(self):
        # published_date will be saved as of now when the post is published
        self.published_date = timezone.now()

        # Save the post
        self.save()

    # __str__ is the method that returns the title of the post
    def __str__(self):
        return self.title    

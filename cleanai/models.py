from django.db import models

class Image(models.Model):
    """Add documentation"""
    file = models.ImageField(
        upload_to='%s-%a-%t', 
        blank=True, 
        null=False,
    )
    
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    def __str__(self):
        return f"{self.created_at}"

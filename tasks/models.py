from djongo import models

class Task(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Pendiente'),
        ('IN_PROGRESS', 'En Proceso'),
        ('COMPLETED', 'Completada'),
    ]

    title = models.CharField(max_length=200)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    _id = models.ObjectIdField(primary_key=True)

    def __str__(self):
        return self.title
    
    class Meta:
        abstract = False
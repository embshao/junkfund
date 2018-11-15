from django.db import models
from django.utils import timezone

STATUS_CHOICES = (
    ('REJECTED', 'rejected'),
    ('APPROVED', 'approved'),
    ('PENDING', 'pending'),
)

class Candidate(models.Model):
    name = models.CharField(max_length=60, unique=True)
    project_name = models.CharField(max_length=60, unique=True)
    project_objective = models.TextField()
    target_audience = models.TextField()
    revenue_model = models.TextField()
    project_age = models.CharField(max_length=60, unique=True)
    contact_details = models.TextField()
    submission_date = models.DateField(default=timezone.now)
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return self.name
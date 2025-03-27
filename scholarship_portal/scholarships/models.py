from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    is_student = models.BooleanField(default=True)  # Default all users to students

    def __str__(self):
        return self.username

class Scholarship(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    eligibility_criteria = models.TextField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    deadline = models.DateField()

    class Meta:
        verbose_name_plural = "Scholarships"

    def __str__(self):
        return self.name

class Application(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name="applications")
    scholarship = models.ForeignKey(Scholarship, on_delete=models.CASCADE, related_name="applications")
    statement = models.TextField(help_text="Explain why you are eligible for this scholarship")
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Pending')
    applied_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Applications"

    def __str__(self):
        return f"{self.student.username} - {self.scholarship.name} ({self.status})"

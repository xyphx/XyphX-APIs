from django.db import models

class Apply(models.Model):
    name = models.CharField(max_length=100)
    org_name = models.CharField(max_length=100)
    tech_interest = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    portfolio = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'applications' 

    def __str__(self):
        return self.name

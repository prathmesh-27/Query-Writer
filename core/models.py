from django.db import models

class QueryHistory(models.Model):
    explanation = models.TextField()
    sql_output = models.TextField()
    db_type = models.CharField(max_length=50)
    model_used = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.explanation[:30]} - {self.timestamp}"
from django.db import models


class Task(models.Model):
    content = models.TextField(blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    class Meta:
        ordering = ["is_completed"]

    def __str__(self):
        return f"{self.content} - {self.created_date} - {self.is_completed}"


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

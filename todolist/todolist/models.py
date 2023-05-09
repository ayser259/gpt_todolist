from django.db import models

class UrgencyLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class PriorityLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class AvoidanceLevel(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=255)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    priority_level = models.ForeignKey(PriorityLevel, on_delete=models.CASCADE, null=True, blank=True)
    urgency_level = models.ForeignKey(UrgencyLevel, on_delete=models.CASCADE, null=True, blank=True)
    avoidance_level = models.ForeignKey(AvoidanceLevel, on_delete=models.CASCADE, null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, blank=True)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def delete_task(self):
        self.status = False
        self.save()


        
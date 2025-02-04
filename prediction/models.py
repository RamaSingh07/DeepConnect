from django.db import models

class Prediction(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    total_bilirubin = models.FloatField()
    direct_bilirubin = models.FloatField()
    alkaline_phosphotase = models.FloatField()
    sgot = models.FloatField()
    albumin = models.FloatField()
    protime = models.FloatField()
    cirrhosis_risk = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    # def __str__(self):
    #     return f"Prediction for {self.age} years old ({self.gender})"

    def __str__(self):
        return f"Prediction {self.id} - {self.age} years old"

class Volunteer(models.Model):
        name = models.CharField(max_length=100)
        email = models.EmailField()
        phone = models.CharField(max_length=15)
        role = models.CharField(max_length=50, choices=[
            ('Awareness Campaigns', 'Awareness Campaigns'),
            ('Fundraising', 'Fundraising'),
            ('Patient Support', 'Patient Support'),
            ('Research Assistance', 'Research Assistance')
        ])
        availability = models.CharField(max_length=20, choices=[
            ('Weekdays', 'Weekdays'),
            ('Weekends', 'Weekends'),
            ('Flexible', 'Flexible')
        ])
        message = models.TextField()
        submitted_at = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return f"{self.name} - {self.role}"



class SignupNew(models.Model):  # ✅ New name (avoids conflicts)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')])
    email = models.EmailField(unique=True)
    message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name





class Feedback(models.Model):
    FEEDBACK_CHOICES = [
        ('bug', 'Bug Report'),
        ('suggestion', 'Suggestion'),
        ('general', 'General Inquiry'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    feedback_type = models.CharField(max_length=20, choices=FEEDBACK_CHOICES)
    rating = models.IntegerField()
    comments = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)  # Stores timestamp

    def __str__(self):
        return f"{self.name} - {self.feedback_type} ({self.rating}/5)"

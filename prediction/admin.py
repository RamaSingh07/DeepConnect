from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import Prediction
from .models import Feedback
from .models import Volunteer
from .models import SignupNew

admin.site.register(Prediction)


@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'feedback_type', 'rating', 'submitted_at')
    search_fields = ('name', 'email', 'feedback_type')

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'role', 'availability', 'submitted_at')
    search_fields = ('name', 'email', 'role')
    list_filter = ('role', 'availability')

@admin.register(SignupNew)
class SignupNewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age', 'gender', 'message', 'created_at')  # ✅ Fields to display
    search_fields = ('name', 'email', 'gender')  # ✅ Search by name, email, gender
    list_filter = ('gender', 'created_at')
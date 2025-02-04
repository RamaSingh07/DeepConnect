from django.contrib import admin
from django.urls import path
from prediction import views  # Import views from the prediction app

urlpatterns = [
    path('', views.home, name='home'),# Root URL
    # path('', include('prediction.urls')),
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('hospital/', views.hospital_view, name='hospital'),  # Define the correct path
    path('predict/', views.predict, name='predict'),
    path('result/', views.result, name='result'),
    path('feedback/', views.feedback, name='feedback'),
    path("thankyou/", lambda request: render(request, "frontend/testing/thankyou.html"), name="thankyou"),
    path("volunteer/", views.volunteer_view, name="volunteer"),
    # path('user-signup/', views.user_signup, name='user_signup'),
    # path("user_thankyou/", lambda request: render(request, "frontend/testing/user_thankyou.html"), name="user_thankyou"),



# ✅ Add URLs for Information & Support
    path('information-support/', views.information_support, name='information_support'),
    path('liver-health/', views.liver_health, name='liver_health'),
    path('liver-conditions/', views.liver_conditions, name='liver_conditions'),
    path('liver-transplant/', views.liver_transplant, name='liver_transplant'),
    path('liver-cancer/', views.liver_cancer, name='liver_cancer'),
    path('liver_living/', views.liver_living, name='liver_living'),
    path('liver-love/', views.liver_love, name='liver_love'),
    path('liver-events/', views.liver_events, name='liver_events'),
    path('liver-publications/', views.liver_publications, name='liver_publications'),
    path('liver-care/', views.liver_care, name='liver_care'),
    path('liver-support/', views.liver_support, name='liver_support'),

    # ✅ How You Can Help
    path('how-you-can-help/', views.how_you_can_help, name='how_you_can_help'),
    path('donate/', views.donate, name='donate'),
    path('fundraise/', views.fundraise, name='fundraise'),
    path('leave-gift/', views.leave_gift, name='leave_gift'),
    path('corporate/', views.corporate, name='corporate'),
    path('raise-awareness/', views.raise_awareness, name='raise_awareness'),
    path('volunteering/', views.volunteering, name='volunteering'),
    path('Healthcare/', views.Healthcare, name='Healthcare'),
    path('other-ways/', views.other_ways, name='other_ways'),

    # ✅ Healthcare Professionals
    path('healthcare-professionals/', views.healthcare_professionals, name='healthcare_professionals'),
    path('resources-share/', views.resources_share, name='resources_share'),
    path('resources-care/', views.resources_care, name='resources_care'),
    path('helpus-healthcare/', views.helpus_healthcare, name='helpus_healthcare'),
    path('liver-disease-healthcare/', views.liver_disease_healthcare, name='liver_disease_healthcare'),
    path('research-healthcare/', views.research_healthcare, name='research_healthcare'),
    path('volunteer-form/', views.volunteer_form, name='volunteer_form'),


    # ✅ About Us
    path('about-us/', views.about_us, name='about_us'),
    path('our-strategy/', views.our_strategy, name='our_strategy'),
    path('who-we-are/', views.who_we_are, name='who_we_are'),
    path('what-we-do/', views.what_wedo, name='what_wedo'),
    path('media-centre/', views.media_centre, name='media_centre'),

    # ✅ Latest News & Blog
    path('latest', views.latest, name='latest'),
    path('parliamentary/', views.parliamentary, name='parliamentary'),
    path('love-liver-month/', views.love_liver_month, name='love_liver_month'),
    path('staying-warm/', views.staying_warm, name='staying_warm'),
    path('liver-disease-spotlight/', views.liver_disease_spotlight, name='liver_disease_spotlight'),
]




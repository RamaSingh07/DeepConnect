import joblib
from django.http import JsonResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
import pickle
import numpy as np
from .models import Prediction
from .models import Volunteer
from .models import Feedback
from .models import SignupNew







# Load the trained model
model_path = 'ml_model/random_forest_model.pkl'
model = joblib.load(model_path)


# Add a new home view
# def home(request):
#     return HttpResponse("Welcome to the Liver Cirrhosis Prediction System!")


def home(request):
    return render(request, 'index.html')

# def signup(request):
#    return render(request, 'signup.html')

def hospital_view(request):
    return render(request, 'frontend/testing/hospital_links.html')

def feedback(request):
    return render(request, 'frontend/testing/feedback.html')

def predict(request):
    return render(request, 'frontend/testing/predict.html')

def result(request):
    return render(request, 'frontend/testing/result.html')

def volunteer_form(request):
    return render(request, 'frontend/testing/volunteering_form.html')



# ✅ Information & Support Views
def information_support(request):
    return render(request, 'frontend/testing/navbar/information_support.html')

def liver_health(request):
    return render(request, 'frontend/testing/infor/liver_health.html')

def liver_conditions(request):
    return render(request, 'frontend/testing/infor/liver_conditions.html')

def liver_transplant(request):
    return render(request, 'frontend/testing/infor/liver_transplant.html')

def liver_cancer(request):
    return render(request, 'frontend/testing/infor/liver_cancer.html')

def liver_living(request):
    return render(request, 'frontend/testing/infor/liver_living.html')

def liver_love(request):
    return render(request, 'frontend/testing/infor/liver_love.html')

def liver_events(request):
    return render(request, 'frontend/testing/infor/liver_events.html')

def liver_publications(request):
    return render(request, 'frontend/testing/infor/liver_publications.html')

def liver_care(request):
    return render(request, 'frontend/testing/infor/liver_care.html')

def liver_support(request):
    return render(request, 'frontend/testing/infor/liver_support.html')

# ✅ How You Can Help Views
def how_you_can_help(request):
    return render(request, 'frontend/testing/navbar/how_you_can_help.html')

def donate(request):
    return render(request, 'frontend/testing/how u can help/Donate.html')

def fundraise(request):
    return render(request, 'frontend/testing/how u can help/fundraise.html')

def leave_gift(request):
    return render(request, 'frontend/testing/how u can help/Leave_gift.html')

def corporate(request):
    return render(request, 'frontend/testing/how u can help/corporate.html')

def raise_awareness(request):
    return render(request, 'frontend/testing/how u can help/raise_awareness.html')

def volunteering(request):
    return render(request, 'frontend/testing/how u can help/volunteering.html')

def Healthcare(request):
    return render(request, 'frontend/testing/how u can help/Healthcare.html')

def other_ways(request):
    return render(request, 'frontend/testing/how u can help/other_ways.html')


# ✅ healthcare_professionals
def healthcare_professionals(request):
    return render(request, 'frontend/testing/navbar/Healthcare_professionals.html')

def resources_share(request):
    return render(request, 'frontend/testing/Healthcare_professional/resources_share.html')

def resources_care(request):
    return render(request, 'frontend/testing/Healthcare_professional/resources_care.html')

def helpus_healthcare(request):
    return render(request, 'frontend/testing/Healthcare_professional/helpus_healthcare(professional).html')

def liver_disease_healthcare(request):
    return render(request, 'frontend/testing/Healthcare_professional/liver_disease(healthcare_professional).html')

def research_healthcare(request):
    return render(request, 'frontend/testing/Healthcare_professional/research(healthcare_professional).html')


#  ✅ About Us Views
def about_us(request):
    return render(request, 'frontend/testing/navbar/about_us.html')

def our_strategy(request):
    return render(request, 'frontend/testing/About_us/our_strategy.html')

def who_we_are(request):
    return render(request, 'frontend/testing/About_us/who_we_are.html')

def what_wedo(request):
    return render(request, 'frontend/testing/About_us/what_wedo.html')

def media_centre(request):
    return render(request, 'frontend/testing/About_us/media_centre.html')

# ✅ Latest News & Blog Views
def latest(request):
    return render(request, 'frontend/testing/navbar/latest.html')

def parliamentary(request):
    return render(request, 'frontend/testing/latest_news/parliamentary.html')

def love_liver_month(request):
    return render(request, 'frontend/testing/latest_news/love_liver_month.html')

def staying_warm(request):
    return render(request, 'frontend/testing/latest_news/staying_warm.html')

def liver_disease_spotlight(request):
    return render(request, 'frontend/testing/latest_news/liver_disease_spotlight.html')




# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('predict')
#     else:
#         form = UserCreationForm()
#     return render(request, 'signup.html', {'form': form})
#
#

# def predict(request):
#     if request.method == 'POST':
#         # Extract input features from the request (adjust keys as per your form)
#         try:
#             age = float(request.POST.get('age'))
#             gender = 1 if request.POST.get('gender') == 'Male' else 0  # Male = 1, Female = 0
#             total_bilirubin = float(request.POST.get('total_bilirubin'))
#             direct_bilirubin = float(request.POST.get('direct_bilirubin'))
#             alkaline_phosphotase = float(request.POST.get('alkaline_phosphotase'))
#             sgot = float(request.POST.get('sgot'))
#             albumin = float(request.POST.get('albumin'))
#             protime = float(request.POST.get('protime'))
#
#             # Create a feature array
#             features =np.array( [[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, sgot, albumin, protime]])
#
#
#             prediction = model.predict(features)[0]  # Classification result
#             probability = model.predict_proba(features)[0][1]
#
#         # Predict using the model
#             prediction = model.predict(features)
#
#         # Return the prediction as a response
#         # return JsonResponse({'cirrhosis_risk': int(prediction[0])})
#         #return render(request, "result.html", {"risk": cirrhosis_risk})
#             return render(request, "result.html", {"risk": probability, "prediction": prediction})
#         except Exception as e:
#             # Handle any errors during prediction
#             return render(request, "result.html", {"error": str(e)})
#     else:
#         # return JsonResponse({'error': 'Invalid request method'}, status=400)
#         return render(request, "frontend/testing/predict.html")

def predict(request):


    if request.method == 'POST':
        # Capture form data
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        total_bilirubin = request.POST.get('total_bilirubin')
        direct_bilirubin = request.POST.get('direct_bilirubin')
        alkaline_phosphotase = request.POST.get('alkaline_phosphotase')
        sgot = request.POST.get('sgot')
        albumin = request.POST.get('albumin')
        protime = request.POST.get('protime')

        if not all([age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, sgot, albumin, protime]):
            return render(request, 'frontend/testing/predict.html', {'error': "Please fill all fields."})

        try:
            age = float(age)
            gender = 1 if gender.lower() == 'male' else 0
            total_bilirubin = float(total_bilirubin)
            direct_bilirubin = float(direct_bilirubin)
            alkaline_phosphotase = float(alkaline_phosphotase)
            sgot = float(sgot)
            albumin = float(albumin)
            protime = float(protime)
        except ValueError:
            return render(request, 'frontend/testing/predict.html',
                          {'error': "Invalid input. Please enter valid numbers."})
        except Exception as e:
            return render(request, 'frontend/testing/predict.html', {'error': f"An error occurred: {str(e)}"})

        features = np.array(
            [[age, gender, total_bilirubin, direct_bilirubin, alkaline_phosphotase, sgot, albumin, protime]])

        # Predict using the model
        prediction = model.predict(features)[0]
        probability = model.predict_proba(features)[0][1] * 100
        cirrhosis_risk = probability

        # Optionally save to the database
        patient = Prediction(
            age=age,
            gender=gender,
            total_bilirubin=total_bilirubin,
            direct_bilirubin=direct_bilirubin,
            alkaline_phosphotase=alkaline_phosphotase,
            sgot=sgot,
            albumin=albumin,
            protime=protime,
            cirrhosis_risk=cirrhosis_risk
        )
        patient.save()

        if probability > 50:
            risk = "High Risk"
            risk_color = "red"
        elif probability > 20:
            risk = "Moderate Risk"
            risk_color = "orange"
        else:
            risk = "Low Risk"
            risk_color = "green"

        return render(request, "frontend/testing/result.html", {
            "risk": risk,
            "risk_color": risk_color,
            "probability": f"{probability:.2f}%",
            "prediction": "Positive" if prediction == 1 else "Negative"
        })

    return render(request, "frontend/testing/predict.html")





def feedback_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        feedback_type = request.POST.get("feedback_type")
        rating = request.POST.get("rating")
        comments = request.POST.get("comments")

        Feedback.objects.create(
            name=name,
            email=email,
            feedback_type=feedback_type,
            rating=int(rating),
            comments=comments
        )

        return JsonResponse({"success": True, "message": "Thank you for your feedback!"})

    return render(request, "feedback.html")
#
# def volunteer_view(request):
#     if request.method == "POST":
#         print("✅ POST request received!")  # Debugging
#
#         name = request.POST.get("name")
#         email = request.POST.get("email")
#         phone = request.POST.get("phone")
#         role = request.POST.get("role")
#         availability = request.POST.get("availability")
#         message = request.POST.get("message")
#
#         print(f"Received: {name}, {email}, {phone}, {role}, {availability}, {message}")  # Debugging
#
#         if not name or not email or not phone:
#             print("❌ Missing required fields!")  # Debugging
#             return JsonResponse({"success": False, "error": "Missing required fields"})
#
#         # Save to database
#         Volunteer.objects.create(
#             name=name,
#             email=email,
#             phone=phone,
#             role=role,
#             availability=availability,
#             message=message
#         )
#
#         print("✅ Volunteer saved successfully!")  # Debugging
#         return JsonResponse({"success": True, "message": "Thank you for volunteering!"})
#
#     return render(request, "volunteering_form.html")

def volunteer_view(request):
    if request.method == "POST":
        print("✅ POST request received!")  # Debugging

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        role = request.POST.get("role")
        availability = request.POST.get("availability")
        message = request.POST.get("message")

        print(f" Received Data: {name}, {email}, {phone}, {role}, {availability}, {message}")  # Debugging

        if not name or not email or not phone:
            print(" Missing required fields!")  # Debugging
            return JsonResponse({"success": False, "error": "Missing required fields"})

        # Save to database
        Volunteer.objects.create(
            name=name,
            email=email,
            phone=phone,
            role=role,
            availability=availability,
            message=message
        )

        print("✅ Volunteer saved successfully!")  # Debugging
        return JsonResponse({"success": True, "message": "Thank you for volunteering! We will get back to you soon."})

    return render(request, "volunteering_form.html")


def signup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Store data in the new model
        SignupNew.objects.create(
            name=name,
            age=age,
            gender=gender,
            email=email,
            message=message
        )

        return JsonResponse({"success": True, "message": "Thank you for signing up!"})

    return render(request, "signup.html")
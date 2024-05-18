from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
import os
from django.contrib.auth import logout
from .module import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login, logout



def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        if not all([name, email, subject, message]):
            error_message = 'Please fill in all fields.'
            return render(request, 'feedback.html', {'error_message': error_message})

        try:
            # Gửi email đến email của công ty
            send_mail(
                subject,
                f'Tên: {name}\nEmail: {email}\n\n{message}',
                'brainprojectbnk@gmail.com',
                ['brainprojectbnk@gmail.com'],
                fail_silently=False,
            )
            success_message = 'Your message has been sent successfully!'
            return render(request, 'feedback.html', {'success_message': success_message})
        except Exception as e:
            error_message = 'An error occurred while sending the message. Please try again later.'
            return render(request, 'feedback.html', {'error_message': error_message})

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    request.session['logged_in'] = False
    return redirect('/')  # Chuyển hướng sau khi đăng xuất

def prediction_view(request):
    if request.method == 'POST':
        prediction_method = request.POST.get('prediction_method')
        
        if not prediction_method:
            return render(request, 'prediction.html', {'msg': 'Please choose a prediction method.'})
        
        if prediction_method == '1':
            if 'image' not in request.FILES:
                return render(request, 'prediction.html', {'msg': 'Please upload an image for Prediction 1.'})
            
            image_file = request.FILES['image']
            image_path = 'myweb/static/userdata/test.jpg'
            
            if os.path.exists(image_path):
                os.remove(image_path)
            
            with open(image_path, 'wb+') as destination:
                for chunk in image_file.chunks():
                    destination.write(chunk)
            
            # Load and process the image
            image = load_image(image_path)
            result = prediction_1(image)
            diagnosis_type = 'Type 1 Diagnosis'
            prediction_type = 1
        
        elif prediction_method == '2':
            if 'image1' not in request.FILES or 'image2' not in request.FILES:
                return render(request, 'prediction.html', {'msg': 'Please upload both images for Prediction 2.'})
            
            image1_file = request.FILES['image1']
            image2_file = request.FILES['image2']
            image1_path = 'myweb/static/userdata/flair.nii'
            image2_path = 'myweb/static/userdata/t1ce.nii'
            
            if os.path.exists(image1_path):
                os.remove(image1_path)
            if os.path.exists(image2_path):
                os.remove(image2_path)
            
            with open(image1_path, 'wb+') as destination:
                for chunk in image1_file.chunks():
                    destination.write(chunk)
            
            with open(image2_path, 'wb+') as destination:
                for chunk in image2_file.chunks():
                    destination.write(chunk)
            
            
            result = prediction_2()
            diagnosis_type = 'Type 2 Diagnosis'
            prediction_type = 2
        
        else:
            return render(request, 'prediction.html', {'msg': 'Invalid prediction method'})
        
        # Save the result to the database if the user is authenticated
        if request.user.is_authenticated:
            PredictionResult.objects.create(
                user=request.user,
                prediction_method=prediction_method,
                result=result,
                diagnosis_type=diagnosis_type
            )
        
        return render(request, 'prediction.html', {'result': result, 'prediction_type': prediction_type})
    
    return render(request, 'prediction.html')
    

def verify_email(request, username):
    user = get_user_model().objects.get(username=username)
    user_otp = OtpToken.objects.filter(user=user).last()
    
    if request.method == 'POST':
        # valid token
        if user_otp.otp_code == request.POST['otp_code']:
            # checking for expired token
            if user_otp.otp_expires_at > timezone.now():
                user.is_active = True
                user.save()
                messages.success(request, "Account activated successfully!! You can Login.")
                return redirect("account_view")
            # expired token
            else:
                messages.warning(request, "The OTP has expired, get a new OTP!")
                return redirect("verify-email", username=user.username)
        # invalid otp code
        else:
            messages.warning(request, "Invalid OTP entered, enter a valid OTP!")
            return redirect("verify-email", username=user.username)
        
    context = {}
    return render(request, "verify_token.html", context)




def resend_otp(request):
    if request.method == 'POST':
        user_email = request.POST["otp_email"]
        
        if get_user_model().objects.filter(email=user_email).exists():
            user = get_user_model().objects.get(email=user_email)
            otp = OtpToken.objects.create(user=user, otp_expires_at=timezone.now() + timezone.timedelta(minutes=5))
            
            
            # email variables
            subject="Email Verification"
            message = f"""
                                Hi {user.username}, here is your OTP {otp.otp_code} 
                                it expires in 5 minute, use the url below to redirect back to the website
                                http://127.0.0.1:8000/verify-email/{user.username}
                                
                                """
            sender = "brainprojectbnk@gmail.com"
            receiver = [user.email, ]
        
        
            # send email
            send_mail(
                    subject,
                    message,
                    sender,
                    receiver,
                    fail_silently=False,
                )
            
            messages.success(request, "A new OTP has been sent to your email-address")
            return redirect("verify-email", username=user.username)

        else:
            messages.warning(request, "This email dosen't exist in the database")
            return redirect("resend-otp")
        
           
    context = {}
    return render(request, "resend_otp.html", context)



def account_view(request):
    form = RegisterForm()
    context = {"form": form}  # Khởi tạo context trước khi kiểm tra method

    if request.method == 'POST':
        if 'sign-in' in request.POST:
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
        
            if user is not None:    
                login(request, user)
                request.session['logged_in'] = True
                storage = messages.get_messages(request)
                storage.used = True
                return redirect('/')
            else:
                messages.warning(request, "Username or Password is incorrect! Try again.")
                return redirect("account_view")
        elif 'sign-up' in request.POST:
            # Xử lý đăng ký
            form = RegisterForm(request.POST)
            if form.is_valid():
                email = form.cleaned_data['email']
                username = form.cleaned_data['username']
                if CustomUser.objects.filter(email=email).exists():
                    messages.warning(request, "Email already exists")
                elif CustomUser.objects.filter(email=email, is_active=False).exists():
                    messages.warning(request, "Email not verified")
                else:
                    form.save()
                    messages.success(request, "Account created successfully! An OTP was sent to your Email")
                    return redirect("verify-email", username=request.POST['username'])
            else:
                if 'email' in form.errors:
                    messages.warning(request, "Invalid email format")
                if 'username' in form.errors:
                    messages.warning(request, "Invalid username format")
    return render(request, "account.html", {"form": form})


from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404
from .models import PredictionResult

def prediction_history_view(request):
    if request.user.is_authenticated:
        user = request.user
        predictions = PredictionResult.objects.filter(user=user).order_by('-created_at')
        return render(request, 'history.html', {'predictions': predictions})
    return redirect('/')
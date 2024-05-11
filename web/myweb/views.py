from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
import os

from .module import load_image, prediction

# Create your views here.
def abstract(request):
    context={}
    return render(request, 'abstract.html', context)

def contact(request):
    context={}
    return render(request, 'contact.html', context)

def dashboard(request):
    context={}
    return render(request, 'dashboard.html', context)

def index(request):
    context={}
    return render(request, 'index.html', context)

def preview(request):
    context={}
    return render(request, 'preview.html', context)

def upload(request):
    context={}
    return render(request, 'upload.html', context)

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        full_name = request.POST.get('full_name') 
        
        if User.objects.filter(username=username).exists():
            msg = "Username already exists"
            return render(request, 'signup.html', {'msg': msg})
        elif Customer.objects.filter(email=email).exists():
            msg = "Email already exists"
            return render(request, 'signup.html', {'msg': msg})
        else:
            # Tạo người dùng mới
            user = User.objects.create_user(username=username, email=email, password=password)
            
            # Tạo khách hàng mới và liên kết với người dùng tạo mới
            customer = Customer.objects.create(user=user, email=email, password=password, full_name=full_name)
            
            # Đăng nhập người dùng tự động sau khi đăng ký thành công
            user = authenticate(username=username, password=password) # type: ignore
            login(request, user)
            request.session['logged_in'] = True  # Thiết lập biến session để đánh dấu đã đăng nhập
            
            return redirect('/')  # Chuyển hướng đến trang chính sau khi đăng ký thành công
    else:
        return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)  
            request.session['logged_in'] = True  # Thiết lập biến session để đánh dấu đã đăng nhập

            return redirect('/')  # Chuyển hướng đến trang chính sau khi đăng nhập thành công
        else:
            msg = "Invalid username or password. Please try again."
            return render(request, 'login.html', {'msg': msg})
    else:
        return render(request, 'login.html')
    
def account(request):
    # Truy vấn thông tin khách hàng từ cơ sở dữ liệu
    if request.user.is_authenticated:
        customer = Customer.objects.get(user=request.user)
        return render(request, 'account.html', {'customer': customer})
    else:
        # Xử lý trường hợp người dùng chưa đăng nhập
        return render(request, 'login.html')  # Hoặc chuyển hướng đến trang đăng nhập

from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    request.session['logged_in'] = False
    return redirect('/')  # Chuyển hướng sau khi đăng xuất

def prediction_view(request):
    if request.method == 'POST' and request.FILES['image']:
        image_file = request.FILES['image']
        image_path = 'myweb/static/userdata/test.jpg'
        
        # Kiểm tra xem file test.jpg đã tồn tại chưa
        if os.path.exists(image_path):
            os.remove(image_path)  # Nếu tồn tại, xóa file cũ
        
        # Lưu file ảnh mới
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # Load ảnh và dự đoán
        image = load_image(image_path)
        result = prediction(image)
        # result = "ok"
        return render(request, 'prediction.html', {'result': result})
    
    return render(request, 'prediction.html')
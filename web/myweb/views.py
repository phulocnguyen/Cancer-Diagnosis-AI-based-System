from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import *
from django.http import HttpResponse
import os
from django.contrib.auth import logout
from .module import *



def home(request):
    context={}
    return render(request, 'home.html', context)

def account_view(request):
    msg = None
    if request.method == 'POST':
        if 'sign-in' in request.POST:
            # Xử lý đăng nhập
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                request.session['logged_in'] = True 
                return redirect('/')  # Chuyển hướng đến trang chính sau khi đăng nhập thành công
            else:
                msg = 'Invalid username or password'

        elif 'sign-up' in request.POST:
            # Xử lý đăng ký
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            full_name = request.POST['full_name']

            # Kiểm tra username đã tồn tại chưa
            if User.objects.filter(username=username).exists():
                msg = 'Username already exists'

            # Kiểm tra email đã tồn tại chưa
            elif User.objects.filter(email=email).exists():
                msg = 'Email already exists'

            else:
                # Tạo người dùng mới
                user = User.objects.create_user(username=username, email=email, password=password)
                
                # Tạo thông tin khách hàng mới
                customer = Customer.objects.create(user=user, email=email, full_name=full_name)
                
                # Đăng nhập người dùng mới tạo
                login(request, user)
                request.session['logged_in'] = True 
                return redirect('/')  # Chuyển hướng đến trang chính sau khi đăng ký thành công

    return render(request, 'account.html', {'msg': msg})

def logout_view(request):
    logout(request)
    request.session['logged_in'] = False
    return redirect('/')  # Chuyển hướng sau khi đăng xuất

def prediction_view(request):
    if request.method == 'POST':
        if 'image' not in request.FILES:
            return render(request, 'prediction.html', {'msg': 'error'})
        
        image_file = request.FILES['image']
        image_path = 'myweb/static/userdata/test.jpg'
        
        # Kiểm tra xem file test.jpg đã tồn tại chưa
        if os.path.exists(image_path):
            os.remove(image_path)  # Nếu tồn tại, xóa file cũ
        
        # Lưu file ảnh mới
        with open(image_path, 'wb+') as destination:
            for chunk in image_file.chunks():
                destination.write(chunk)
        
        # Load ảnh
        image = load_image(image_path)
        
        # Xác định phương pháp dự đoán từ form
        prediction_method = request.POST.get('prediction_method')
        if prediction_method == '1':
            result = prediction_1(image)
        elif prediction_method == '2':
            result = prediction_2(image)
        else:
            return render(request, 'prediction.html', {'msg': 'Invalid prediction method'})
        
        return render(request, 'prediction.html', {'result': result})
    else:
        return render(request, 'prediction.html')
# Brain Tumor Detection Using Deep Learning
# Thành viên
1. 22022547 Nguyễn Phú Lộc
2. 22022605 Nguyễn Duy Minh Lâm
3. 22022552 Trần Đức Đăng Khôi
4. 22022551 Bùi Ngọc Khánh
[Report và Demo]( https://drive.google.com/drive/folders/1YXsobF5helTy3xYGuaQnY7D3u5a6g63d?usp=sharing)
# Giới thiệu dự án
Mục đích của dự án này là xây dựng một website sử dụng mô hình Deep Learning để phân loại và phân vùng ung thư dựa trên hình ảnh. Website này sẽ cung cấp một giao diện thuận tiện cho người dùng, cho phép họ tải lên hình ảnh và nhận được kết quả phân loại từ mô hình. Việc triển khai thành công dự án này sẽ giúp tăng khả năng phát hiện sớm ung thư, hỗ trợ các bác sĩ và chuyên gia y tế trong việc đưa ra chẩn đoán chính xác hơn. Tuy nhiên, đây là một vấn đề nhạy cảm, hệ thống chỉ có vai trò hỗ trợ, không phải thay thế các bác sĩ trong việc chẩn đoán. Hệ thống website của chúng tôi được sử dụng để chẩn đoán bao gồm phân loại (Classification) và phân vùng (Segmentation) hình ảnh u não để cho ra kết quả dự đoán

## Getting Started

Dưới đây là một số hướng dẫn cách cài đặt và sử dụng phần mềm.

## To Install:

Cloning the Repository:

```
$ git clone https://github.com/phulocnguyen/Cancer-Diagnosis-AI-based-System.git

```

Installing the environment control:

```
$ pip install virtualenv

$ virtualenv env

```

Activating the environment:

on Windows:
```
env\Scripts\activate
```

Setup environment to run the app
```
$ pip install -r requirements.txt
```
Run the app
```
$ cd web
$ python manage.py runserver
```


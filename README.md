# Brain Tumor Detection Using Deep Learning
# Thành viên
1. 22022547 Nguyễn Phú Lộc
2. 22022605 Nguyễn Duy Minh Lâm
3. 22022552 Trần Đức Đăng Khôi
4. 22022551 Bùi Ngọc Khánh
   
[Report và Demo]( https://drive.google.com/drive/folders/1YXsobF5helTy3xYGuaQnY7D3u5a6g63d?usp=sharing)

# Giới thiệu dự án
Mục đích của dự án này là xây dựng một website sử dụng mô hình Deep Learning để phân loại và phân vùng ung thư dựa trên hình ảnh. Website này sẽ cung cấp một giao diện thuận tiện cho người dùng, cho phép họ tải lên hình ảnh và nhận được kết quả phân loại từ mô hình. Việc triển khai thành công dự án này sẽ giúp tăng khả năng phát hiện sớm ung thư, hỗ trợ các bác sĩ và chuyên gia y tế trong việc đưa ra chẩn đoán chính xác hơn. Tuy nhiên, đây là một vấn đề nhạy cảm, hệ thống chỉ có vai trò hỗ trợ, không phải thay thế các bác sĩ trong việc chẩn đoán. Hệ thống website của chúng tôi được sử dụng để chẩn đoán bao gồm phân loại (Classification) và phân vùng (Segmentation) hình ảnh u não để cho ra kết quả dự đoán

## Mô tả
Hệ thống chẩn đoán u não có 2 tác vụ chính là Classification và Segmentation.
Đối với tác vụ Classification, chúng tôi sử dụng mô hình Convolutional Neural Network để tiến hành trích xuất đặc điểm từ hình ảnh đầu vào và đưa ra nhãn chính xác. Mô hình hoạt động tốt với bộ dữ liệu mà chúng tôi tìm được với độ chính xác cao trên từng tập train/val/test lần lượt là 0.989/0.991/0.933
Đối với tác cụ Segmentation, chúng tôi sử dụng kiến trúc UNet bao gồm 2 thành phần chính là encoder và decoder. Mô hình cho kết quả khá chính xác, đảm bảo độ tin cậy khi sử dụng với bộ dữ liệu lớn.

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


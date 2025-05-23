Link báo cáo: https://www.overleaf.com/project/682ed96f06afd7a8a4edaa07
## Thiết lập và Cài đặt BackEnd
## 1. Sao chép kho lưu trữ:
```bash
   git clone https://github.com/nhannguyen92/spotify-clone-prj/tree/main.git
   cd backend
   ```
## 2. Tạo Môi Trường Ảo (Virtual Environment)
- Chạy lệnh sau:
  
```bash
  python -m venv myvenv
```
- Cho phép thực thi script trong PowerShell (Windows):
```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```
- Kích hoạt môi trường ảo:
```bash
    myvenv\Scripts\activate
```
## 3. Cài đặt Thư viện Cần Thiết
- Chạy:
```bash
  pip install -r requirements.txt
```
## 4. Cấu Hình Cơ Sở Dữ Liệu
- Cập nhật cấu hình cơ sở dữ liệu trong file settings.py bên trong thư mục spotify_clone_backend.
- Dự án sử dụng PostgreSQL làm cơ sở dữ liệu:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'spotify_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
## 5. Thực hiện Migrations
- Tạo file migration từ models::
```bash
    python manage.py makemigrations
```
- Áp dụng migrations vào cơ sở dữ liệu::
```bash
    python manage.py migrate
```
## 6. Tạo Tài Khoản Quản Trị (Superuser)
- Chạy:
```bash
    python manage.py createsuperuser
```
## 7. Tạo Dữ Liệu Mẫu Cục Bộ:
- Chạy script sau để tạo dữ liệu thử nghiệm:
```bash
  py seed_data.py
```
## 8. Chạy Server:
- Chạy:
```bash
    python manage.py runserver
```
## Thiết lập và Cài đặt FrontEnd
1. **Cài Đặt Các Gói Phụ Thuộc**:
   ```bash
   npm install
   ```
2. **Thiết Lập Tailwind CSS**:
   Đảm bảo file `tailwind.config.js` và `index.css` được cấu hình:
   ```css
   /* src/index.css */
   @tailwind base;
   @tailwind components;
   @tailwind utilities;
   ```
   Nếu chưa có, khởi tạo Tailwind:
   ```bash
   npx tailwindcss init
   ```

3. **Chạy Server Phát Triển**:
   ```bash
   npm start
   ```
   Ứng dụng sẽ mở tại `http://localhost:3000`.

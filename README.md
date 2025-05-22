Các phần mềm cần cài đặt:
    -WSL (Hệ thống con Windows dành cho Linux)
    -MongoDB được cài đặt và chạy trong WSL
    -Python(3.9+)
    -Visual Studio Code với tiện ích mở rộng WSL
*Cài đặt BACKEND:
    1 Cài đặt môi trường:
    Bước 1: Clone code từ Github
    – git clone [https://github.com/alixblu/spotify_clone_backend.git]
    – cd spotify_clone_backend
    Bước 2: Tạo môi trường ảo
    Thiết lập môi trường ảo để quản lý các phụ thuộc:
    python3 -m venv spotify_envi source spotify_envi/bin/activate
    Bước 3: Cài đặt các thư viện cần thiết
    pip install -r requirements.txt
    Bước 4: Thiết lập MongoDB
    – sudo apt update
    – sudo apt install mongodb
    – sudo systemctl start mongodb
    Bước 5: Cấu hình cơ sở dữ liệu trong Django
    Cập nhật tệp settings.py để sử dụng MongoDB
    DATABASES = ’default’: ’ENGINE’: ’djongo’, ’NAME’: ’spotify_clone_db’,
    2 Thiết lập ứng dụng:
    Tạo file .env tại thư mục gốc backend:
    38
    DEBUG = True
    SECRET_KEY = django - insecure - zbb ^ @6$ ^ lq ^ or + @ * gj0 & xr - w *1( yqzwuzhis3 &
    ,→ gc8 ) -3824 @2@
    DATABASE_URL = mongodb :// localhost :27017/ spotify
    SPOTIFY_CLIENT_ID =15 f6f63ea91341ca883077f84c45a285
    SPOTIFY_CLIENT_SECRET =57 bdcf24c96d477680d2b645dcc9ce39
    REDIRECT_URI = http ://127.0.0.1:5173/ callback
    3 Khởi chạy:
    Khởi động máy chủ phát triển Django
    – python manage.py makemigrations
    – python manage.py migrate
    – python manage.py runserver
*Cài đặt FRONTEND
     1 Cài đặt các thư viện cần thiết:
    Cài đặt các gói phụ thuộc, chạy lệnh sau để cài đặt tất cả các gói cần thiết:
    npm install
    Cài đặt các phần phụ thuộc (thư viện chính)
    npm install lucide-react react react-dom react-icons react-router-dom
    2 Khởi tạo Tailwind CSS:
    – npm install -D tailwindcss@3 postcss autoprefixer
    – npx tailwindcss init -p
    Thao tác này sẽ tạo ra tailwind.config.js và postcss.config.js.
    3 Khởi chạy:
    npm run dev

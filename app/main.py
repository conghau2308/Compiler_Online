from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- Nhớ thêm dòng này
from app.routes import files

app = FastAPI(title="CS COMPLIER AZURE")

# --- BẮT ĐẦU CẤU HÌNH CORS ---
origins = [
    "http://localhost:3000",        # Dành cho Next.js chạy ở máy tính của bạn
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],            # Cho phép mọi phương thức (GET, POST, PUT, DELETE)
    allow_headers=["*"],            # Cho phép mọi header
)
# --- KẾT THÚC CẤU HÌNH CORS ---

app.include_router(files.router)
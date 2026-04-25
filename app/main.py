from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware  # <-- Nhớ thêm dòng này
from app.routes import files

app = FastAPI(title="CS COMPLIER AZURE")

# --- BẮT ĐẦU CẤU HÌNH CORS ---
origins = [
    "https://frontend-compiler-beta.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://frontend-compiler-beta.vercel.app",
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# --- KẾT THÚC CẤU HÌNH CORS ---

app.include_router(files.router)
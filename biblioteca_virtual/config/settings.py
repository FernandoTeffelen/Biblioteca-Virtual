import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
            "DATABASE_URL",
            "postgresql://postgres:ySKhZEZJCNwHMY2i@db.nwynkxlzbcuwpumngigh.supabase.co:5432/postgres"  # fallback local
        )
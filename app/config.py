import os
from dotenv import load_dotenv
load_dotenv(r"C:\Users\Jaswanth\inventory-management\.env", override=True)
class Config:
    SQLALCHEMY_DATABASE_URI = (
    f"mysql+pymysql://{os.getenv('DB_USER').strip()}:{os.getenv('DB_PASSWORD').strip()}"
    f"@{os.getenv('DB_HOST').strip()}:4000/{os.getenv('DB_NAME').strip()}"
    f"?ssl_verify_cert=true&ssl_verify_identity=true"
)
    SQLALCHEMY_ENGINE_OPTIONS = {
    "connect_args": {
        "ssl": {
            "verify_cert": True,
            "verify_identity": True,
        },
        "autocommit": True,
    }
}
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #JWT
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY') 
    #mail
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.getenv('MAIL_USERNAME').strip()
    MAIL_PASSWORD = os.getenv('MAIL_PASSWORD').strip()


import os
from dotenv import load_dotenv

load_dotenv()

smtp_host=os.getenv("SMTP_HOST")
smtp_port=os.getenv("SMTP_PORT")
SMTP_USERNAME=os.getenv("SMTP_USERNAME")
SMTP_PASSWORD=os.getenv("SMTP_PASSWORD")


print(smtp_host)
print(smtp_port)
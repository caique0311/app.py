from dotenv import load_dotenv
import os

load_dotenv()
print("ENV =", os.getenv("GEMINI_API_KEY"))

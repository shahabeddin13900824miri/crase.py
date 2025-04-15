import shutil
import os

# مشخص کردن مسیر فایل و مقصد
source = r"C:\Users\shaha\OneDrive\Desktop\as\crase\crase.py"
destination = r"C:\Users\shaha\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup"

try:
    # کپی کردن فایل
    shutil.copy(source, destination)
    print("فایل با موفقیت کپی شد!")
except FileNotFoundError:
    print("فایل یا مسیر مشخص شده پیدا نشد.")
except Exception as e:
    print(f"خطایی رخ داد: {e}")

os.remove('routin.py')
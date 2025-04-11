import os
import requests

TOKEN = os.environ['TELEGRAM_TOKEN']
CHAT_ID = os.environ['TELEGRAM_CHAT_ID']
FILE_PATH = 'training_log_excelcharts.xlsx'

url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"
with open(FILE_PATH, 'rb') as file:
    files = {'document': file}
    data = {'chat_id': CHAT_ID}
    response = requests.post(url, files=files, data=data)

if response.status_code == 200:
    print("✅ Файл успешно отправлен в Telegram!")
else:
    print(f"❌ Ошибка: {response.status_code}")
    print(response.text)

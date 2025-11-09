# delete_webhook.py - Remove webhook to allow polling
import requests
from config import BOT_TOKEN

url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
params = {"drop_pending_updates": True}

print("🔧 Deleting webhook...")
response = requests.post(url, params=params)
data = response.json()

if data.get("ok"):
    print("✅ Webhook deleted successfully!")
    print("   Your Railway bot should work now.")
    print("\n   Restart your Railway deployment to apply changes.")
else:
    print(f"❌ Error: {data}")

# force_stop_bot.py - Force stop all bot instances
import requests
import time
from config import BOT_TOKEN

print("🔧 Force stopping all bot instances...\n")

# Step 1: Delete webhook (if any)
print("1️⃣ Deleting webhook...")
url = f"https://api.telegram.org/bot{BOT_TOKEN}/deleteWebhook"
params = {"drop_pending_updates": True}
response = requests.post(url, params=params)
if response.json().get("ok"):
    print("   ✅ Webhook deleted")
else:
    print("   ⚠️  No webhook to delete")

# Step 2: Get pending updates to clear queue
print("\n2️⃣ Clearing update queue...")
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getUpdates"
params = {"offset": -1, "timeout": 1}
response = requests.get(url, params=params)
if response.json().get("ok"):
    print("   ✅ Update queue cleared")
else:
    print(f"   ⚠️  {response.json()}")

# Step 3: Wait for other instances to timeout
print("\n3️⃣ Waiting for other instances to timeout (30 seconds)...")
for i in range(30, 0, -5):
    print(f"   ⏳ {i} seconds remaining...")
    time.sleep(5)

# Step 4: Check if we can connect now
print("\n4️⃣ Testing connection...")
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
response = requests.get(url)
if response.json().get("ok"):
    bot = response.json()["result"]
    print(f"   ✅ Bot is ready: @{bot['username']}")
    print("\n✅ All instances should be stopped now!")
    print("   You can restart Render service now.")
else:
    print(f"   ❌ Error: {response.json()}")

print("\n" + "="*50)
print("📋 Next Steps:")
print("1. Go to Render dashboard")
print("2. Click 'Manual Deploy' → 'Deploy latest commit'")
print("3. Wait 2 minutes")
print("4. Check logs for '200 OK' (not 409)")
print("5. Test bot: https://t.me/solarkh_bot")

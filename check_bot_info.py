# check_bot_info.py - Check bot status and webhook
import requests
from config import BOT_TOKEN

# Check webhook info
url = f"https://api.telegram.org/bot{BOT_TOKEN}/getWebhookInfo"
response = requests.get(url)
data = response.json()

print("🔍 Bot Webhook Status:")
print("=" * 50)

if data.get("ok"):
    info = data.get("result", {})
    webhook_url = info.get("url", "")
    
    if webhook_url:
        print(f"⚠️  WEBHOOK IS SET: {webhook_url}")
        print(f"   Last error: {info.get('last_error_message', 'None')}")
        print(f"   Pending updates: {info.get('pending_update_count', 0)}")
        print("\n❌ This is causing the conflict!")
        print("   Webhooks and polling (Railway) cannot run together.")
        
        # Offer to delete
        print("\n🔧 To fix, run: python delete_webhook.py")
    else:
        print("✅ No webhook set (Good!)")
        print("\n⚠️  The conflict is from another polling instance.")
        print("   Check:")
        print("   - Did you deploy to Render, PythonAnywhere, etc?")
        print("   - Is bot running on another computer?")
        print("   - Multiple Railway services?")
else:
    print(f"❌ Error: {data}")

# Check bot info
url2 = f"https://api.telegram.org/bot{BOT_TOKEN}/getMe"
response2 = requests.get(url2)
data2 = response2.json()

if data2.get("ok"):
    bot = data2.get("result", {})
    print("\n" + "=" * 50)
    print("🤖 Bot Information:")
    print(f"   Username: @{bot.get('username')}")
    print(f"   Name: {bot.get('first_name')}")
    print(f"   ID: {bot.get('id')}")
    print(f"   Can join groups: {bot.get('can_join_groups')}")

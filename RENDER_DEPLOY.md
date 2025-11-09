# 🚀 Deploy SolarKH Bot to Render

## Quick Deploy Guide

### Step 1: Create Render Account
1. Go to **https://render.com**
2. Click **"Get Started"**
3. Sign up with **GitHub** (recommended)

### Step 2: Deploy from GitHub

#### Option A: One-Click Deploy (Easiest)
1. Make sure your code is pushed to GitHub: `https://github.com/chhany007/solarkh_bot`
2. Go to Render Dashboard
3. Click **"New +"** → **"Background Worker"**
4. Click **"Connect account"** to link GitHub
5. Select repository: **`chhany007/solarkh_bot`**
6. Render will auto-detect settings from `render.yaml`
7. Click **"Create Background Worker"**
8. Wait ~2 minutes for deployment

#### Option B: Manual Configuration
If auto-detection doesn't work:

**Settings:**
- **Name**: `solarkh-bot`
- **Region**: Singapore (closest to Cambodia)
- **Branch**: `main`
- **Runtime**: Python 3
- **Build Command**: `pip install -r requirements.txt`
- **Start Command**: `python bot.py`
- **Plan**: Free

### Step 3: Verify Deployment

**Check Logs:**
1. Go to your service in Render
2. Click **"Logs"** tab
3. Look for: `✅ SolarKH Bot started successfully!`

**Test Bot:**
1. Open Telegram: https://t.me/solarkh_bot
2. Send: `/start`
3. Try: `/language` → Choose Khmer
4. Test: `/quote 300 0.15`

### Step 4: Stop Railway (Important!)

To avoid conflicts:
1. Go to **Railway Dashboard**
2. Find your `solarkh_bot` project
3. Click **Settings** → **Delete Service**
4. Or just click **"Stop"** to pause it

---

## ✅ Render Advantages

- **750 hours/month free** (vs Railway's 500)
- **No credit card required** for free tier
- **Better uptime** for free tier
- **Singapore region** (lower latency for Cambodia)
- **Auto-deploy** from GitHub

---

## 🔧 Troubleshooting

### Bot not responding?
- Check Render logs for errors
- Verify bot token in `config.py`
- Make sure Railway instance is stopped

### Build failed?
- Check `requirements.txt` is present
- Verify Python version compatibility
- Check Render build logs

### Still getting 409 Conflict?
- Stop ALL other instances (Railway, local, etc.)
- Run: `python delete_webhook.py`
- Restart Render service

---

## 📊 Monitoring

**View Logs:**
- Render Dashboard → Your Service → Logs

**Restart Bot:**
- Render Dashboard → Manual Deploy → Deploy latest commit

**Update Bot:**
```bash
git add .
git commit -m "Update bot"
git push origin main
```
Render auto-deploys!

---

## 💰 Free Tier Limits

- **750 hours/month** (enough for 24/7)
- **512 MB RAM**
- **0.1 CPU**
- **Sleeps after 15 min inactivity** (but wakes on Telegram message)

Perfect for a Telegram bot! 🎉

---

## 🆘 Need Help?

- Check logs in Render dashboard
- Verify GitHub repo is up to date
- Make sure only ONE instance is running
- Test with: `/start` in Telegram

Your bot: **@solarkh_bot**
Channel: **@solar_kh**

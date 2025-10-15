# Telegram Render Bot (Fixed Version)

✅ **Now compatible with Python 3.11 (no imghdr issue)**

## Files
- `app.py` — Flask webhook bot code
- `requirements.txt` — dependencies
- `runtime.txt` — ensures Render uses Python 3.11.9
- `Procfile` — start command for Render

## Deploy (Render)
1. Upload to GitHub
2. On Render → New Web Service → connect repo
3. Environment Variables:
   - `BOT_TOKEN` = your Telegram bot token
4. Deploy — Render will auto-detect Python 3.11
5. Set webhook:
   ```bash
   curl -F "url=https://<your-app>.onrender.com/webhook" https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook
   ```

Enjoy your working bot! 🎉

import requests
from datetime import datetime

# تنظیمات سرور هیدیفای
HIDDIFY_API_URL = "https://your-hiddify-server/api/v1/users"  # آدرس API سرور هیدیفای
API_TOKEN = "your_api_token"  # توکن API سرور

# لیست کانفیگ‌ها
configs = [
    {"user": "p1", "name": "💚@HIDDIFY_plas", "ip": "188.114.96.218", "port": 3581},
    {"user": "p2", "name": "💛@HIDDIFY_plas", "ip": "162.159.192.33", "port": 988},
    {"user": "p1", "name": "🧡@HIDDIFY_plas", "ip": "162.159.192.215", "port": 988},
]

# تابع برای دریافت اطلاعات از API
def get_user_usage(api_url, token):
    headers = {"Authorization": f"Bearer {token}"}
    try:
        response = requests.get(api_url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"خطا در اتصال به API: {e}")
        return None

# تابع برای نمایش اطلاعات
def display_usage(data, configs):
    if not data or "users" not in data:
        print("اطلاعاتی یافت نشد.")
        return
    
    # دیکشنری برای ذخیره اطلاعات کاربران
    user_data = {user["username"]: user for user in data.get("users", [])}
    
    for config in configs:
        username = config["user"]
        config_name = config["name"]
        
        if username not in user_data:
            print(f"کاربر {username} یافت نشد.")
            continue
        
        user_info = user_data[username]
        data_used = user_info.get("data_used", 0) / (1024 ** 3)  # تبدیل به گیگابایت
        last_seen = user_info.get("last_seen", "نامشخص")
        
        # محاسبه زمان فعال بودن
        if last_seen != "نامشخص":
            last_seen_time = datetime.fromisoformat(last_seen.replace("Z", "+00:00"))
            uptime = datetime.now() - last_seen_time
            uptime_str = f"{uptime.days} روز و {uptime.seconds//3600} ساعت"
        else:
            uptime_str = "نامشخص"
        
        print(f"کانفیگ: {config_name}")
        print(f"کاربر: {username}")
        print(f"حجم مصرف: {data_used:.2f} گیگابایت")
        print(f"زمان فعال بودن: {uptime_str}")
        print("-" * 30)

# اجرای برنامه
def main():
    usage_data = get_user_usage(HIDDIFY_API_URL, API_TOKEN)
    display_usage(usage_data, configs)

if __name__ == "__main__":
    main()

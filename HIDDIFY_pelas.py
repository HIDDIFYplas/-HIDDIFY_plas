import requests

# Server and config settings
HIDDIFY_API_URL = "https://your-hiddify-server/api/v2/users"  # Replace with your server API URL
API_TOKEN = "your_api_token"  # Replace with your server API token
CONFIGS = [
    {"user": "p1", "name": "💚@HIDDIFY_plas"},
    {"user": "p2", "name": "💛@HIDDIFY_plas"},
    {"user": "p1", "name": "🧡@HIDDIFY_plas"},
]

# Function to disable user
def disable_user(username):
    headers = {"Authorization": f"Bearer {API_TOKEN}", "Content-Type": "application/json"}
    url = f"{HIDDIFY_API_URL}/{username}"
    payload = {"active": False}  # Request to disable user
    try:
        response = requests.put(url, headers=headers, json=payload)
        response.raise_for_status()
        print(f"User {username} has been successfully disabled.")
    except requests.exceptions.RequestException as e:
        print(f"Error disabling user {username}: {e}")

# Function to manage and display usage
def manage_usage():
    MAX_DATA = 50  # Maximum data: 50 terabytes
    MAX_DAYS = 30  # Maximum uptime: 30 days

    for config in CONFIGS:
        username = config["user"]
        config_name = config["name"]
        
        # Simulated usage (can be replaced with real API data)
        data_used = 50  # Assume 50 terabytes used
        uptime_days = 30  # Assume 30 days active
        
        # Check limits
        status = "Active"
        if data_used >= MAX_DATA or uptime_days >= MAX_DAYS:
            status = "Disconnected"
            disable_user(username)  # Disable user
        
        print(f"Config: {config_name}")
        print(f"User: {username}")
        print(f"Data Usage: {data_used} terabytes")
        print(f"Uptime: {uptime_days} days")
        print(f"Status: {status}")
        print("-" * 20)

# Run the code
if __name__ == "__main__":
    manage_usage()

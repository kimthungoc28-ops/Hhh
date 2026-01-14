import gspread
from oauth2client.service_account import ServiceAccountCredentials

SHEET_NAME = "TikTok Gift Tracker"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive"
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "credentials.json", scope
)

client = gspread.authorize(creds)
sheet = client.open(SHEET_NAME)

gifts_db = sheet.worksheet("GIFTS_DB")
gift_log = sheet.worksheet("GIFT_LOG")

def load_gifts():
    data = gifts_db.get_all_records()
    return {row["Gift Name"]: row for row in data}

def add_new_gift(name, diamond, price, note):
    gifts_db.append_row([name, diamond, price, note])

def log_gift(data):
    gift_log.append_row([
        data["time"],
        data["user"],
        data["gift"],
        data["count"],
        data["diamond"],
        data["vnd"]
    ])

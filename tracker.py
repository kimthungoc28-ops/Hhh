from TikTokLive import TikTokLiveClient
from TikTokLive.events import GiftEvent
from datetime import datetime
import webbrowser

from sheet_manager import load_gifts, log_gift

client = TikTokLiveClient(unique_id="@USERNAME_TIKTOK")

@client.on("gift")
async def on_gift(event: GiftEvent):

    gifts = load_gifts()
    gift_name = event.gift.name

    if gift_name not in gifts:
        webbrowser.open("http://localhost:5000/new_gift")
        return

    gift = gifts[gift_name]
    vnd = int(gift["Price VND"]) * event.gift.count

    data = {
        "time": datetime.now().strftime("%H:%M:%S"),
        "user": event.user.nickname,
        "gift": gift_name,
        "count": event.gift.count,
        "diamond": event.gift.diamond_count,
        "vnd": vnd
    }

    log_gift(data)
    print("Logged:", data)

client.run()

from phantom.core.clients import phantom
from telethon import events
from time import time
import socket
from datetime import datetime

start_time = datetime.now()

async def get_ping(host="8.8.8.8", port=53, timeout=3):
    try:
        start = time()
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        end = time()
        sock.close()
        ping_time = int(round((end - start) * 1000, 2))
        return f"{ping_time}ms"
    except socket.error:
        return "Ping failed"
    
@phantom.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def ping_handler(event):
    start = time()
    await event.edit("🏓 Pinging..")
    end = time()
    ping = await get_ping()
    latency = int((end - start) * 1000)
    uptime = (datetime.now() - start_time)
    uptime_str = str(uptime).split(".")[0]
    await event.edit(f"🏓 Pong!\nPing: {ping}\nLatency: {latency}ms\nUptime: {uptime_str}")
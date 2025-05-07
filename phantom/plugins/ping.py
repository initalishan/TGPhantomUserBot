from phantom.core.clients import phantom
from telethon import events
from time import time
import socket

async def get_ping(host="8.8.8.8", port=53, timeout=3):
    try:
        start = time()
        socket.setdefaulttimeout(timeout)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        end = time()
        sock.close()
        ping_time = round((end - start) * 1000, 2)
        return f"{ping_time}ms"
    except socket.error:
        return "Ping failed"
    
@phantom.on(events.NewMessage(outgoing=True, pattern=r"\.ping"))
async def ping_handler(event):
    latency = time()
    await event.edit("Pinging..")
    latency = time()
    ping = await get_ping()
    await event.edit(f"Pong!\nPing: {ping}\nLatency: {latency}")
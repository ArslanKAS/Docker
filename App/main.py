# 1. Import Libraries
import json
import uvicorn
from dataclasses import dataclass, field
from fastapi import FastAPI, HTTPException, Response

# 2. Create App Instance
app = FastAPI()

# 3. Define Data Class
@dataclass
class Channel:
    id: str
    name: str
    tags: list[str] = field(default_factory=list)
    description: str = ""

# 4. Initiate a Channel Dictionary that contains details of YouTube channels
channels: dict[str, Channel] = {}

with open("channels.json", encoding="utf8") as file:
    channels_raw = json.load(file)
    for channel_raw in channels_raw:
        channel = Channel(**channel_raw)
        channels[channel.id] = channel

# 5. Define a GET request function for Homepage
@app.get("/")
def read_root() -> Response:
    return Response("The server is running.")

# 6. Define a GET request function for Channels
@app.get("/channels/{channel_id}", response_model=Channel)
def read_item(channel_id: str) -> Channel:
    if channel_id not in channels:
        raise HTTPException(status_code=404, detail="Channel not found")
    return channels[channel_id]

# Run the App through Uvicorn
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
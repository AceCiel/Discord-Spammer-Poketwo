from webserver import keep_alive
import requests

channelID = 1195020177318875227
headers = {
    "authorization":
    "NzU0Mjg2MjI0NjQyMTQ2MzA1.G5vbuE.0X-cE0hHiJfIMEFOHvNFmTT06mw6d5VF9I9CjA"
}
keep_alive()
file = open("text.txt", "r")
lines = file.readlines()

while True:
    for line in lines:
        requests.post(
            f"https://discord.com/api/v9/channels/{channelID}/messages",
            headers=headers,
            json={"content": line})

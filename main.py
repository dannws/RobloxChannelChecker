import json, os, time
import requests
from discord_webhook import DiscordWebhook, DiscordEmbed
import pyfiglet

os.system(f'title dannw on dc ^')

with open("config.json", "r") as config:
  config = json.load(config)

webhookurl = config['webhook']
embed = DiscordEmbed(title="dannw on dc :3", url="https://github.com/dannws/RobloxChannelChecker", color=0x39328a)

webhook = DiscordWebhook(url=webhookurl)
headers = {'Accept': 'application/json'}

r = requests.get("https://raw.githubusercontent.com/bluepilledgreat/Roblox-DeployHistory-Tracker/main/ChannelsAll.json", headers=headers)
channelList = r.json()



def clear():
    os.system("cls")
    print(
        pyfiglet.figlet_format(
            "                                     Channels                                                     "
        )
    )
    print("                                                   (MADE by dannw)")
    print("                                                    (im mentally)")
    print("                                                     (unstable)")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")
    print("                         ")


clear()


def checkifalive(channel):
    bleh = requests.get(f"https://clientsettings.roblox.com/v2/client-version/WindowsPlayer/channel/{channel}")
    if bleh.status_code == 200:
       print(f"{channel} is open")
       try:
          embed.delete_embed_field(1)
       except:
          embed.add_embed_field(name=channel, value=f"{channel} is open!", inline=False)
       

       




def checkchannel():
    for i in range(0,177):
        channel = channelList[i]
        checkifalive(channel=channel)



while True:
   checkchannel()
   try:
      webhook.delete()
   except:
      pass
   print("posting embed...")
   print("")
   print("--------------------------------------------------------------------")
   print("")
   webhook.add_embed(embed)
   webhook.execute()
   webhook.remove_embed(0)
   time.sleep(600)
   
   












from browser import document, html

def discordInvite(ev):
  Win("you got invited :D", "Hello, please join our discord server :3</br><center><a href='https://discord.gg/MPmAVk3VwK'>click here</a>", 500, 500)

registerApp(
  App(
    "discord",
    "discord.jpg",
    discordInvite
  )
)
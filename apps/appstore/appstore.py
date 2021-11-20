def appstore(ev):
  ducc = Win("App Store", "<iframe src='https://udn-appstore.tbsharedaccount.repl.co/assets/apps/applauncher/' style=\"width: 100%; height: 100%;\"></iframe>", 300, 320)
registerApp(
  App(
    "app store",
    "UDNAPPSTORE.png",
    appstore
  )
)
# def installAnApp(appname, appHTML,winwidth,winheight,icon):
#   def f1(1)
#   registerApp(
#     App(
#       appname,
#       icon,
#       f1
#     )
#   )
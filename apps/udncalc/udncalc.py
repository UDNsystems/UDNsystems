def Test(ev):
  calc = Win("UDNCalc", "<iframe src='https://udncalc.udnsystems.repl.co' style=\"width: 100%; height: 100%;\"></iframe>", 300, 320)
registerApp(
  App(
    "UDNCalc",
    "udncalc.png",
    UDNCalc
  )
)
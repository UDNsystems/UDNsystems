def docs(ev):
  Win("Documentation","<iframe src='auroramate/apps/docs/docs.html' width='400' height='400'/>",400, 400)

registerApp(
  App(
    "Documentation",
    "credits.png",
    docs
  )
)
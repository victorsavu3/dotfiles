status.register("disk",
    path="/",
    format="💾 {used:.0f}/{total:.0f}G",)

status.register("pulseaudio",
    format="♪{volume}",
    step=1,)

status.register("taskwarrior")

status.register("spotify")

status.run()

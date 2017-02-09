#!/usr/bin/python
# -*- coding: utf-8 -*-

from i3pystatus import Status

status = Status()

status.register("clock",
    format="%a %-d-%-m %H:%M:%S",)

status.register("load")

status.register("temp",
    format="{temp:.0f}°C",)

status.register("battery",
    format="{status} {percentage:2.0f}% [{percentage_design:2.0f}%] {remaining:%E%hh:%Mm}",
    alert=True,
    alert_percentage=15,
    status={
        "DIS": "🔋",
        "CHR": "⚡",
        "FULL": "🔌",
    },)

status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

status.register("network",
    interface="enp2s0",
    format_up="🖧 {v4cidr}",
    format_down="🖧 DOWN",)

status.register("network",
    interface="wlp3s0",
    format_up="📻 {essid} {quality:03.0f}% {v4cidr}",
    format_down="📻 DOWN",)

status.register("disk",
    path="/",
    format="💾 {used:.0f}/{total:.0f}G",)

status.register("pulseaudio",
    format="♪{volume}",
    step=1,)
    
status.register("taskwarrior")

status.register("spotify")

status.run()

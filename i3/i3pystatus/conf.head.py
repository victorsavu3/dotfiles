#!/usr/bin/python
# -*- coding: utf-8 -*-

from i3pystatus import Status

status = Status()

status.register("clock",
    format="%a %-d-%-m %H:%M:%S",)

status.register("load")

status.register("temp",
    format="{temp:.0f}°C",)

status.register("runwatch",
    name="DHCP",
    path="/var/run/dhclient*.pid",)

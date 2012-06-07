#!/bin/sh
#
# Changes the brightness of the specified screen.
# Your specific path will likely vary, so customise to your needs.

echo $1 > /sys/devices/pci0000:00/0000:00:0b.0/0000:02:00.0/backlight/acpi_video0/brightness


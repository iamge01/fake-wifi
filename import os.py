import os

# Configuration details
ssid = "FakeWiFi"
interface = "wlan0"  # Replace with your wireless interface name
channel = "6"  # Wi-Fi channel

# Create a configuration file for hostapd
hostapd_conf = f"""
interface={interface}
driver=nl80211
ssid={ssid}
hw_mode=g
channel={channel}
"""

# Write the hostapd configuration file
with open("hostapd.conf", "w") as file:
    file.write(hostapd_conf)

# Create a command to run hostapd
hostapd_command = f"sudo hostapd hostapd.conf"

# Execute the hostapd command
os.system(hostapd_command)

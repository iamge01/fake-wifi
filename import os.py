import os

# List of SSIDs to create
ssids = ["FakeWiFi_1", "FakeWiFi_2", "FakeWiFi_3", "FakeWiFi_4"]

# Set the Wi-Fi interface to use
interface = "Wireless LAN adapter WiFi"  # Replace with your Wi-Fi adapter name

# Automate the creation of multiple SSIDs using airbase-ng
def create_multiple_ssids(interface, ssids):
    # Put the interface into monitor mode
    os.system(f"sudo ifconfig {interface} down")
    os.system(f"sudo iwconfig {interface} mode monitor")
    os.system(f"sudo ifconfig {interface} up")

    # Create each SSID on different channels
    for i, ssid in enumerate(ssids):
        channel = 6 + i  # Set each SSID to a different channel
        command = f"sudo airbase-ng -e \"{ssid}\" -c {channel} {interface} &"
        os.system(command)
        print(f"Started SSID: {ssid} on channel {channel}")

# Create the fake SSIDs
create_multiple_ssids(interface, ssids)

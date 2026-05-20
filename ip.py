# Raspberry Pi IP Display on SSD1306 OLED
#
# Hardware:
# - Raspberry Pi
# - SSD1306 OLED display (128x64 I2C)
#
# Wiring (I2C):
# OLED VCC -> 3.3V
# OLED GND -> GND
# OLED SCL -> GPIO3 (SCL)
# OLED SDA -> GPIO2 (SDA)
#
# Install dependencies:
# sudo apt update
# sudo apt install python3-pip -y
# pip3 install adafruit-circuitpython-ssd1306 pillow netifaces
#
# Enable I2C:
# sudo raspi-config
# Interface Options -> I2C -> Enable

import time
import socket
import netifaces
from PIL import Image, ImageDraw, ImageFont
import board
import busio
import adafruit_ssd1306

# OLED display size
WIDTH = 128
HEIGHT = 64

# Initialize I2C
i2c = busio.I2C(board.SCL, board.SDA)

# Initialize OLED
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c)

# Clear display
oled.fill(0)
oled.show()

# Create blank image for drawing
image = Image.new("1", (WIDTH, HEIGHT))
draw = ImageDraw.Draw(image)

# Load default font
font = ImageFont.load_default()


def get_ip_address():
    """Get Raspberry Pi IP address."""
    interfaces = netifaces.interfaces()

    for interface in interfaces:
        if interface == "lo":
            continue

        addrs = netifaces.ifaddresses(interface)

        if netifaces.AF_INET in addrs:
            ip_info = addrs[netifaces.AF_INET][0]
            return ip_info.get("addr", "No IP")

    return "No Network"


while True:
    # Clear drawing area
    draw.rectangle((0, 0, WIDTH, HEIGHT), outline=0, fill=0)

    hostname = socket.gethostname()
    ip = get_ip_address()

    # Draw text
    draw.text((0, 0), "Raspberry Pi", font=font, fill=255)
    draw.text((0, 20), f"Host: {hostname}", font=font, fill=255)
    draw.text((0, 40), f"IP: {ip}", font=font, fill=255)

    # Display image
    oled.image(image)
    oled.show()

    # Refresh every 5 seconds
    time.sleep(5)

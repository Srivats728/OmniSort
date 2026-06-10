# OmniSort

**The ultimate download and email manager.**

Have you ever just stared at your download folder or your email inbox in pure horror, looking at cluttered files and unread emails you didn't even know existed? Enter OmniSort, an all-in-one physical tool to quickly and easily sort your email inbox or download folder with absolute ease. Featuring an OLED display, 16 customizable switches, and a glorious rotary knob, tactility and ease of use you get with this product is unmatched. Follow along my journey of building this and bringing it to life! Thanks for reading.

*Built by Srivats Viswanathan*

---

## Build Log
*(CAD renders, schematics, and PCB layouts will be here once they are finished).*

## Hardware
* **Brains:** Seeed XIAO RP2040 
* **Inputs:** 16x MX-Style Switches & 1x EC11 Rotary Encoder
* **Display:** 0.91-inch OLED 
* **Under Hood:** 16x 1N4148 Diodes (for 4x4 matrix) & 16x SK6812 MINI-E RGB LEDs
* **Case:** Custom 3D-printed enclosure secured with M3 screws and heatset inserts

## How It Works
1. **Board:** Will use CircuitPython/KMK to handle switch matrix, track dial, and update OLED screen. 
2. **Host:** A background Python script on PC will watch local folders and talking to email servers to route data whenever a switch is hit.
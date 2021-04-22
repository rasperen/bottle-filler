# bottle-filler
Do you hate bottling as well? This makes it faster and easier!
This project will enable a pump for a specified time to fill a bottle.
This works for all bottles!

## How to use:
### Filling bottles:
1. Make sure the pump is clean and empty. Just pump some air through after cleaning. You don't want any cleaning solution in your beer.
2. Start pumping wort to a bottle until there is no air left in the hoses. You can use the timer or the flip switch, your choice!
3. Set the timer. Just try something out.
4. Do a tryout by pressing start (and read Emergency below)
5. Repeat steps 3 and 4 until the timer is correct.
6. Happy filling!

### Cleaning:
1. Pump cleaning solution through the pump and hoses with the flip switch.
2. Pump clean water through if needed.

### Emergency, emergency!
If the pump is pumping on the timer, and you want it to stop immediately, just press the start button again. The pump will stop and the screen will show STOP for 3 seconds. After that, you can start filling bottles again.

## Materials:
  * Pump: https://nl.aliexpress.com/item/32884867303.html 
  * Adapter: https://nl.aliexpress.com/item/33010470892.html (12V, 3A)
  * Wemos D1 Mini: https://nl.aliexpress.com/item/32529101036.html
  * Wemos screen: https://nl.aliexpress.com/item/32627787079.html
  * SSR: https://nl.aliexpress.com/item/33054516205.html (without shell)
  * 3 Buttons: https://nl.aliexpress.com/item/681794061.html
  * Switch: https://nl.aliexpress.com/item/32890322785.html
  * Box of minumum 9.4x9.4x3cm
  * Screws to secure the Wemos:https://nl.aliexpress.com/item/4000027708283.html (M2 100pcs, 5mm)
  * Spacers to secure the Wemos: https://nl.aliexpress.com/item/4000142479946.html (M2, 3mm)
  * 1.5mm drill bit: https://nl.aliexpress.com/item/4000258922176.html
  * Wiring
  * Usb charger + cable

## Used equipment:
  * Soldering equipment
  * Drill
  * Multitool
  * 12mm drill bit

## Connect to the WEMOS:
  * Screen (easiest way is to just use it as a HAT)
  * SSR to GPIO14 (Input +) and GND (Input -)
  * Start button to GPIO4 and GND
  * Up button to GPIO12 and GND
  * Down button to GPIO13 and GND
  * Pull down resistors are not neccesary, as the Wemos has internal resistors.

## Also Connect:
  * Switch to SSR Output + and -
  * Pump to the SSR Output -
  * Adapter + to the SSR Output +
  * Adapter - to Pump -

## To Save the file to the Wemos (from Windows):
  * Install uPyCraft: https://randomnerdtutorials.com/install-upycraft-ide-windows-pc-instructions/
  * Go to Tools -> Preferences
  * Go to the Serial tab
  * Set: baud=115200, bytesize=8, stopbots=1,  parity=none
  * Click close button on the preferences popup
  * Connect the Wemos to your computer
  * Click Tools -> Serial and the correct COM Port
  * Click the New File button on the upper right, to create main.py
  * Copy the contents of the file in the editor and save
  * Click Tools -> Download to download the file to the Wemos

## Known issues:
  * When you get an error on line 20, change `i2c = I2C(-1, Pin(5), Pin(4))` to `i2c = I2C(Pin(5), Pin(4))` on line 20.
  
*Special thanks to Loek and Diede from brew guild Zoetermeer for helping me out on some questions I had while creating this.*

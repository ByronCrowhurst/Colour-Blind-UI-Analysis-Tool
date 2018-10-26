# Contract 4 \- Colour Blindness UI Analysis Tool
* _Byron Crowhurst_
* _github ID: ByronCrowhurst_

### How to use the program:
To use the program simply add an image called "screen.jpg" and run the program.
After the program has exited there will be 3 new images in the program directory.

In the event that no "screen.jpg" can be found the program will simply exit with no changes being made.


1. main\(\)
The man function calls every other function neatly in one place, it calls the load_image function and stores the returned value in variables to be passed to the anomalous_trichromacy 
2. load\_image\(\)
The load image function simply loads and returns screenshot of the game to be changed later on in the code.
3. check\_image\_exists\(\)
This function checks if the image is able to be loaded.
4. colour\_blind\_adjustments\(base\_image, image\_one, image\_two, image\_three)
This function takes the images and creates pixel arrays which are then passed to other functions to have adjustments made, and then are returned and saved as PNG images
5. get\_type\_to\_adjust(type\_number)
Checks which type of colour blindness is being simulated and returns a string of the type of colour blindness
6. colour\_blindness\_recolouring(red, green, blue, type\_number)
Takes the base colours of the pixel and applys a form of colour skew to the RGB channels (R = R + G + B etc...) using the dictionaries imported form colour\_skew\_values.py
7. colour\_skew\_values.py
A file that stores the correct skew values (listed below) in a dictionary to be called later.

\*RGB channel values:

Normal: R:\[100, 0, 0\], G:\[0, 100, 0\], B:\[0, 100, 0]
 Protanopia: R:\[56\.667, 43\.333, 0\], G:\[55\.833, 44\.167, 0\], B:\[0, 24\.167, 75\.833\]
 Protanomaly: R:\[81\.667, 18\.333, 0\], G:\[33\.333, 66\.667, 0\], B:\[0, 12\.5, 87\.5]
 Deuteranopia: R:\[62\.5, 37\.5, 0\], G:\[70, 30, 0\], B:\[0, 30, 70\]
 Deuteranomaly: R:\[80, 20, 0\], G:\[25\.833, 74\.167, 0\], B:\[0, 14\.167, 85\.833\]
 Tritanopia: R:\[95, 5, 0\], G:\[0, 43\.333, 56\.667\], B:\[0, 47\.5, 52\.5\]
 Tritanomaly: R:\[96\.667, 3\.333, 0\], G:\[0, 73\.333, 26\.667\], B:\[0, 18\.333, 81\.667\]
 Achromatopsia: R:\[29\.9, 58\.7, 11\.4\], G:\[29\.9, 58\.7, 11\.4\], B:\[29\.9, 58\.7, 11\.4\]
 Achromatomaly: R:\[61\.8, 32, 6\.2\], G:\[16\.3, 77\.5, 6\.2\], B:\[16\.3, 32\.0, 51\.6\]

extracted from: http://web.archive.org/web/20081014161121/http://www.colorjack.com/labs/colormatrix/

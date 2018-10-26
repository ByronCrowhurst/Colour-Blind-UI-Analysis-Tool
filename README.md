# Contract 4 \- Colour Blindness UI Analysis Tool
* _Byron Crowhurst_
* _github ID: ByronCrowhurst_

1. main\(\)
The man function calls every other function neatly in one place, it calls the load_image function and stores the returned value in variables to be passed to the anomalous_trichromacy 
2. load_image\(\)
The load image function simply loads and returns screenshot of the game to be changed later on in the code.
3. colour_blind_adjustments\(\)
This algorthm takes the images and converts them to a pixel array, then passes the values of the pixel arrays to a seperate reduction algorithm. Then, once assigned to the array it is then deleted so that pygame can save the images.
4. protanopia_recolouring\(\)
This algorithm takes the RGB values, then using the correct numbers\* adjusts the values accordingly and returns the new RGB values

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

# Contract 4 \- Colour Blindness UI Analysis Tool
* _Byron Crowhurst_
* _github ID: ByronCrowhurst_

1. main\(\)
The man function calls every other function neatly in one place, it calls the load_image function and stores the returned value in variables to be passed to the anomalous_trichromacy 
2. load_image\(\)
The load image function simply loads and returns screenshot of the game to be changed later on in the code.
3. anomalous_trichromacy\(\)
This algorthm takes the images and converts them to a pixel array, then reduces the RGB values of the pixel arrays. Then, once written to the image, deletes the arrays and saves the images.
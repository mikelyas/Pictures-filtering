# Image processing

This is a program, that converts your image based on your request. Can process several requests at a time.

## What can it do?

- Mirror
- Rotate
- Invert
- Sharpen
- Darken by percentage from 0 to 100
- Lighten by percentage from 0 to 100
- Convert to black&white

## What did I used?

Every function is based on using numpy potential on max. NO scipy, NO matplotlib, NO cv2, ONLY HARDCORE. For sharpening I used padding method with kernel. For black&white np.mean and so on.

There is an individual file for every request, except lighten and darken,because they a pretty much the same.

## How do you use it?

Type python main.py --help for help, and you will get all the options you can use.
You can run program by python main.py, then you type your request from this list:
- --mirror
- --rotate
- --inverse
- --bw
- --lighten <percentage:0-100>
- --darken  <percentage:0-100>
- --sharpen

You can type as much requests as you wish, it will eventually sum up. And last, but not least you type path of the picture you want to convert and path to a result picture.
Remember that you are working in folder semestralka.
I used matplotlib to show a result picture at the end of the program.

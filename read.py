from subprocess import call

cmd_img='fswebcam -r 720x1280 image2.png'#to capture image
cmd_beg= ' tesseract abc.png xyz'#To convert image file to text file
cmd_end= ' espeak -ven+f4 -f xyz.txt 2>/dev/null' # To play back from text file

call([cmd_img], shell=True)
call([cmd_beg], shell=True)
call([cmd_end], shell=True)




# This sketch makes use of:
# "Nyan Cat"
# PRguitarman [Standard YouTube License / redrawn as sprite sheet], from Youtube

def setup():
    size(300,138)
    frameRate(12)

def draw(): 
    background('#004477')
    nyan = loadImage('nyancat-spritesheet.gif')
    xpos = (frameCount % 5) * 300 * -1
    image(nyan, xpos,0)
    

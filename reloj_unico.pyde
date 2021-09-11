r = 0
b = 0
d = 0
def setup ():
    size (250, 250)
def draw():
    background(57, 208, 247)
    global r
    global b
    global d
    fill(247, 57, 191)
    ellipse(25, r, 40, 50)
    if r > height:
       r = 0
    else:
       r = map(second(), 0, 59, 0, height)
    ellipse(120, b, 40, 50)
    if b > height:
       b = 0
    else:
       b = map(minute(), 0, 59, 0, height)
    ellipse(210, d, 40, 50)
    if d > height:
       d = 0
    else:
       d = map(hour(), 0, 59, 0, height)

import math

# fragment shader like example of how colors could be controlled
def fragment(pos, s):
    x = pos[0] * 2 - 1
    y = pos[1] * 2 - 1

    dist = math.sqrt(x*x + y*y)

    brightness = math.sin(dist*3 + s/5)/2 + 0.5

    r = brightness * (math.sin(s/5)/2 + 0.5)
    g = brightness * (math.cos(s/5)/2 + 0.5)
    b = 0

    return (r, g, b)
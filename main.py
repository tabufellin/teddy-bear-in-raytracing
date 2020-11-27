
from raytracer import Raytracer
from sphere import *
from materials import *
from math_things import V3
from light import Light

r = Raytracer(500, 500)

r.light = Light(
  position=V3(30, 15, 50),
  intensity=1.1
)

r.background_color = color(100,100,100)

r.scene = [
  
  Sphere(V3(4.6, -1.3, -15), 2, red_bowl),
  Sphere(V3(5.8, 0, -14.5), 1.1, brown_skin),
  Sphere(V3(2.9, 0, -14.5), 1.1, brown_skin),
  Sphere(V3(6, -2.6, -13), 1.1, brown_skin),
  Sphere(V3(3.3, -2.6, -13), 1.1, brown_skin),
  Sphere(V3(4.6, 1.6, -14.9), 1.7, brown_skin),
  Sphere(V3(5.6, 2.7, -14.4), 0.7, brown_skin_extra),
  Sphere(V3(3.6, 2.7, -14.4), 0.7, brown_skin_extra),
  Sphere(V3(4.6, 1.3, -13.52), 0.6, brown_skin_extra),
  Sphere(V3(4.2, 2.1, -13.5), 0.2, eye),
  Sphere(V3(5, 2.1, -13.5), 0.2, eye),
  Sphere(V3(4.5, 1.3, -13), 0.2, eye),
  
  Sphere(V3(-3, -1.3, -15), 2, white_skin),
  Sphere(V3(-1.3, 0, -14.5), 1.1, white_skin),
  Sphere(V3(-4.7, 0, -14.5), 1.1, white_skin),
  Sphere(V3(-1.3, -2.6, -13.5), 1.1, white_skin),
  Sphere(V3(-4.6, -2.6, -13.5), 1.1, white_skin),
  Sphere(V3(-3, 1.6, -14.9), 1.7, white_skin),
  Sphere(V3(-2, 2.7, -14.4), 0.7, white_skin),
  Sphere(V3(-4, 2.7, -14.4), 0.7, white_skin),
  Sphere(V3(-3, 1.3, -13.3), 0.2, white_skin),
  Sphere(V3(-3.4, 2.1, -13.5), 0.2, eye),
  Sphere(V3(-2.6, 2.1, -13.5), 0.2, eye),
  
]
r.render()
r.write('out.bmp')
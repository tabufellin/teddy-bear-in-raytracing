from color import color

class Material(object):
  def __init__(self, diffuse=color(0,0,0), albedo=(1, 0), spec=0):
    self.diffuse = diffuse
    self.albedo = albedo
    self.spec = spec


red_bowl = Material(diffuse=color(180, 0, 0), albedo=(0.6,  0.3), spec=10)
white_skin = Material(diffuse=color(255, 255, 255), albedo=(1,  1), spec=40)
brown_skin = Material(diffuse=color(255, 204, 153), albedo=(0.2,  0.3), spec=20)
eye = Material(diffuse=color(50, 50, 50), albedo=(0.2,  0.3), spec=10)
brown_skin_extra = Material(diffuse=color(150, 60, 50), albedo=(0.2,  0.3), spec=10)
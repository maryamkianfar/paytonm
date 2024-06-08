import random

from payton.scene import Scene, physics
from payton.scene.geometry import Cube
from payton.scene.gui import info_box


def select(list):
    for obj in list:
        obj.material.color = [1, 1, 1]
        obj.mass = 1.0


scene = Scene(on_select=select, physics_force_continuous=True)
for i in range(10):
    x = random.randint(-5, 5)
    y = random.randint(-5, 5)
    z = random.randint(-5, 5)
    r = random.randint(0, 255) / 255.0
    g = random.randint(0, 255) / 255.0
    b = random.randint(0, 255) / 255.0
    cube = Cube()
    cube.material.color = [r, g, b]
    cube.position = [x, y, z]
    scene.add_object("cube_{}".format(i), cube)

scene.add_object(
    "info",
    info_box(left=10, top=10, label="Try clicking cubes"),
)

scene.run(start_clocks=True)

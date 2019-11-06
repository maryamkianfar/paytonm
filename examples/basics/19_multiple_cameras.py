import os
from payton.scene import Scene
from payton.scene.geometry import Cube
from payton.scene.observer import Observer

scene = Scene()
scene.background.top_color = [0, 0, 0, 1]
scene.background.bottom_color = [0, 0, 0, 1]

texture_file = os.path.join(os.path.dirname(__file__), "cube.png")

cube = Cube(width=5.0, height=5.0, depth=5.0)
cube.position = [0, 0, 2.5]
cube.material.texture = texture_file

scene.add_object("cube", cube)

inside_box = Observer(
    position=[-1.7898840267533351, 2.210322695165203, 1.400984730396208],
    target=[0, 0, 1],
    fov=110,
)

scene.add_observer(inside_box)
scene.huds["_help"].show()

scene.run()

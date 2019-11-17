"""Quake 2 Model Test"""
import os

import sdl2

from payton.scene import Scene
from payton.scene.controller import Controller
from payton.scene.geometry import MD2, Plane
from payton.scene.gui import info_box

scene = Scene()
ground = Plane(width=20, height=20)
object_file = os.path.join(os.path.dirname(__file__), "infantry", "tris.md2")
model = MD2(filename=object_file)


class CustomKeyboardControls(Controller):
    def keyboard(self, event, scene):
        super().keyboard(event, scene)
        if event.type == sdl2.SDL_KEYUP:
            key = event.key.keysym.sym
            if key == sdl2.SDLK_UP:
                model.animate("walk", 2, 13)
            if key == sdl2.SDLK_DOWN:
                model.animate("death", 0, 19, False)


label = """
Hit Keyboard UP to walk
Hit Keyboard Down to death animation
"""

scene.add_object(
    "info", info_box(left=10, top=10, width=320, height=100, label=label)
)

scene.add_object("ground", ground)
scene.add_object("infantry", model)
scene.controller = CustomKeyboardControls()
model.animate("walk", 2, 13)
scene.run()

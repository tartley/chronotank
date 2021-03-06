
from math import radians

scale_damping = rot_damping = 0.98

class CameraMan(object):

    def __init__(self, camera, get_follow=None, scale=None, rot=None):
        self.camera = camera
        self.get_follow = get_follow
        self.x = 0
        self.y = 0
        if scale is None:
            scale = camera.scale
        self.scale = scale
        if rot is None:
            rot = camera.rot
        self.rot = rot

    def update(self, dt):
        if self.get_follow:
            follow = self.get_follow()
        else:
            follow = self

        if follow is not None:
            self.camera.x = follow.x
            self.camera.y = follow.y
            self.camera.rot += \
                (radians(-follow.rot) - self.camera.rot) * rot_damping * dt

        self.camera.scale += \
            (self.scale - self.camera.scale) * scale_damping * dt


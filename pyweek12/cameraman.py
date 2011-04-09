
scale_damping = rot_damping = 0.98

class CameraMan(object):

    def __init__(self, camera, get_follow, scale=None, rot=None):
        self.camera = camera
        self.get_follow = get_follow
        if scale is None:
            scale = camera.scale
        self.scale = scale
        if rot is None:
            rot = camera.rot
        self.rot = rot

    def update(self, _, dt):
        follow = self.get_follow()
        if follow is not None:
            self.camera.x = follow.x
            self.camera.y = follow.y
        self.camera.scale += \
            (self.scale - self.camera.scale) * scale_damping * dt
        self.camera.rot += \
            (self.rot - self.camera.rot) * rot_damping * dt


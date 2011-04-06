
class CameraMan(object):

    def __init__(self, camera, get_follow):
        self.camera = camera
        self.get_follow = get_follow

    def update(self, _, __):
        follow = self.get_follow()
        if follow is not None:
            self.camera.x = follow.x
            self.camera.y = follow.y


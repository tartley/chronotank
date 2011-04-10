print 'options:'
print '  --novsync'
print '  --window'
print '  --fps'
print '  --alsa|--openal|--directsound|--silent'


class Options(object):
    '''
    Application-wide options are stored in this object's attributes.
    These are populated at start-up by a rough-and-ready check of command-line
    args. One day they might also take config files into account, to allow
    persistance of option changes by the user.

    `vsync`: Boolean, default to True. synchronise screen refreshes to monitor.
    Setting this to True will limit framerate to your monitor refresh rate
    (e.g. 60fps), which is likely what you want unless you are performance
    testing. Setting it to False will increase framerate, but not visibly
    (since your monitor cannot display the extra frames) and will introduce
    'tearing'. Note that some video drivers have settings which override this
    value.

    `fullscreen`: boolean, default to True. If false, display in a window.

    `fps`: Display frames per second in lower-left of screen.
    '''
    def __init__(self, argv):
        self.vsync = '--novsync' not in argv
        self.fullscreen = '--window' not in argv and '-w' not in argv
        self.fps = '--fps' in argv

        self.audio = None
        if '--alsa' in argv:
            self.audio = 'alsa'
        if '--openal' in argv:
            self.audio = 'openal'
        if '--silent' in argv:
            self.audio = 'silent'
        if '--directsound' in argv:
            self.audio = 'directsound'


    def __str__(self):
        return 'Options:\n' + '\n'.join(
            '    %s = %s' % (attr, value)
            for attr, value in self.__dict__.items()
        )


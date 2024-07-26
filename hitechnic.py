from pybricks.iodevices import Ev3devSensor


class HTColorSensor(Ev3devSensor):
    _ev3dev_driver_name = 'ht-nxt-color-v2'
    _MODE_COLOR = 0
    _MODE_RGBW = 1

    def __init__(self, val):
        super().__init__(val)
        self.m = self._MODE_COLOR
        # self._mode('RGB')
        self._number_of_values = 4  # I want to extract tuple of [R,G,B,W] values

    def _open_files(self):
        super()._open_files()
        self._command_file = open(self.path + 'command', 'w')

    def _close_files(self):
        super()._close_files()
        self._command_file.close()

    def set_mains_50hz(self):
        """Configure the sensor for 50Hz power mains"""
        self._command_file.write('50HZ')
        self._command_file.flush()

    def set_mains_60hz(self):
        """Configure the sensor for 60Hz power mains"""
        self._command_file.write('60HZ')
        self._command_file.flush()

    def rgbw(self):
        """returns the tuple of color values: (red, blue, green white). 0 to 255 for each color"""
        return self.read('RGB')

    def color(self):
        return self.read('COLOR')

    def read_mode(self, mode):
        return self.read(mode)

class Temperature:

    scale_units = {"C": "Celsius", "F": "Fahrenheit"}
    def __init__(self, degrees, scale="C"):

        self.degrees = degrees
        self.scale = scale

    def convert_to(self, target_scale):
        if self.scale == target_scale:
            return self.degrees
        if self.scale == "C" and target_scale == "F":
            return (self.degrees * 9/5) + 32
        return (self.degrees - 32) * 5/9

my_temp = Temperature(60)
print(my_temp.convert_to("F"))
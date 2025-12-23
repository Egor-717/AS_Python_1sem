if __name__ == "__main__":
    pass


import math

def DegToRad(D):
    if D <= 0 or D >= 360:
        raise ValueError("Угол должен быть в диапазоне: 0 < D < 360")

    radians = D * math.pi / 180
    return radians

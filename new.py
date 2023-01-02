import configparser

def height_prct(percentage):
    return (configparser.HEIGHT / 100) * percentage

def width_prct(percentage):
    return (configparser.WIDTH / 100) * percentage
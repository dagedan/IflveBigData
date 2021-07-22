import random


def random_six():
    return "%06d" % random.randint(0, 999999)


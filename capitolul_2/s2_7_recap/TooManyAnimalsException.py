class TooManyAnimalsException(Exception):

    def __init__(self):
        super().__init__("Sunt prea multe animale in adapost!")
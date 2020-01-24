class Guardian:
    """
    Class to create the "Guardian" charater whith name and
    initial position.
    """
    def __init__(self, name, structure, position):
        """
        Creation of Guardan
        """
        self.nane = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        self.structure[self.case_y][self.case_x] = "G"

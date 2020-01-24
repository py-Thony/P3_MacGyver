class Item:
    """
    Class of items
    """
    def __init__(self, name, structure, position):
        """
        Creation of items
        """
        self.name = name
        self.position = position
        self.structure = structure
        self.case_y = position[0]
        self.case_x = position[1]
        self.structure[self.case_y][self.case_x] = name[0]
        
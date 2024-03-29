class Base:
    """Base class for managing id attribute."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base instance.

        Args:
            id (int): The identity of the new Base instance.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


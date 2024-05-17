#!/usr/bin/python3
"""Defines a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize data.

        Args:
            size (int, optional): Size of the square.
            position (tuple[int], optional): Position of the square.
        """
        self.size = size
        self.position = position

    def area(self):
        """Get the current square area."""
        return self.__size * self.__size

    @property
    def size(self):
        """Get the size of square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter of the value size.
            Args:
                value (int): Value corresponding to the size.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter of the value position.
            Args:
                value (tuple[int]): Value corresponding to the position.
        """
        try:
            if len(value) != 2 or value[0] < 0 or value[1] < 0:
                raise
            if not isinstance(value[0], int) or not isinstance(value[1], int):
                raise
        except Exception:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Prints in stdout the square with the character #."""
        x, y = self.position
        if self.size == 0:
            print()
            return
        for iiii in range(y):
            print()
        for i in range(self.size):
            for ii in range(x):
                print(" ", end="")
            for iii in range(self.size):
                print("#", end="")
            print()

class Publisher:

    def __init__(self, publisher_name: str):
        if isinstance(publisher_name, int):
            self.__name = "N/A"
        elif publisher_name.strip():
            self.__name = publisher_name.strip()
        else:
            self.__name = "N/A"
        # TODO

        pass

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, publisher_name):
        # TODO
        self.__name = publisher_name
        pass

    def __repr__(self):
        # we use access via the property here
        return f'<Publisher {self.__name}>'

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return other.name == self.__name

    def __lt__(self, other):
        return self.__name < other.name

    def __hash__(self):
        return hash(self.__name)

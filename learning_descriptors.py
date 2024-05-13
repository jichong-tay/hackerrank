# Non-Data Descriptors
class Yes:
    """A non-data descriptor that always returns Yes"""

    def __get__(self, instance, owner):
        print("Yes.__get__ called")
        return "Yes"


# Data Descriptors
class NoisyDescriptor:
    """A data descriptor that prints out all its actions"""

    def __set_name__(self, owner, name):
        print(f"Received {name=} from {owner=}")
        self.private_name = f"_{name}"

    def __get__(self, obj, objcls):
        print(f"Getting {self.private_name} from {obj=} of {objcls=}")
        if obj:
            return getattr(obj, "self.private_name", "Nothing here!")
        return getattr(objcls, "self.private_name", "Nothing here!")

    def __set__(self, obj, value):
        print(f"Setting value {value=} on {obj=}")
        setattr(obj, "self.private_name", value)

    def __delete__(self, obj):
        print(f"Deleting value from {obj}")
        delattr(obj, "self.private_name")


class TestClass:

    alpha = Yes()
    beta = NoisyDescriptor()
    gamma = NoisyDescriptor()

    def __init__(self, value):
        self.beta = value

    @property
    def zeta(self):
        return getattr(self, "_zeta", None)

    @zeta.setter
    def zeta(self, value):
        self._zeta = value

    @zeta.deleter
    def zeta(self):
        delattr(self, "_zeta")

class ExampleClass:
    def __init__(self, public_data, protected_data, private_data):
        self.public_data = public_data # Public attribute

        self._protected_data = protected_data # Protected attribute

        self.__private_data = private_data # Private attribute

    
    def get_public_data(self):
        return self.public_data # Public method

    def _get_protected_data(self):
        return self._protected_data # Protected method

    def __get_private_data(self):
        return self.__private_data # Private method


example_object = ExampleClass(public_data="Public", protected_data="Protected", private_data="Private")# Object creation
print("Public Data:", example_object.public_data) # Public access to attribute

print("Protected Data:", example_object._get_protected_data()) # Protected access to attribute

print("Private Data:", example_object._ExampleClass__get_private_data()) # Private access to attribute

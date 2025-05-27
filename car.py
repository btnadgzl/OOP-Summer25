class Car:
    def __init__(self, brand, engine_type):
        self.brand = brand              
        self.__engine_type = engine_type  

    def show_engine_type(self):
        print(f"The engine type is: {self.__engine_type}")

    def __start_the_engine(self):
        print(f"The {self.brand} engine has started.")

    def start_the_car(self):
        self.__start_the_engine()

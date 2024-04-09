class ParentClass:
    def __init__(self, CarModel, Colour, Speed):
        self.CarModel = CarModel
        self.Colour = Colour
        self.Speed = Speed

    # f-string. It is a way to format strings by embedding expressions inside string literals,
    # using curly braces {}. The f at the beginning of the string stands for "formatted".
    # It allows you to embed Python expressions directly inside a string, making string formatting
    # much simpler and more readable.
    def display_info(self):
        return f"{self.CarModel} car colour is {self.Colour} have speed of {self.Speed}"

    def price_segment(self, segment):
        self.segment = segment
        print(self.display_info() + " is " + self.segment)


class ChildClass(ParentClass):
    expectation = 'high'


c1 = ChildClass('F21', 'White', 321)
c1.price_segment('Luxury')

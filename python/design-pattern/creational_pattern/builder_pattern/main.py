class House:
    def __init__(self, builder):
        self.stories = builder.stories
        self.door_type = builder.door_type
        self.roof_type = builder.roof_type


class HouseBuilder:
    def __init__(self):
        self.stories = None
        self.door_type = None
        self.roof_type = None

    def set_stories(self, stories: int):
        self.stories = stories
        return self

    def set_door_type(self, door_type: str):
        self.door_type = door_type
        return self

    def set_roof_type(self, roof_type: str):
        self.roof_type = roof_type
        return self

    def build(self):
        return House(self)


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build_1_story_house(self):
        return self.builder.set_stories(1).set_door_type("single").set_roof_type("pointy").build()

    def build_2_story_house(self):
        return self.builder.set_stories(2).set_door_type("double").set_roof_type("flat").build()

if __name__ == '__main__':
    house_builder = HouseBuilder()
    director = Director(house_builder)

    one_story_house = director.build_1_story_house()
    two_story_house = director.build_2_story_house()

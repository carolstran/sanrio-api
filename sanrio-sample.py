import collections
from graphene import ObjectType, Schema, String, Int, Field

Character = collections.namedtuple("Character", ['name', 'description', 'debut_year'])

data = {
    1: Character("Hello Kitty", "As tall as 5 apples and as heavy as three", 1974),
    2: Character("Tuxedosam", "A little naïve and a bit of a blunderer, but everybody loves this personable penguin who likes to eat all the time", 1979),
    3: Character("My Melody", "Very honest, good-natured and her favorite food is almond pound cake", 1975),
    4: Character("Strawberry King", "King of the beautiful and peaceful Strawberry Kingdom", 1975)
}

class CharacterType(ObjectType):
    name = String()
    description = String()
    debut_year = Int()

    def resolve_name(character, info):
        return person.name

    def resolve_description(character, info):
        return person.description

    def resolve_debut_year(character, info):
        return person.debut_year    

class Query(ObjectType):
    character = Field(CharacterType)

    def resolve_character(root, info):
        return data[1]

schema = Schema(query=Query)

# TODO: Expose the service on an endpoint
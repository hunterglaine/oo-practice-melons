############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name


    def add_pairing(self, *pairing):
        """Add a food pairing to the instance's pairings list."""

        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""
    
    all_melon_types = []

    musk = MelonType('musk', 1998, 'green', True, True, 
                 'Muskmelon')
    musk.add_pairing('mint')
    all_melon_types.append(musk)

    cas = MelonType('cas', 2003, 'orange', False, False, 
                 'Casaba')
    cas.add_pairing('strawberries','mint')
    all_melon_types.append(cas)
    
    cren = MelonType("cren", 1996, "green", False, False, "Crenshaw")
    cren.add_pairing("proscuitto")
    all_melon_types.append(cren) 

    yw = MelonType("yw", 2013, "yellow", False, True, "Yellow Watermelon")
    yw.add_pairing("ice cream")
    all_melon_types.append(yw) 
    
    return all_melon_types


def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""

    for melon in melon_types:
        print(f'{melon.name} pairs with')
        for pairing in melon.pairings:
            print(f'- {pairing}')
        print()



def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    melon_by_codes = {}

    for melon in melon_types:
        melon_by_codes[melon.code] = melon 
    
    return melon_by_codes

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest."""

    sellable = False

    def __init__(self, melon_type, shape_rating, color_rating, harvest_field,
                harvested_by):
        
        self.melon_type = melon_type
        self.shape_rating = shape_rating
        self.color_rating = color_rating
        self. harvest_field = harvest_field
        self.harvested_by = harvested_by
    

    def is_sellable(self):
    
        if self.shape_rating > 5 and self.color_rating > 5 and self.harvest_field != 3:
            self.sellable = True

def make_melons(melon_types):
    """Returns a list of Melon objects."""

    # Fill in the rest

def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 




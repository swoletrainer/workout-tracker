


class Athlete():
    """
    A class to represent an athlete.
    """
    def kg_to_lbs(kg):
        return float(kg)/2.2046226218

    def lbs_to_kg(lbs):
        return float(lbs)*2.2046226218

    def split_ips_height(height):
        ft, inches = height.split("'")
        return ft, inches
    

    def __init__(self, name=None, weight=None, height=None, training_method=None, IPS=True):
        # store arguments into dictionary
        self.stats = locals()

        # assign variables
        self.name = name
        self.weight = weight
        self.height = height
        self.training_method = training_method
        self.IPS = IPS

        self.complete_profile = True
        self.units = IPS
        
        # initialize height (IPS)
        self.feet = 0
        self.inches = 0

        # initialize height (metric)
        self.meters = 0
        self.cm = 0

        # set weight to appropriate units
        if self.units:
            self.weight_units = 'lbs'
            self.height_units_first = 'ft'
            self.height_units_second = 'in'
        else:
            self.wunits = 'kg'
            self.height_units_first = 'm'
            self.height_units_second = 'cm'

            
            
    def __str__(self):
        return '{}: {}, {}, {}'.format(str(self.name), str(self.weight), str(self.height), str(self.training_method))


if __name__ == '__main__':
    a = Athlete('Alaa Alokby', 210.00, "5'11", 'MM')
    print(a)
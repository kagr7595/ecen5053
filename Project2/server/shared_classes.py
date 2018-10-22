#Shared between files that must be started at different times

import json

#Special version for dictionaries
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, P_dict):
            return obj.__dict__
        #Let the base class default method raise the TypeError
        return json.JSONEncoder.default(self, obj)

#This is the object that will turned into a string via json serializing so that when I 'loads' it will be a dictionary [12]
class P_dict(object):
    def __init__(self, **entries):
        self.__dict__.update(entries)

    def show_current_temp_f(self):
        return self.current_temp_f
    
    def show_current_hum(self):
        return self.current_hum
    
    def show_lowest_temp_f(self):
        return self.lowest_temp_f
    
    def show_lowest_hum(self):
        return self.lowest_hum
    
    def show_highest_temp_f(self):
        return self.highest_temp_f
    
    def show_highest_hum(self):
        return self.highest_hum
    
    def show_average_temp_f(self):
        return self.average_temp_f
    
    def show_average_hum(self):
        return self.average_hum    

    def serialize(self):
        return json.dumps(self, cls=ComplexEncoder)

    def print_obj(self):
        print('current_temp_f: ', self.current_temp_f)
        print('current_hum: ',    self.current_hum)
        print('lowest_temp_f: ',  self.lowest_temp_f)
        print('lowest_hum: ',     self.lowest_hum)
        print('highest_temp_f: ', self.highest_temp_f)
        print('highest_hum: ',    self.highest_hum)
        print('average_temp_f: ', self.average_temp_f)
        print('average_hum: ',    self.average_hum)

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

    def show_current_status(self):
        #This is whether the gate is open or closed (open = 1)
        return self.current_status
    
    def show_current_timestamp(self):
        return self.current_timestamp
    
    def show_current_timestamp_str(self):
        return self.current_timestamp_str
    
    def show_day_num_open(self):
        return self.day_num_open
    
    def show_day_array_hour_num_open(self):
        return self.day_array_hour_num_open
    
    def show_day2_num_open(self):
        return self.day_num2_open
    
    def show_day2_array_hour_num_open(self):
        return self.day2_array_hour_num_open
    
    def show_day3_num_open(self):
        return self.day3_num_open
    
    def show_day3_array_hour_num_open(self):
        return self.day3_array_hour_num_open
    
    def show_day4_num_open(self):
        return self.day4_num_open
    
    def show_day4_array_hour_num_open(self):
        return self.day4_array_hour_num_open
    
    def show_day5_num_open(self):
        return self.day5_num_open
    
    def show_day5_array_hour_num_open(self):
        return self.day5_array_hour_num_open
    
    def show_day6_num_open(self):
        return self.day6_num_open
    
    def show_day6_array_hour_num_open(self):
        return self.day6_array_hour_num_open
    
    def show_day7_num_open(self):
        return self.day7_num_open
    
    def show_day7_array_hour_num_open(self):
        return self.day7_array_hour_num_open

    
    

    def serialize(self):
        return json.dumps(self, cls=ComplexEncoder)

    

    def print_obj(self):
        print('current_status: ', self.current_status)
        print('current_timestamp: ', self.current_timestamp)
        print('current_timestamp_str: ', self.current_timestamp_str)
        print('day_num_open: ', self.day_num_open)
        print('day_array_hour_num_open: ', self.day_array_hour_num_open)
        print('day2_num_open: ', self.day2_num_open)
        print('day2_array_hour_num_open: ', self.day2_array_hour_num_open)
        print('day3_num_open: ', self.day3_num_open)
        print('day3_array_hour_num_open: ', self.day3_array_hour_num_open)
        print('day4_num_open: ', self.day4_num_open)
        print('day4_array_hour_num_open: ', self.day4_array_hour_num_open)
        print('day5_num_open: ', self.day5_num_open)
        print('day5_array_hour_num_open: ', self.day5_array_hour_num_open)
        print('day6_num_open: ', self.day6_num_open)
        print('day6_array_hour_num_open: ', self.day6_array_hour_num_open)
        print('day7_num_open: ', self.day7_num_open)
        print('day7_array_hour_num_open: ', self.day7_array_hour_num_open)
        ####print(': ', self.)  ##format

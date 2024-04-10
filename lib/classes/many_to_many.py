class NationalPark:

    def __init__(self, name):
        # no underscore we accessing the property's getter 
        # if it had an underscore we would be referring to the private variable
        # and we would be bypassing the property's setter logic
        self.name = name
        
    def trips(self):
        #find trips that match current instance (self) that we are working within
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        # get all trips for current national park (self)
        # iterate over trips and isolate the visitor (trip.visitor)
        # self.trips() - self refers to the current instance
        # self.trips() - refers to value of method .trips() for current instance
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        # iterate over Trip.all
        # keep track of how many times we see a specific visitor 
        # find the max number of times 
        visits = [trip.visitor for trip in self.trips()]
        most_freq = None#this is most frequent visitor 
        most_freq_count = 0 #this is to keep track of the number of visits for most frequent visitors
        #loop through visits
        for i in visits:
            #get count of current value
            cur_freq = visits.count(i)
            # print(i.name, most_freq.name)
            #if current value's count > previous count
            if(cur_freq > most_freq_count):
                #update current values
                most_freq = i
                most_freq_count = cur_freq 
        #return resulting values
        return most_freq
        
        

    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, value):
        #check it name attribute exists 
        if (hasattr(self, 'name')):
            print('something went wrong')
        #if it doesn't exist, create self._name and set it
        else: 
            self._name = value 

class Trip:
    #class attribute 
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        #append whatever instance we are creating to class attribute 'all'
        Trip.all.append(self)
    
    @property 
    def start_date(self):
        return self._start_date 
    
    @start_date.setter 
    def start_date(self, value):
        # 'test test'
        months = ['jan', 'feb', 'march', 'apr', 'may', 'june', 'jul', 'aug', 'sept', 'oct', 'nov', 'dec']
        digit_ends = ['th', 'st', 'nd', 'rd']
        # is split[0] -> Jan, Feb, March, April, ...
        # is split[1] -> a digit, with 'th, st, nd, rd')
        if(isinstance(value, str) and len(value.split(' ')) == 2):
            split = value.split(' ')
            if(not split[0].lower() in months):
                print('something went wrong')
            if(split[1][-2:] not in digit_ends):
                print('something went wrong') 
            if(not split[1][:-2].isdigit()):
                print('something went wrong') 
            self._start_date = value 
            #is the first value in months
            #does the second value start with a number
            #does it end with something in digit_ends
        else:
            print('something went wrong')

    @property 
    def end_date(self):
        return self._end_date 
    
    @end_date.setter 
    def end_date(self, value):
        if(isinstance(value, str) and len(value.split(' ')) == 2):
            self._end_date = value 
        else: 
            print('something went wrong')

class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        pass

    @property 
    def name(self):
        return self._name 
    
    @name.setter 
    def name(self, value):
        if(isinstance(value, str) and 1 <= len(value) <= 15):
            self._name = value
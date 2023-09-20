class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, name):
        if(not hasattr(self, "name") and isinstance(name, str) and len(name) > 3):
            self._name = name 
        else: 
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in Trip.all]
        #for each visitor in visitors
        #check the count of that visitor in visitors
        return max(self.visitors(), key = lambda x: visitors.count(x))

    @classmethod 
    def most_visited(cls):
        # key compares items
        # key function where the iterables are passed and comparison is performed based on its return value
        # for each value in cls.all, lambda replaces value with park.total_visits()
        # park is the current value of iteration over cls.all
        return max(cls.all, key = lambda park: park.total_visits())

class Trip:
    all = []
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)

    @property 
    def start_date(self):
        return self._start_date 
    @start_date.setter 
    def start_date(self, start_date):
        if(isinstance(start_date, str) and len(start_date) >= 7 and len(start_date.split(' ')) == 2):
            self._start_date = start_date
        else: 
            raise Exception

    @property 
    def end_date(self):
        return self._end_date 
    @end_date.setter 
    def end_date(self, end_date):
        if(isinstance(end_date, str) and len(end_date) >= 7 and len(end_date.split(' ')) == 2):
            self._end_date = end_date
        else: 
            raise Exception 


class Visitor:
    all = []
    def __init__(self, name):
        self.name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name 
    @name.setter 
    def name(self, name):
        if(isinstance(name, str) and 1 <= len(name) <= 15):
            self._name = name 
        else: 
            raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        return len([trip for trip in self.trips() if trip.national_park == park])
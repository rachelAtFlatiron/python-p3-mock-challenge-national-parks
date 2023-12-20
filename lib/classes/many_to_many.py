class NationalPark:
    all = []
    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    def trips(self):
        #trip
        #all the trips 
        #if the trip matches the current national park
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        #visitor
        #loop through self.trips()
        return list(set([trip.visitor for trip in self.trips()]))
    
    #Returns the total number of times a park has been visited
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        # if not self.trips():
        #     return None
        # #key will represent a visitor (a visitor instance)
        # #value will represent the number of times the visitor has visited (an integer)
        # visitor_counts = {} 
        # for trip in self.trips():
        #     #if visitor key already exists
        #     if trip.visitor in visitor_counts:
        #         #add to the value
        #         visitor_counts[trip.visitor] += 1
        #     #if the visitor key does NOT exist
        #     else:
        #         #create that key, and set it to 1
        #         visitor_counts[trip.visitor] = 1
        # #use max to find the greatest value 
        # return max(visitor_counts, key=visitor_counts.get)
        most_visitor = None
        most_tally = 0
        for visitor in self.visitors():
            tally = 0 #tally to reset per each visitor
            for trip in self.trips():
                if visitor == trip.visitor:
                    tally += 1
            if most_tally < tally:
                most_tally = tally 
                most_visitor = visitor 
        return most_visitor
    
    @classmethod 
    def most_visited(cls):
        most_tally = 0 
        most_park = None
        #look at each national park - use NationalPark.all and a loop
        for park in NationalPark.all:
            #get the number of visits for current park - park.total_visits()
            num_visits = park.total_visits()
            #compare to current most visited
            if(num_visits > most_tally):
                most_tally = num_visits 
                most_park = park 
        return most_park

    @property 
    def name(self):
        return self._name 
    @name.getter 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, val):
        if not hasattr(self, 'name'):
            self._name = val


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
    @start_date.getter 
    def start_date(self):
        return self._start_date 
    @start_date.setter 
    def start_date(self, val):
        if isinstance(val, str) and len(val) >= 7:
            self._start_date = val
        #if debugging by hand/with ipdb you might want to put in the exceptions regardless of tests
        else:
            raise Exception

    @property 
    def end_date(self):
        return self._end_date 
    @end_date.getter 
    def end_date(self):
        return self._end_date 
    @end_date.setter 
    def end_date(self, val):
        if isinstance(val, str) and len(val) >= 7:
            self._end_date = val
        else: 
            raise Exception

class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        return[trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        visits = [trip for trip in self.trips() if trip.national_park == park]
        return len(visits)
    

    @property 
    def name(self):
        return self._name 
    @name.getter 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, val):
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val
class NationalPark:

    def __init__(self, name):
        self.name = name
        
    #append trips that match the current national park (self)
    def trips(self):
        #filter through all trips, and finding matching trips 
        # matching_trips = []
        # for trip in Trip.all:
        #     if(trip.national_park == self):
        #         matching_trips.append(trip)
        # return matching_trips
        return [trip for trip in Trip.all if trip.national_park == self]
    
    
    def visitors(self):
        #find all the relevant trips
        #extract specifically the visitor value 
        return list(set([trip.visitor for trip in self.trips()]))
    
    def total_visits(self):
        # find all trips for the current national park (self)
        if(len(self.trips()) == 0):
            return 0
        else: 
            return len(self.trips())
    
    def best_visitor(self):
        #get all trips to current park (self.trips())
        #get all unique visitors to park (self.visitors())
        
        greatest_visitor = None 
        greatest_visitor_count = 0
        #for each unique visitor
        for cur_visitor in self.visitors():
            #count the number of trips in self.trips() with said visitor
            cur_count = 0
            for trip in self.trips():
                if trip.visitor == cur_visitor:
                    cur_count += 1
            #compare to previous count for previous unique visitor
            #if count is greater, update greatest visitor
            if(cur_count > greatest_visitor_count):
                greatest_visitor_count = cur_count 
                greatest_visitor = cur_visitor
        return greatest_visitor            

    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, new_name):
        if(not hasattr(self, 'name') and isinstance(new_name, str) and len(new_name) >= 3):
            self._name = new_name 
        # else: 
        #     raise ValueError('something went wrong')

    def __repr__(self):
        return f'<NationalPark name={self.name} />'

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
    def start_date(self, new_start_date):
        if(isinstance(new_start_date, str) and len(new_start_date) >= 7):
            self._start_date = new_start_date
        # else:
        #     raise ValueError('something went wrong with the start_date')

    @property 
    def end_date(self):
        return self._end_date 
    @end_date.setter 
    def end_date(self, new_end_date):
        if(isinstance(new_end_date, str) and len(new_end_date) >= 7):
            self._end_date = new_end_date

    @property 
    def visitor(self):
        return self._visitor 
    @visitor.setter 
    def visitor(self, new_visitor):
        if(isinstance(new_visitor, Visitor)):
            self._visitor = new_visitor

    @property 
    def national_park(self):
        return self._national_park 
    @national_park.setter 
    def national_park(self, new_national_park):
        if(isinstance(new_national_park, NationalPark)):
            self._national_park = new_national_park

    def __repr__(self):
        return f'<Trip start={self.start_date} end={self.end_date} park={self.national_park.name} visitor={self.visitor.name} />'

class Visitor:

    def __init__(self, name):
        self.name = name
        
    def trips(self):
        # look through all of the trips (Trip.all)
        # does the current trip we're looking at...trip.visitor == self 
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        # look through this visitor's trips (self.trips())
        # isolate the national park 
        return list(set([trip.national_park for trip in self.trips()]))
    
    def total_visits_at_park(self, park):
        pass

    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, new_name):
        #type str, length 1-15 
        if(isinstance(new_name, str) and 1 <= len(new_name) <= 15):
            self._name = new_name 
        # else:
        #     raise ValueError('Name must be string of length 1-15')


    def __repr__(self):
        return f'<Visitor name={self.name} />'
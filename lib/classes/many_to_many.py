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
        if(not hasattr(self, 'name') and len(name) > 3):
            self._name = name 
        else: 
            raise Exception
        
    def trips(self):
        # all_trips = []
        # for trip in Trip.all:
        #     if(trip.national_park == self):
        #         all_trips.append(trip)
        # return all_trips
        return [trip for trip in Trip.all if trip.national_park == self]

    
    def visitors(self):
        # all_visitors = []
        # for trip in self.trips():
        #     all_visitors.append(trip.visitor)
        # return all_visitors
        return list({ trip.visitor for trip in self.trips() })
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        most_visits = 0 
        most_visitor = None 
        #look at each visitor - self.visitors()
        for visitor in self.visitors():
            #get # of trips visitor made to current park - total_visits_at_park(self)
            visitors_visits = visitor.total_visits_at_park(self)
            if(most_visits < visitors_visits):
                print('entered if')
                most_visits = visitors_visits 
                most_visitor = visitor 

        return most_visitor 
    
    @classmethod
    def most_visited(cls):
        #cls.all -> all instances of the national park 
        #1st park -> total_visits()
        #2nd park -> total_visits()
        #3rd park -> total_visits()
        return max(cls.all, key = lambda park: park.total_visits())



# def valid_date(date):
#     months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#     ends = ["st", "nd", "rd", "th"]
#     date_arr = months.split() 
#     if (date_arr[0] not in months):
#         return False 
#     if (date_arr[0][-2] not in ends):
#         return False 
#     if (date)

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
        if(isinstance(start_date, str) and len(start_date) >= 7 and isinstance(start_date, str)):
            self._start_date = start_date 
        else: 
            raise Exception
    #if using regex 
    #1. first word is either Jan, Feb, March, etc.
    #2. second word starts with either 1 or 2 numbers
    #3. second word ends with either 'nd', 'st, 'rd', 'th'

    @property 
    def end_date(self):
        return self._end_date 
    @end_date.setter
    def end_date(self, end_date):
        if(isinstance(end_date, str) and len(end_date) >= 7):
            self._end_date = end_date
        else: 
            raise Exception


class Visitor:

    def __init__(self, name):
        self.name = name

    @property 
    def name(self):
        return self._name 
    @name.setter 
    def name(self, name):
        if(isinstance(name, str) and 1 <= len(name) <= 15):
            self._name = name 
        else: 
            raise Exception
        
    # visitor -> trips -> national_parks
    def trips(self):
        # all_trips = [] 
        # for trip in Trip.all: #look through all trips
        #     if(trip.visitor == self): #if trips visitor matches current visitor instance
        #         all_trips.append(trip) #add to list 
        # return all_trips
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        # all_parks = []
        # for trip in self.trips():
        #     all_parks.append(trip.national_park)
        # return list(set(all_parks))
        return list({trip.national_park for trip in self.trips()})

    
    def total_visits_at_park(self, park):
        # #keep count of the number of visits for the park 
        # visits = 0 
        # #iterate over self.trips() (all of the current visitor's trips)
        # for trip in self.trips():
        #     #if the current trip matches the park argument
        #     if(trip.national_park == park):
        #         visits += 1 
        # return visits 
        return len([trip for trip in self.trips() if trip.national_park == park])
    
    
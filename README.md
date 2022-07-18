# flounder-lodgings
Hotel management service for me to learn whatever I think is cool in Python. Currently run on command line, might transition to web app.
##### Menu so far:
* Make reservation (currently only shows unoccupied rooms)
* Look at all rooms regardless of status
* Edit reservation
##### To-Do:
- [x] Add functionality for date tracking by using consensus date format and adding feature to subtract dates (overloaded op) to see if the reservation has expired
- [x] Add featured to automatically mark room as 'CLEANING' for one day after reservation has expired
     ~~Add serialization for room class to put into database~~
- [ ] Encryption (?) for user so that they can only edit their own reservation. Maybe for time being generate key for user and it tracks their rooms and lets them edit reservations when entered.
  - [ ] Create another table for users and have the main key or whatever the term is in SQL be the password generated, and use that to link to room table
- [ ] Add search feature to satisfy various requests for room accomodations (Partially complete, can currently search for rooms with >= bed count, <= price, and > date
  - [ ] Need to add functionality to show rooms that satisfy some of the requirements if no exact matches are found.
  - [ ] Need to add functionality for rooms to be booked for multiple ranges, not just up to a single date. 

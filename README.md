# flounder-lodgings
##### Menu so far:
* Make reservation (currently only shows unoccupied rooms)
* Look at all rooms regardless of status
* Edit reservation
##### To-Do:
* Add functionality for date tracking by using consensus date format and adding feature to subtract dates (overloaded op) to see if the reservation has expired
* Add featured to automatically mark room as 'CLEANING' for one day after reservation has expired
* Add serialization for room class to put into database
* Encryption (?) for user so that they can only edit their own reservation. Maybe for time being generate key for user and it tracks their rooms and lets them edit reservations when entered.

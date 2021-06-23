# meeting-room-reservation

1. Run git clone https://github.com/shubham1604/meeting-room-reservation.git in directory of your choice

2. Assuming, you already have a virtual environment set up, activate it using the following command:
    
    source env_folder/bin/activate
    where env_folder = name of your virtual environment folder 

3. Navigate to the project directory using cd /meeting-room-reservation/

4. Run pip install -r requirements.txt to install project dependancies

5. For convinience a sample SQLITE database file has been included in the project which contains some test data.  

6. Run python manage.py runserver to start the development server. 

7. Hit http://localhost:8000/ in your browser to list all rooms.

8. Hit http://localhost:8000/reservations/1/ to view reservations of room number 1. Replace 1 with any room number(refer step 7) you wish to see the reservations of.(Currently reservations are for room number 1 and 2 only)

9. Hit http://localhost:8000/reservations/update/1/ to update the reservation with the reservation id 1. Current preset reservation ids are (2,3,4,5,7 etc).

10. Test admin user credentails :
          username : testuser1
          password : testpassword
          
          username : testuser2
          password : testpassword

11. Only the user who has created the reservations will be able to edit or delete it in logged in state. 

12. The sample database here is only for your convenience. Feel free to create admin users of your own by running the following command and entring valid information.

      python manage.py createsuperuser

          
          

# Interview Tasks

The project you have here is a web application that allows an HR department to manage candidates and schedule interviews for those candidates. The application is used by the HR department through the Django admin interface. There is a REST API exposed that is used by other partners & applications to query the data. 

1. Get the project working on your local machine. The information in the README.md file should be enough to get you up and running. 

2. The HR department can manage candidates from the Django admin interface. They can't manage interviews for those candidates from the admin interface though. Make sure they can manage interface in the best possible manner from the admin interface. 

3. Fix the issue with the frontend where the candidates aren't loading correctly

4. The candidates API (exposed under /api/candidates) needs a new feature: a partner wants to query the candidates by firstname or lastname or by a general query parameter. Some use cases:
   /api/candidates?last_name=sparrow
   /api/candidates?first_name=jack
   /api/candidates?query=test

5. Allow the user to search candidates by firstname or lastname from the UI. 

6. From the frontend we want to allow a user to download an ICS file with all the candidate's interviews. 

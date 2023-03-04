# Django-Job-App
An Job Application Based on Django framework

This Project contains:- 
    1. Main Project : jobapp
    2. 1st app : hire(for employers)
    3 . 2nd app : jobs(for users/candidate)
--------------------------------------------------------------------

I created this project from scratch.
I donot have experience in Frontend , so i kept it simple , but i m having some experience in Django Backend.
I devloped 3 Projects on Django including this one.
--------------------------------------------------------------
to create a super user or an administrator, steps are below:-

1.   python3 manage.py createsuperuser
2 .  Enter Required feilds asked in CLI.

--------------------------------------------------------------
I created 4 Models named:
  1. jobPost :- contains data of job listed on website 
  2. accepted :- contains accepted candidates data
  3. deleted :- contains reject candidtae's data
  4. docs :- contains applicant's documents with their names
  
--------------------------------------------------------------

Now , whenever Employer rejects any candidate , it get stored in deleted model and will be removed from Manage applications tab i.e. will be deleted from docs model
and whenver Employer accepts the candidate application , it will be stored in accepted model , and got deleted from docs model.

==========================================================================================

There is an timout for logged in users also.

===========================================================================================

This Project uses : sqlite3 for database 

----------------------------------------------------------------------------------------
Thank you!!👍👍

BUBBLING Software Engineer Task
===============================

As part of a small organization i want to give my users the ability to organize and exchange notes!


Mission
=======

Create the following API:
-------------------------
Users can create groups and join new ones 
All the available groups are listed through an endpoint
User specific groups are also listed through an endpoint
A user can be part of multiple groups
User can post notes withing the group
User can post a note to a user of a group (personal note)
Only users that belong to a group can see the notes in the group (group notes)
Only the user that the note is referred to can see the note


Develoment Requirements
-----------------------
Option A: using Python 3.8.6, Django 3.1.4 and DRF
Option B: using Python 3.8.6, FastAPI 0.63 

Database: SQLite or Postgres whatever is more convenient


Deliverable
===========
The outcome is a git(GitHub or Gitlab) repo with your project containing explicit instruction on how it can be run locally.
Document your design choices and anything else you think we need to know in the PR description.
You should deliver your solution as a Pull Request in your repo. 
Frontend is completely optional. Tests (unit tests, integration tests or both?) are a must.


Resources
=========
1. `Django`: https://www.djangoproject.com/
2. `DRF`: https://www.django-rest-framework.org/
3. `FastAPI`: https://fastapi.tiangolo.com/
4. `HTTP statuses`: https://httpstatuses.com/
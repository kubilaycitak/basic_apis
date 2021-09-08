# API with DB Connection
### Purpose
- The main goal here is to get data from a database and preparing it to be used via the API.
### Usage
- You can run the .py file to run it.

    ``` commandline
    $ python api_db.py
    ```
- You can visit addresses like;
-- http://127.0.0.1:5000/api/v1/resources/matches/all
-- http://127.0.0.1:5000/api/v1/resources/matches?team_1=G2
-- http://127.0.0.1:5000/api/v1/resources/matches?t1_world_rank=1&team_2=MOUSESPORTS

### Content
- Data to be used is prepared as a .db file, and the file has some endpoints that you can use to access this data. You can find those endpoints in the code.
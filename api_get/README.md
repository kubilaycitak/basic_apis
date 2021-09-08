# API with Dictionary Data
### Purpose
- HTTP (Hypertext Transfer Protocol) is the primary means of communicating data on the web. HTTP implements a number of “methods” which tell which direction data is moving and what should happen to it. The two most common are GET, which pulls data from a server, and POST, which pushes new data to a server. In this file, we will be taking a look at GET method.
### Usage
- You can run the .py file to run it.

    ``` commandline
    $ python api_get.py
    ```

- You can visit adresses such as;
-- http://127.0.0.1:5000
-- http://127.0.0.1:5000/api/v1/resources/matches/all
-- http://127.0.0.1:5000/api/v1/resources/matches?id=2

etc.

### Content
- Data to be used is prepared in the code as list of dictionaries and the file has some endpoints that you can use to access this data. You can find those endpoints in the code.

# CS:GO Matches Data with Basic API Types
- In general, APIs let your product or service communicate with other products and services without having to know how they’re implemented. We can consider an API like a messenger that delivers your request to the provider that you’re requesting it from and then delivers the response back to you.
- In these APIs, some match records of the video game CS:GO is used as data.
### Content
- You can find 4 API files with minor different charasteristics above. The main goal of this repository is to give you entry level insights about APIs.
- With api_get, api_db and api_csv you can access the CS:GO data while api_token does not contain that data and specifies only key authentication.
### Setup
- You can install required setups on the directory from pip;

    ``` commandline
    $ pip install -r requirements.txt
    ```
### Usage
- You can simply start command line, go to the API's directory and run the .py file. For example when you are in the directory, you can run the following command;

    ``` commandline
    $ python api_db.py
    ```
- Then go to endpoints that are specified on the command line and the task itself.
# API with Key Authentication
### Purpose
- Sending username and password on every request can be seen as a security risk even if HTTPS is being used, because the client must store these information unencrypted before sending them with requests. As a solution, using a key to authenticate requests could do the trick. 
- Keys are usually issued with an expiration time, after which they become invalid and a new key must be obtained.
### Usage
- You can run the .py file to run it.

    ``` commandline
    $ python api_token.py
    ```
- When you visit the address 'http://127.0.0.1:5000/protected', you will notice that you need a key to access this page. But when you visit 'http://127.0.0.1:5000/unprotected' you will not have any problems accessing that page. You can also log in, get your key and access the protected page via 'http://127.0.0.1:5000/login' with the password of 'admin'. After copying your key from this page, you can go back to the protected page and add "?token=<token_str>" and access the protected page.
### Content
- A key is created and being asked in the code in order to keep the process going, which makes exchanging sensitive data more secure. The file has some endpoints that you can use to access this data. You can find those endpoints in the code.
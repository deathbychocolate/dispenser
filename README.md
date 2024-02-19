# How do I run it?
- Developers (you should have python3 and pipenv installed):
    - Run the following at the root of the project to install all the dependencies: ```pipenv install --dev```
    - Run the following at the root of the project: ```python3 dispenser/main.py```.

# How does it work?
It works like any other API. Simply make a call to any of the following URIs:
- ```http://127.0.0.1:5000/```
- ```http://127.0.0.1:5000/price```
- ```http://127.0.0.1:5000/products```
- ```http://127.0.0.1:5000/purchase```

# Tips and tricks?
Try and visit the test suite in the following directory: ```dispenser/test``` using the following terminal command ```pytest```
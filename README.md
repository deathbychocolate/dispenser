# How do I run it?
- Developers (you should have python3 and pipenv installed):
    - Run the following at the root of the project to install all the dependencies: ```pipenv install --dev```
    - Run the following in inner dispenser folder of the project: ```python3 main.py```.

# How does it work?
It works like any other API. Simply make a call to any of the following URIs:
- ```http://127.0.0.1:5000/```
- ```http://127.0.0.1:5000/price```
- ```http://127.0.0.1:5000/products```
- ```http://127.0.0.1:5000/purchase```

# Tips and tricks?
Try and visit the test suite in the following directory ```dispenser``` and use the following terminal command ```pytest test/```
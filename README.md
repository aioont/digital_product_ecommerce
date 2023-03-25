# Digital Product E-commerce

Digital Product E-commerce (DPE) is a software platform to buy and sell digital products. This web application allows users to buy digital products and download it.This is a simple MultiVendor e-commerce website built with Django (Ptyhon) and Stripe is added as payment processor.In this website, Vendors (Stores) can register and add their products.And Users can visit the product and order by paying with Debit/Credit Card (Stripe is Used).

```diff
- Digital Product E-commerce is under development phase.
```

## Table of contents
* [Pre-Requisites](#Pre-Requisites)
* [Technologies Used](#Technologies-Used)
* [Setup and Installation](#Setup-and-Installation)
* [Example](#Example-For-windows)
* [Screenshot](#Screenshot)

## Pre-Requisites
1. Install Git Version Control
[ https://git-scm.com/ ]

2. Install Python Latest Version
[ https://www.python.org/downloads/ ]

3. Install Pip (Package Manager)
[ https://pip.pypa.io/en/stable/installing/ ]

*Alternative to Pip is Homebrew*

## Technologies Used
Django framework by python for admin panel and backend HTML,CSS and JavaScript for web front-end. Stripe is added as payment processor.

## Features of this Project

### A. Admin Users Can
1. Manage Category (Add, Update, Filter and Delete)
2. Manage Products (Add, Update, Filter and Delete)
3. Manage Users (Update, Filter and Delete)
4. Manage Orders (View and Process)

### B. Vendors Can
1. Add Products
2. Update Profile
3. Gets Notification When an Order is made by Users
4. Get Orders and Manage Them

### C.  Users Can Can
1. Add to Cart
2. Pay with Debit/Credit Card and Order
3. While Checkout, User should give the address to keep as record
4. Get Email Notification about the confirmation of the order

## Setup and Installation

**1. Create a Folder where you want to save the project**

**2. Create a Virtual Environment and Activate**

Install Virtual Environment First
```
$  pip install virtualenv
```

Create Virtual Environment

For Windows
```
$  python -m venv venv
```
For Mac
```
$  python3 -m venv venv
```

Activate Virtual Environment

For Windows
```
$  source venv/scripts/activate or goto venv/Scripts enter "cmd" then "activate"
```

For Mac
```
$  source venv/bin/activate
```

**3. Clone this project**
```
$  git clone https://github.com/aioont/digital_product_ecommerce.git
```

Then, Enter the project
```
$  cd digital_product_ecommerce
```

**4. Install Requirements from 'requirements.txt'**
```python
$  pip install -r requirements.txt
```

**5. Add the hosts**

- Got to settings.py file 
- Then, On allowed hosts, Add [‘*’]. 
```python
ALLOWED_HOSTS = ['*']
```
*No need to change on Mac.*


**6. Now Run Server**

Command for PC:
```python
$ python manage.py runserver
```

Command for Mac:
```python
$ python3 manage.py runserver
```

**7. Login Credentials**

Create Super User (Admin)

Command for PC:
```
$  python manage.py createsuperuser
```

Command for MAC:
```
$  python3 manage.py createsuperuser
```
Then Add Email, Username and Password

## Example-For windows

 *Install python and git

1. Initial Setup - In terminal
```
cmd
mkdir dpe
cd dpe
pip3 install virtualenv
virtualenv -p python3 env
source env/Scripts/activate or open cmd in env/Scripts and run "activate"
cd ../..
```
2. Install django and dependencies
```
pip install django
git clone https://github.com/aioont/digital_product_ecommerce.git
cd digital_product_ecommerce
pip install -r requirements.txt
```
3. Run and view application by entering > http://127.0.0.1:8000/ in browser
```
python manage.py runserver
```
4. Create Super User (Admin)
```
python manage.py createsuperuser
```
Use this credentials to login into http://127.0.0.1:8000/admin

## Screenshot

![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_43_22](https://user-images.githubusercontent.com/97335084/227714395-1c552a75-cac6-4213-a4fd-722fd01c7414.png)![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_47_19](https://user-images.githubusercontent.com/97335084/227714427-3cb659bf-671a-4d2e-ba45-2676c6f58c98.png)

![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_45_13](https://user-images.githubusercontent.com/97335084/227714423-94fb51db-baad-4f9e-af0c-e2feea160dcb.png)![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_45_31](https://user-images.githubusercontent.com/97335084/227714456-f808c1f9-3d66-4514-bde0-81aa1c0d900f.png)

![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_46_32](https://user-images.githubusercontent.com/97335084/227714515-0563f92a-560a-4cf4-bbc5-3b2b959078aa.png)

![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_46_59](https://user-images.githubusercontent.com/97335084/227714517-51e630b7-816c-4931-8304-ae60295bf119.png)
![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_47_30](https://user-images.githubusercontent.com/97335084/227714521-b1a4f3e8-740a-4dfa-aacb-defaee4c0f97.png)
![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_47_53](https://user-images.githubusercontent.com/97335084/227714524-4a82f0e2-ddd5-41fc-8af6-31ac4ab756a4.png)
![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_48_35](https://user-images.githubusercontent.com/97335084/227714528-dcaab088-7862-43a0-8d9e-bec285197515.png)
![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_48_43](https://user-images.githubusercontent.com/97335084/227714534-cb0dc568-93a8-413b-8d7e-aa2a0d5bb443.png)
![Home _ Digital Product Ecommerce - Google Chrome 25-03-2023 16_49_02](https://user-images.githubusercontent.com/97335084/227714541-50eebb8b-ce42-4302-b058-e0cd1d20d3e5.png)

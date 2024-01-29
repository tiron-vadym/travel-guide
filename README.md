# Travel Guide

The Travel Guide project is a web application designed to provide users with comprehensive information about various cities, attractions, routes, and user reviews worldwide. It serves as a platform for travelers to discover new destinations, plan their trips, and share their experiences with others.

## Installing

Python3 must be already installed

```shell
git clone https://github.com/tiron-vadym/travel-guide.git
cd travel_guide
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```

#### 1. Use the following command to load prepared data from fixture to test and debug your code <br>

`python manage.py loaddata taxi_service_db_data.json`

#### 2. After loading data from fixture you can use following superuser (or create another one by yourself)

  - Login: `admin.user`
  - Password: `1qazcde3`


## Demo
![img.png](img.png)
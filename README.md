# Django
Django hello world

# Requirements 
```
python 3.7
~/.aws/credentials
```

# Steps for installation

## Windows

```
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```

For running server
```
python manage.py runserver
```

Demo URL
```
http://127.0.0.1:8000/AWS/hello/
```

##Page in Development
### List of instances(us-east-1)
```
http://127.0.0.1:8000/AWS/instances
```

### List of vpcs(us-east-1)
```
http://127.0.0.1:8000/AWS/aws_vpcs
```
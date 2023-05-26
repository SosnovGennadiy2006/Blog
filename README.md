# Blog

A simple blog system based on `python3.9.2` and `Django4.2.1`, also project uses `MySQL8.0`.

## Main Features:
- Articles support html markdown, codesnipets and LaTeX.
- Profile system with user avatars.

## Installation:
Change MySQL client from `pymysql` to `mysqlclient`, more details please reference [pypi](https://pypi.org/project/mysqlclient/) , checkout preperation before installation.

Install via pip: `pip install -Ur requirements.txt`

If you do NOT have `pip`, please use the following methods to install:
- OS X / Linux, run the following commands: 

    ```
    curl http://peak.telecommunity.com/dist/ez_setup.py | python
    curl https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python
    ```

- Windows：

    Download http://peak.telecommunity.com/dist/ez_setup.py and https://raw.github.com/pypa/pip/master/contrib/get-pip.py, and run with python. 

## Run

Modify `DjangoBlog/setting.py` with database settings, as following:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST': 'host',
        'PORT': 3306,
    }
}
```

### Create database
Run the following command in MySQL shell:
```sql
CREATE DATABASE `blog`;
```

Run the following commands in Terminal:
```bash
python manage.py makemigrations
python manage.py migrate
```  

### Create super user

Run command in terminal:
```bash
python manage.py createsuperuser
```

### Collect static files
Run command in terminal:
```bash
python manage.py collectstatic --noinput
```

### Getting start to run server
Execute: `python manage.py runserver`

Open up a browser and visit: http://127.0.0.1:8000/ , the you will see the blog.
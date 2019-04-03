Playing with flask
https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates

Currently on Followers

to run

```
export FLASK_APP=microblog.py
export FLASK_DEBUG=1
/path/to/anaconda/bin/flask run
```

When models change, remember to
```
flask db migrate -m "some commit message"
flask db upgrade
```

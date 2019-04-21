
## Email

`mail.py` is a script for sending user an email notification.
It can be either used as a standalone script or as a python module:

```sh
./mail.py --to jialin@gatech.edu --resid test1
```

In python:

```python3
import mail
mail.send("jialin@gatech.edu", "test1")
```



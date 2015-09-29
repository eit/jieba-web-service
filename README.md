# jieba-web-service
A web service for Chinese text segmentation using Jieba project.

This project based on falcon framework and gunicorn

# Installation
We have to install libarary by pip.
If you don't have it, please install it first.

```bash
$ pip install falcon
$ pip install gunicorn
$ pip install jieba
```

# Usage
```bash
$ sh start.sh
```
Then you will have started the service jieba-segmentation with http://localhost:8000/jieba

(If you want to change the path of service, you could edit the file "app.py".)

You have to use 'POST' request and send the content with RAW. Then you will recieve response result with json format.

Enjoy it.

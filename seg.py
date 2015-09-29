#encoding=utf-8
import falcon
import jieba
import json

class Resource(object):
    def on_post(self, req, resp):
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body')

        #seg_list = list(jieba.cut(body, cut_all=False))
        seg_list = list(jieba.cut_for_search(body))
        resp.body = json.dumps(seg_list);
        #resp.body = "/ ".join(seg_list)
        resp.status = falcon.HTTP_200

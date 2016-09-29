import falcon
import jieba
import json
import jieba.posseg as pseg
import posSeg

class Resource(object):
    def on_post(self, req, resp):
        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body')

        #seg_list = list(jieba.cut(body, cut_all=False))
        words = pseg.lcut(body);
        result=list();
        for word, flag in words:
            tmp=posSeg.posSeg(word,flag)
            result.append(tmp.__dict__)
        resp.body=json.dumps(result)
        resp.status = falcon.HTTP_200

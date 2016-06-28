#encoding=utf-8
import falcon
import jieba
import json
import jieba.analyse

class Resource(object):
	def on_post(self, req, resp):
		size = req.get_param_as_int('topk',required=True)
		data = req.get_param('data',required=True)
		#pos = req.get_param_as_list('pos',required=True)
		#body = req.stream.read()
		#if not body:
		#	raise falcon.HTTPBadRequest('Empty request body')

		
		pos = ['n','v','a']
		tags = jieba.analyse.extract_tags(data,topK=size,withWeight=True,allowPOS=pos)
		resp.body = json.dumps(tags);
		#resp.body = "/ ".join(seg_list)
		resp.status = falcon.HTTP_200
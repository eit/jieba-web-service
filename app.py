# jieba app
import falcon
import seg
import tag
import pos
api = application = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
seg = seg.Resource()
api.add_route('/jieba', seg)
tag = tag.Resource()
api.add_route('/jieba/tag', tag)
pos = pos.Resource()
api.add_route('/jieba/pos', pos)

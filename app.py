# jieba app
import falcon
import seg
import tag
api = application = falcon.API()
api.req_options.auto_parse_form_urlencoded = True
seg = seg.Resource()
api.add_route('/jieba', seg)
tag = tag.Resource()
api.add_route('/jieba/tag', tag)


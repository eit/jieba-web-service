# jieba app
import falcon
import seg
import tag

api = application = falcon.API()
seg = seg.Resource()
api.add_route('/jieba', seg)
tag = tag.Resource()
api.add_route('/jieba/tag', tag)


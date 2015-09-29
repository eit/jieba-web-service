# jieba app
import falcon
import seg

api = application = falcon.API()
seg = seg.Resource()
api.add_route('/jieba', seg)



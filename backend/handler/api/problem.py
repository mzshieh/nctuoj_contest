import tornado
import tornado.gen

from req import Service
from req import ApiRequestHandler

class Problems(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self):
        err, res = yield from Service.Problem.get_problem_list()
        if err:
            self.render(err)
        else:
            self.render(res)

    @tornado.gen.coroutine
    def post(self):
        pass

class Problem(ApiRequestHandler):
    @tornado.gen.coroutine
    def get(self, id):
        pass

    @tornado.gen.coroutine
    def put(self, id):
        pass
        

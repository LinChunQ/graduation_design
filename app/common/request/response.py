class ResponseHandler:
    @staticmethod
    def success(data=None, msg=""):
        return {"code": 200, "data": data, "msg": msg}, 200

    @staticmethod
    def error(code, msg="", status_code=200):
        return {"code": code, "msg": msg}, status_code
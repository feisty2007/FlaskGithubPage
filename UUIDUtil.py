
import uuid

class UUIDUtil:
    def gen(self):
        uid = str(uuid.uuid4())
        #suid = ''.join(uid.split('-'))
        return uid

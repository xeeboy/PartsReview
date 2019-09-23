from getdb import CORPID, SECRET, AGENTID

from json import dumps, loads
from requests import get, post


class SmsWechat:
    """调用api向企业微信的自建应用程序(agentid=1000002)发送文本、图片或者文件消息"""
    def __init__(self):
        self.base_url = "https://qyapi.weixin.qq.com/cgi-bin"
        self.token = self._get_token()

    def _get_token(self):
        url_arg = '/gettoken?corpid={}&corpsecret={}'.format(CORPID, SECRET)
        url = self.base_url + url_arg
        r = get(url)
        return loads(r.text)['access_token']

    def _get_media_id(self, msg_type, file_obj):
        """file_obj is such as open(file_path, 'rb')
        or a BytesIO().getvalue;
        """
        url = self.base_url + "/media/upload?access_token={}&type={}".format(self.token, msg_type)
        data = {"media": file_obj}
        r = post(url=url, files=data)
        return r.json()['media_id']

    def _gen_msg(self, msg_type, contents, file_obj):
        """
        msg_type::str 'text','image','file'
        contents配合msg_type='text'使用
        file_obj配合msg_type='image'或'file'使用
        """
        base_string = '''{
        "touser": '@all', 
        "msgtype": msg_type, 
        "agentid": AGENTID, 
        msg_type: {'%s': '%s'},
        "safe": 0}'''
        if msg_type == 'text':
            values = base_string % ('content', contents)
        else:
            media_id = self._get_media_id(msg_type, file_obj)
            values = base_string % ('media_id', media_id)
        data = eval(values)
        return bytes(dumps(data), 'utf-8')

    def send_message(self, msg_type, contents=None, file_obj=None):
        post_msg = self._gen_msg(msg_type, contents, file_obj)
        url = self.base_url + '/message/send?access_token={}'.format(self.token)
        post(url, data=post_msg)


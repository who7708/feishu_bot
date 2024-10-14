import base64
import hashlib
import hmac
import time


def gen_sign(secret):
    """
    生成签名
    :return:
    """
    timestamp = time.time()
    # 拼接timestamp和secret
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    hmac_code = hmac.new(string_to_sign.encode("utf-8"), digestmod=hashlib.sha256).digest()
    # 对结果进行base64处理
    sign = base64.b64encode(hmac_code).decode('utf-8')
    return {
        "sign": sign,
        "timestamp": timestamp,
    }

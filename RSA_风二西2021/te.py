from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def decrypt_message(encrypted_message, key):
    # 使用AES解密
    cipher = AES.new(key, AES.MODE_EAX, nonce=encrypted_message[:16])
    data = cipher.decrypt(encrypted_message[16:])
    return data


# 示例用的密钥，实际使用时应该是一个安全的随机字节序列
key = b'1234567812345678'

# 假设你从RabbitMQ接收到的是一个base64编码的字符串
encrypted_message_b64 = 'AQAPM...'  # 这里应该是完整的base64编码的加密消息

# 解码base64字符串
encrypted_message = base64.b64decode(encrypted_message_b64)

# 解密消息
decrypted_message = decrypt_message(encrypted_message, key)

print("Decrypted message:", decrypted_message)
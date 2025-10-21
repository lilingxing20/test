"""
hashlib 模块提供了许多常见的加密哈希算法，以使用如 MD5、SHA-1、SHA-256 等算法来计算字符串或二进制数据的哈希值。
"""

import hashlib


md5 = hashlib.md5()
md5.update("天行健，君子以自强不息，不坠青云之志。".encode("utf-8"))
print(md5.hexdigest())   # ecaaa0166007ab1a531e193e2e786c34

md5 = hashlib.md5()
md5.update("天行健，".encode("utf-8"))
md5.update("君子以自强不息，".encode("utf-8"))
md5.update("不坠青云之志。".encode("utf-8"))
print(md5.hexdigest())   # ecaaa0166007ab1a531e193e2e786c34

sha1 = hashlib.sha1()
sha1.update("顺为凡，逆则仙，只在心中一念间。".encode("utf-8"))
print(sha1.hexdigest())   # 9163af2ac6704ce57ea2d95686e61e70ab692e93

sha1 = hashlib.sha1()
sha1.update("顺为凡，逆则仙，".encode("utf-8"))
sha1.update("只在心中一念间。".encode("utf-8"))
print(sha1.hexdigest())   # 9163af2ac6704ce57ea2d95686e61e70ab692e93

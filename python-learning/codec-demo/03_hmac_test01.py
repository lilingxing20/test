"""
HMAC（Hash-based Message Authentication Code）是基于哈希函数的消息认证码，用于验证数据完整性和真实性。它结合密钥与哈希算法，确保消息未被篡改且来源可信。下文将从结构、应用场景、安全性等维度展开解析。
核心结构与工作原理

HMAC的计算公式为 HMAC(K， M) = H( (K⊕opad) || H( (K⊕ipad) || M ) )​，其中：
    K 是密钥，需在通信双方间安全共享；
    M 为原始消息；
    H 是哈希函数（如SHA-256）；
    opad（外层填充）和 ipad（内层填充）是固定值的字节填充。

流程分为两步：

    内层哈希：将密钥与ipad异或后拼接消息，进行哈希；
    外层哈希：将密钥与opad异或后拼接内层哈希结果，再次哈希。
    这种双层结构增强了对哈希碰撞攻击的防御能力。

应用场景与优势

    API请求认证
    如RESTful API中，客户端生成HMAC签名（密钥+请求参数），服务端验证签名合法性，防止参数篡改。
    令牌签名（如JWT）
    JWT使用HMAC对令牌头部和载荷签名，接收方通过验证签名确保令牌未被伪造。
    ​文件完整性校验​
    下载文件时附带HMAC值，用户通过本地密钥重新计算HMAC，比对结果判断文件是否被篡改。
    ​网络协议安全​
    TLS协议中可选HMAC作为数据完整性保护机制，抵御中间人攻击。

HMAC与普通哈希的区别
​特性​           HMAC                    普通哈希（如SHA-256）
密钥依赖       必须使用密钥               无密钥
安全性目标      完整性+认证               仅完整性
抗碰撞场景      抵御已知明文攻击           依赖哈希函数本身抗碰撞能力
典型攻击防御    防止密钥泄露前的消息伪造     无法防御恶意篡改（无密钥验证）

安全性考量
    ​密钥管理​
    密钥需通过安全渠道分发（如TLS加密传输），长度建议≥哈希输出长度（如SHA-256用256位密钥）。
    ​算法选择​
    优先选用SHA-256、SHA-3等抗碰撞性强的哈希算法，避免MD5、SHA-1等已破解算法。
    ​防重放攻击​
    在HMAC计算中加入时间戳或随机数（Nonce），避免攻击者重复发送旧消息。
    ​长度扩展攻击防御​
    HMAC的双哈希结构天然抵御此类攻击（如SHA-256的长度扩展漏洞被HMAC消解）。

典型问题与解决方案
    ​密钥泄露风险​
    采用硬件安全模块（HSM）或密钥管理系统（KMS）存储密钥。
    ​算法升级兼容性​
    在HMAC值中标注哈希算法类型（如alg:HS256），便于后续切换算法。
    ​性能瓶颈​
    对高频请求场景（如微服务通信），可预计算HMAC或使用硬件加速。
"""

import hmac
import hashlib


def generate_hmac(key: bytes, message: str) -> str:
    h = hmac.new(key, message.encode(), hashlib.sha256)
    return h.hexdigest()

# 验证HMAC
def verify_hmac(key: bytes, message: str, received_digest: str) -> bool:
    expected_digest = generate_hmac(key, message)
    return hmac.compare_digest(expected_digest, received_digest)


if __name__ == "__main__":

    # 此代码演示了 HMAC-SHA256 的生成与验证，关键点在于使用 hmac.compare_digest 避免时序攻击。
    key = b"my_secret_key"
    message = "Hello, World!"
    hmac_digest = generate_hmac(key, message)
    print(f"HMAC: {hmac_digest}")

    # 验证HMAC
    is_valid = verify_hmac(key, message, hmac_digest)
    print(f"Is HMAC valid? {is_valid}")

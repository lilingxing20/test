"""
Base64编码，是由64个字符组成编码集：26个大写字母A~Z，26个小写字母a~z，10个数字0~9，符号“+”与符号“/”。
Base64 实际上就是一种查表的编码方法，使用 64 个字符的字符集进行编码，字符集为：ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/
每个字符使用六位（2^6 = 64）表示，因此它能够表示 64 个不同的值。
Base64编码会把3字节的二进制数据编码为4字节的文本数据，长度增加33%，好处是编码后的文本数据可以在邮件正文、网页等直接显示。

Base64编码的基本思路是将原始数据的三个字节拆分转化为四个字节，然后根据Base64的对应表，得到对应的编码数据。
当原始数据凑不够三个字节时，编码结果中会使用额外的符号“=”来表示这种情况。
  - 编码过程：
    1) 将3字节的二进制数据分为4组，每组6位。
    2) 每个6位的二进制数据对应字符集中的一个字符。
    3) 如果原始数据不是3字节的倍数，用0填充最后一组。
    4) 将4个字符连接起来，得到编码后的文本数据。
    5) 如果编码后的文本数据长度不是4的倍数，用等号（=）填充。
    6) 编码后的文本数据就是最终的Base64编码结果。
  - 解码过程：
    1) 将Base64编码的文本数据分为4组，每组4个字符。
    2) 每个字符对应字符集中的6位二进制数据。
    3) 将4组二进制数据合并起来，得到3字节的二进制数据。
    4) 如果最后一组有等号（=），去掉等号填充的0位。
    5) 解码后的二进制数据就是最终的原始数据。

Base64编码将二进制数据转换为可打印字符，通过将数据分成6位二进制组并映射到64个字符实现。以字符串"hello ?"为例：
  - 编码过程：
    原始字符串： "hello ?"
    拆分数据:  将每个字符转换为ASCII码，然后每个ASCII码转换为8位二进制
      h(104) -> 01101000
      e(101) -> 01100101
      l(108) -> 01101100
      l(108) -> 01101100
      o(111) -> 01101111
      (32)  -> 00100000
      ?(63) -> 00111111
    原始二进制数据： 把每个字符的8位二进制拼接起来
      01101000 01100101 01101100 01101100 01101111 00100000 00111111
    二进制分组‌： 每3个字节（24位）分为4组，每组6位
      011010 000110 010101 101100 011011 000110 111100 100000 001111 110000 000000
    查base64的编码表映射：
      第一组： 011010 对应二进制是：26， 26对应base64字符为：a
      第二组： 000110 对应二进制是：6， 6对应base64字符为： G
      第三组： 010101 对应二进制是：21， 21对应base64字符为： V
      第四组： 01100 对应二进制是：44， 44对应base64字符为： s
      第五组： 11011 对应二进制是：27， 27对应base64字符为： b
      第六组： 00110 对应二进制是：6， 6对应base64字符为： G
      第七组： 11100 对应二进制是：60， 60对应base64字符为： 8
      第八组： 00000 对应二进制是：32， 32对应base64字符为： g
      第九组： 01111 对应二进制是：15， 15对应base64字符为： P
      第十组： 10000 对应二进制是：48， 48对应base64字符为： w
    填充等号：
      原始数据共7字节（56位），56 ÷ 6 = 9余2 → 需补4位0，形成第10组
      最终分组数：10 ÷ 4 ≈ 2.5 → 向上取整为3组（Base64要求总组数是4的倍数）
      补2个=填充符
    编码结果：
      aGVsbG8gPw==
    
  - 解码过程：
    编码结果： aGVsbG8gPw==
    移除填充符： 去掉等号填充的0位
      aGVsbG8gPw== -> aGVsbG8gPw
    字符映射：
      a→0, G→32, V→21, s→44, b→1, G→32, 8→60, g→48, P→56, w→64
    6位转二进制：
      a(26) -> 011010
      G(32) -> 010000
      V(21) -> 010101
      s(44) -> 011011
      b(1) -> 000001
      G(32) -> 010000
      8(60) -> 011100
      g(48) -> 011000
      P(56) -> 011100
      w(64) -> 011101
    重组为8位：
      01101000011001010110110001101100011011110010000000111111
    按8位分组：
      01101000 01100101 01101100 01101100 01101111 00100000 00111111
    转ASCII：
      01101000 -> h
      01100101 -> e
      01101100 -> l
      01101100 -> l
      01101111 -> o
      00100000 ->  
      00111111 -> ?
    解码结果：
      hello ?
"""

import base64


base64_encoding_table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def base64_encode(ss: str) -> str:
    """
    Base64编码函数
    :param ss: 原始字符串
    :return: Base64编码后的字符串
    """
    # 编码过程
    print("\n" + "-" * 20 + " 编码过程：" + "-" * 20)

    # 每个字符的ASCII码
    ascii_codes = [ord(c) for c in ss]
    # 每个字符的8位二进制
    binary_data = [bin(ord(c))[2:].zfill(8) for c in ss]
    # print(f"每个字符的8位二进制：{binary_data}")

    # 拆分字符串，字符转换为ASCII码和8位二进制
    print(f"拆分字符串，字符转换为ASCII码和8位二进制：")
    for s, ac, bd in zip(ss, ascii_codes, binary_data):
        print(f"{s}({ac}) -> {bd}")

    # 原始二进制数据
    raw_binary = "".join(binary_data)
    print(f"原始二进制数据：{raw_binary}")

    # 需要填充的0位：6 - (7*8 % 6) = 4
    pad_count = (6 - (len(raw_binary) % 6)) % 6
    print(f"需要填充的0位：{pad_count}")

    # 填充0位
    padded_binary = raw_binary + "0" * pad_count
    print(f"填充0位后的二进制数据：{padded_binary}")


    # 二进制分组：每3个字节（24位）分为4组，每组6位
    binary_groups = [padded_binary[i:i+6] for i in range(0, len(padded_binary), 6)]
    print(f"二进制分组：{binary_groups}")

    # 4个字符一组，每个字符对应base64编码表的一个字符
    base64_chars = [base64_encoding_table[int(group, 2)] for group in binary_groups]
    print(f"base64字符：{base64_chars}")

    # Base64要求总组数是4的倍数
    pad_char_count = 4 - (len(binary_groups) % 4)
    print(f"需要填充的等号数：{pad_char_count}")
    pad_base64_chars = base64_chars + ["="] * pad_char_count
    print(f"填充等号后的base64字符：{pad_base64_chars}")

    return "".join(pad_base64_chars)


def base64_decode(encoded: str) -> str:
    """
    Base64解码函数
    :param encoded: Base64编码后的字符串
    :return: 原始字符串
    """
    # 解码过程
    print("\n" + "-" * 20 + " 解码过程：" + "-" * 20)

    # 移除填充符
    encoded_no_pad = encoded.rstrip("=")
    print(f"移除填充符后的编码结果：{encoded_no_pad}")

    # 字符映射：将base64字符映射为6位二进制
    base64_binary = "".join([bin(base64_encoding_table.index(c))[2:].zfill(6) for c in encoded_no_pad])
    print(f"字符映射后的6位二进制：{base64_binary}")

    # 重组为8位：每8位一组
    reassembled_binary = [base64_binary[i:i+8] for i in range(0, len(base64_binary), 8)]
    print(f"重组为8位后的二进制数据：{reassembled_binary}")

    # 转ASCII：将每个8位二进制转换为ASCII码
    decoded_ascii = [int(group, 2) for group in reassembled_binary]
    print(f"转ASCII后的结果：{decoded_ascii}")

    # 转字符串：将ASCII码转换为字符
    decoded_chars = [chr(c) for c in decoded_ascii]
    print(f"转字符串后的结果：{decoded_chars}")

    return "".join(decoded_chars)


if __name__ == "__main__":
    # 原始字符串："hello ?"
    ss = "hello ?"
    print(f"\n原始字符串：{ss}")

    # 编码结果：aGVsbG8gPw==
    encoded = base64_encode(ss)
    print(f"自定义编码结果：【{encoded}】")
    encoded = base64.b64encode(ss.encode("utf-8")).decode("utf-8")
    print(f"标准编码结果：【{encoded}】")

    # 解码结果：hello ?
    decoded = base64_decode(encoded)
    print(f"自定义解码结果：【{decoded}】")
    decoded = base64.b64decode(encoded).decode("utf-8")
    print(f"标准解码结果：【{decoded}】")

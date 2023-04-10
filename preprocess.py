"""
@func:      对ZigBee传输到电脑的数据进行预处理
@time:      2023-04-09
@auther:    敖钰民
"""
"""
通信协议：Start(2bit) ID(2bit)  Len(2bit) Data(nbit) CRC(2bit) end(2bit)         
"""
import re


# CRC校验函数
def crc(data: bytes, poly: int = 0x07) -> int:
    """CRC-8."""
    crc_value = 0
    mask = (1 << len(bin(poly)) - 2) - 1  # Create a mask to limit the CRC size
    for byte in data:
        crc_value ^= byte
        for _ in range(8):
            if crc_value & 0x80:
                crc_value = (crc_value << 1) ^ poly
            else:
                crc_value <<= 1
        crc_value &= mask  # Apply the mask to limit the CRC size
    return crc_value


# zigbee数据解码函数
def zb_decode(data: str) -> dict:
    """
    Decode ZigBee data.
    :param data: 串口数据
    :return:  数据和数据长度
    """
    decode_data = {}
    # 起始和结束校验
    pattern = r'51(.*?)15'      # 定义正则表达式
    # 匹配符合条件的字符串
    result = re.findall(pattern, data)  # 返回匹配的数组，是一个字符串列表
    result = result[0]   # 取出第一个匹配的字符串
    # 解码id
    decode_data["device_id"] = int(result[:2])
    # 数据长度
    decode_data["data_len"] = int(result[2:4])
    # 数据
    decode_data["data"] = result[4:-2]
    # 校验和
    decode_data["crc"] = int(result[-2:])

    # crc校验
    if crc(decode_data["data"].encode()) == decode_data["crc"]:
        print("CRC校验正确")
        return decode_data
    else:
        print("CRC校验错误！")
        return None


if __name__ == '__main__':
    data = '511205aabbc0415'
    data = zb_decode(data)
    print(data["data"])

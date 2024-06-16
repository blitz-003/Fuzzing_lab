import math
import random
import struct
from typing import Any


def insert_random_character(s: str) -> str:
    """
    向 s 中下标为 pos 的位置插入一个随机 byte
    pos 为随机生成，范围为 [0, len(s)]
    插入的 byte 为随机生成，范围为 [32, 127]
    """
    pos = random.randint(0, len(s))
    random_char = chr(random.randint(32, 127))
    return s[:pos] + random_char + s[pos:]



def flip_random_bits(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 bitflip 与 random havoc 实现相邻 N 位翻转（N = 1, 2, 4），其中 N 为随机生成
    从 s 中随机挑选一个 bit，将其与其后面 N - 1 位翻转（翻转即 0 -> 1; 1 -> 0）
    注意：不要越界
    """
    byte_array = bytearray(s, 'utf-8')
    bit_length = len(byte_array) * 8
    if bit_length == 0:
        return s

    n = random.choice([1, 2, 4])
    bit_pos = random.randint(0, bit_length - n)

    for i in range(n):
        byte_index = (bit_pos + i) // 8
        bit_index = (bit_pos + i) % 8
        byte_array[byte_index] ^= 1 << bit_index

    return byte_array.decode('utf-8', errors='ignore')

import random

def arithmetic_random_bytes(s: str) -> str:
    """
    AFL-inspired mutation strategy: randomly increment/decrement adjacent N bytes (N = 1, 2, 4).
    - Choose N randomly from [1, 2, 4].
    - For each chosen byte position, add a random value in [-35, 35] and wrap around within [0, 255].
    """
    byte_array = bytearray(s, 'utf-8')
    
    if len(byte_array) == 0:
        return s
    
    n = random.choice([1, 2, 4])
    if n > len(byte_array):
        n = len(byte_array)
    
    byte_pos = random.randint(0, len(byte_array) - n)
    
    for i in range(n):
        num = byte_array[byte_pos + i]
        num = (num + random.randint(-35, 35)) % 256
        byte_array[byte_pos + i] = num

    return byte_array.decode('utf-8', errors='ignore')

# def arithmetic_random_bytes(s: str) -> str:
#     """
#     基于 AFL 变异算法策略中的 arithmetic inc/dec 与 random havoc 实现相邻 N 字节随机增减（N = 1, 2, 4），其中 N 为随机生成
#     字节随机增减：
#         1. 取其中一个 byte，将其转换为数字 num1；
#         2. 将 num1 加上一个 [-35, 35] 的随机数，得到 num2；
#         3. 用 num2 所表示的 byte 替换该 byte
#     从 s 中随机挑选一个 byte，将其与其后面 N - 1 个 bytes 进行字节随机增减
#     注意：不要越界；如果出现单个字节在添加随机数之后，可以通过取模操作使该字节落在 [0, 255] 之间
#     """
#     byte_array = bytearray(s, 'utf-8')
#     if len(byte_array) == 0:
#         return s

#     n = random.choice([1, 2, 4])
#     byte_pos = random.randint(0, len(byte_array) - n)
#     for i in range(n):
#         num = byte_array[byte_pos + i]
#         num = (num + random.randint(-35, 35)) % 256
#         byte_array[byte_pos + i] = num

#     return byte_array.decode('utf-8', errors='ignore')

# def arithmetic_random_bytes(self, inp, n=1):
#     byte_array = bytearray(inp)

#     if len(byte_array) <= n:
#         return byte_array  # No bytes to mutate if the array is too small

#     byte_pos = random.randint(0, len(byte_array) - n)
#     for i in range(byte_pos, byte_pos + n):
#         byte_array[i] = random.randrange(256)  # Assuming bytes range from 0 to 255

#     return bytes(byte_array)


import random

def interesting_random_bytes(s: str) -> str:
    """
    AFL-inspired mutation strategy: randomly select a position and change the value of a random byte.
    """
    byte_array = bytearray(s, 'utf-8')
    
    if len(byte_array) == 0:
        return s
    
    byte_pos = random.randint(0, len(byte_array) - 1)
    byte_array[byte_pos] = random.randint(0, 255)
    
    return byte_array.decode('utf-8', errors='ignore')


# def interesting_random_bytes(s: str) -> str:
#     """
#     基于 AFL 变异算法策略中的 interesting values 与 random havoc 实现相邻 N 字节随机替换为 interesting_value（N = 1, 2, 4），其中 N 为随机生成
#     interesting_value 替换：
#         1. 构建分别针对于 1, 2, 4 bytes 的 interesting_value 数组；
#         2. 随机挑选 s 中相邻连续的 1, 2, 4 bytes，将其替换为相应 interesting_value 数组中的随机元素；
#     注意：不要越界
#     """
#     interesting_values_1 = [0, 1, 255]
#     interesting_values_2 = [0, 1, 32767, 65535]
#     interesting_values_4 = [0, 1, 2147483647, 4294967295]

#     byte_array = bytearray(s, 'utf-8')
#     if len(byte_array) == 0:
#         return s

#     n = random.choice([1, 2, 4])
#     byte_pos = random.randint(0, len(byte_array) - n)
    
#     if n == 1:
#         value = random.choice(interesting_values_1)
#     elif n == 2:
#         value = random.choice(interesting_values_2)
#     else:
#         value = random.choice(interesting_values_4)
    
#     byte_array[byte_pos:byte_pos + n] = value.to_bytes(n, byteorder='little', signed=False)

#     return byte_array.decode('utf-8', errors='ignore')


def havoc_random_insert(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 random havoc 实现随机插入
    随机选取一个位置，插入一段的内容，其中 75% 的概率是插入原文中的任意一段随机长度的内容，25% 的概率是插入一段随机长度的 bytes
    """
    pos = random.randint(0, len(s))
    if random.random() < 0.75:
        insert_content = s[random.randint(0, len(s)):random.randint(0, len(s))]
    else:
        insert_content = ''.join(chr(random.randint(32, 127)) for _ in range(random.randint(1, 10)))
    return s[:pos] + insert_content + s[pos:]


def havoc_random_replace(s: str) -> str:
    """
    基于 AFL 变异算法策略中的 random havoc 实现随机替换
    随机选取一个位置，替换随后一段随机长度的内容，其中 75% 的概率是替换为原文中的任意一段随机长度的内容，25% 的概率是替换为一段随机长度的 bytes
    """
    start = random.randint(0, len(s))
    end = start + random.randint(1, 10)
    if random.random() < 0.75:
        replace_content = s[random.randint(0, len(s)):random.randint(0, len(s))]
    else:
        replace_content = ''.join(chr(random.randint(32, 127)) for _ in range(random.randint(1, 10)))
    return s[:start] + replace_content + s[end:]


class Mutator:

    def __init__(self) -> None:
        """Constructor"""
        self.mutators = [
            insert_random_character,
            flip_random_bits,
            arithmetic_random_bytes,
            interesting_random_bytes,
            havoc_random_insert,
            havoc_random_replace
        ]

    def mutate(self, inp: Any) -> Any:
        mutator = random.choice(self.mutators)
        return mutator(inp)

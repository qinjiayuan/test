# !/usr/bin python3
# encoding: utf-8 -*-
# @file     : encry_decry.py.py
# @author   : Gowent 
# @Time     : 2025/3/5 16:18
# @Copyright: Personal
import hashlib
from Crypto.Hash import SHA
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5 as PKCS1_signature
from Crypto.Cipher import PKCS1_v1_5 as PKCS1_cipher , AES

def md5(s:str):
    return hashlib.md5(s.encode(encoding='utf-8')).hexdigest()


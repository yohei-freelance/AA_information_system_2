#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 25 16:42:19 2018

@author: yohei
"""
#ローカル関数を用いた再帰バージョン
def is_power(a,b):
    if type(a) != int or type(b) != int:
        return('整数を入力してください.')
    elif b == 1:
        return('bに1を入力してはベキ乗を考えることができません.')
    elif a <= 0 or b <= 0:
        return('0以下の値は入力しないでください.')
    else:
        def is_realpower(a,b):
            while a != 1:
                if a%b != 0:
                    print ('ベキ乗ではありません.')
                    break
                else:
                    a = a/b
                    return (is_realpower(a,b))
            if a == 1:
                print ('ベキ乗です.')
    return(is_realpower(a,b))


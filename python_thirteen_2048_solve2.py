#! python3
# solve3_2048.py - 盤面の評価関数を計算して次の一手を決める

# ライブラリのインポート
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os # geckodriverのコピー
import shutil
import numpy as np
import pprint
import time
import copy
from numpy.random import *
import math
# デバッグ
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.debug('Start of program')
logging.disable(logging.CRITICAL)# debugしない

def try_obtain_tile(board):# 現在の局面を取得
    tile_container_elem = browser.find_element_by_class_name('tile-container')

    try:
        tile_1_1 = tile_container_elem.find_elements_by_class_name('tile-position-1-1')
        try:
            board['1-1'] =  eval(tile_1_1[2].text.replace('\n',''))
        except:
            board['1-1'] =  eval(tile_1_1[0].text.replace('\n',''))
    except:
        logging.debug('1-1: None')
        board['1-1'] = '0'

    try:
        tile_1_2 = tile_container_elem.find_elements_by_class_name('tile-position-1-2')
        try:
            board['1-2'] =  eval(tile_1_2[2].text.replace('\n',''))
        except:
            board['1-2'] =  eval(tile_1_2[0].text.replace('\n',''))
    except:
        logging.debug('1-2: None')
        board['1-2'] = '0'

    try:
        tile_1_3 = tile_container_elem.find_elements_by_class_name('tile-position-1-3')
        try:
            board['1-3'] =  eval(tile_1_3[2].text.replace('\n',''))
        except:
            board['1-3'] =  eval(tile_1_3[0].text.replace('\n',''))
    except:
        logging.debug('1-3: None')
        board['1-3'] = '0'

    try:
        tile_1_4 = tile_container_elem.find_elements_by_class_name('tile-position-1-4')
        try:
            board['1-4'] =  eval(tile_1_4[2].text.replace('\n',''))
        except:
            board['1-4'] =  eval(tile_1_4[0].text.replace('\n',''))
    except:
        logging.debug('1-4: None')
        board['1-4'] = '0'

    try:
        tile_2_1 = tile_container_elem.find_elements_by_class_name('tile-position-2-1')
        try:
            board['2-1'] =  eval(tile_2_1[2].text.replace('\n',''))
        except:
            board['2-1'] =  eval(tile_2_1[0].text.replace('\n',''))
    except:
        logging.debug('2-1: None')
        board['2-1'] = '0'

    try:
        tile_2_2 = tile_container_elem.find_elements_by_class_name('tile-position-2-2')
        try:
            board['2-2'] =  eval(tile_2_2[2].text.replace('\n',''))
        except:
            board['2-2'] =  eval(tile_2_2[0].text.replace('\n',''))
    except:
        logging.debug('2-2: None')
        board['2-2'] = '0'

    try:
        tile_2_3 = tile_container_elem.find_elements_by_class_name('tile-position-2-3')
        try:
            board['2-3'] =  eval(tile_2_3[2].text.replace('\n',''))
        except:
            board['2-3'] =  eval(tile_2_3[0].text.replace('\n',''))
    except:
        logging.debug('2-3: None')
        board['2-3'] = '0'

    try:
        tile_2_4 = tile_container_elem.find_elements_by_class_name('tile-position-2-4')
        try:
            board['2-4'] =  eval(tile_2_4[2].text.replace('\n',''))
        except:
            board['2-4'] =  eval(tile_2_4[0].text.replace('\n',''))
    except:
        logging.debug('2-4: None')
        board['2-4'] = '0'

    try:
        tile_3_1 = tile_container_elem.find_elements_by_class_name('tile-position-3-1')
        try:
            board['3-1'] =  eval(tile_3_1[2].text.replace('\n',''))
        except:
            board['3-1'] =  eval(tile_3_1[0].text.replace('\n',''))
    except:
        logging.debug('3-1: None')
        board['3-1'] = '0'

    try:
        tile_3_2 = tile_container_elem.find_elements_by_class_name('tile-position-3-2')
        try:
            board['3-2'] =  eval(tile_3_2[2].text.replace('\n',''))
        except:
            board['3-2'] =  eval(tile_3_2[0].text.replace('\n',''))
    except:
        logging.debug('3-2: None')
        board['3-2'] = '0'

    try:
        tile_3_3 = tile_container_elem.find_elements_by_class_name('tile-position-3-3')
        try:
            board['3-3'] =  eval(tile_3_3[2].text.replace('\n',''))
        except:
            board['3-3'] =  eval(tile_3_3[0].text.replace('\n',''))
    except:
        logging.debug('3-3: None')
        board['3-3'] = '0'

    try:
        tile_3_4 = tile_container_elem.find_elements_by_class_name('tile-position-3-4')
        try:
            board['3-4'] =  eval(tile_3_4[2].text.replace('\n',''))
        except:
            board['3-4'] =  eval(tile_3_4[0].text.replace('\n',''))
    except:
        logging.debug('3-4: None')
        board['3-4'] = '0'

    try:
        tile_4_1 = tile_container_elem.find_elements_by_class_name('tile-position-4-1')
        try:
            board['4-1'] =  eval(tile_4_1[2].text.replace('\n',''))
        except:
            board['4-1'] =  eval(tile_4_1[0].text.replace('\n',''))
    except:
        logging.debug('4-1: None')
        board['4-1'] = '0'

    try:
        tile_4_2 = tile_container_elem.find_elements_by_class_name('tile-position-4-2')
        try:
            board['4-2'] =  eval(tile_4_2[2].text.replace('\n',''))
        except:
            board['4-2'] =  eval(tile_4_2[0].text.replace('\n',''))
    except:
        logging.debug('4-2: None')
        board['4-2'] = '0'

    try:
        tile_4_3 = tile_container_elem.find_elements_by_class_name('tile-position-4-3')
        try:
            board['4-3'] =  eval(tile_4_3[2].text.replace('\n',''))
        except:
            board['4-3'] =  eval(tile_4_3[0].text.replace('\n',''))
    except:
        logging.debug('4-3: None')
        board['4-3'] = '0'

    try:
        tile_4_4 = tile_container_elem.find_elements_by_class_name('tile-position-4-4')
        try:
            board['4-4'] =  eval(tile_4_4[2].text.replace('\n',''))
        except:
            board['4-4'] =  eval(tile_4_4[0].text.replace('\n',''))
    except:
        logging.debug('4-4: None')
        board['4-4'] = '0'
    return board

def print_board(board):# 盤を見やすく表示
    print('  ' + '____'*4)
    print(' | ' + board['1-1'] + ' | ' + board['2-1'] + ' | ' + board['3-1'] + ' | ' + board['4-1'] + ' | ')
    print(' | ' + board['1-2'] + ' | ' + board['2-2'] + ' | ' + board['3-2'] + ' | ' + board['4-2'] + ' | ')
    print(' | ' + board['1-3'] + ' | ' + board['2-3'] + ' | ' + board['3-3'] + ' | ' + board['4-3'] + ' | ')
    print(' | ' + board['1-4'] + ' | ' + board['2-4'] + ' | ' + board['3-4'] + ' | ' + board['4-4'] + ' | ')
    print('  ' + '____'*4)

def read_board():# 現在の局面を辞書に格納
    board = {'1-1':'0','1-2':'0','1-3':'0','1-4':'0',\
    '2-1':'0','2-2':'0','2-3':'0','2-4':'0',\
    '3-1':'0','3-2':'0','3-3':'0','3-4':'0',\
    '4-1':'0','4-2':'0','4-3':'0','4-4':'0'}# 初期設定は全て0

    board = try_obtain_tile(board)
    print_board(board)
    return board

def cal_gain_function(board):# ある局面が与えられた時に、その評価関数を計算する
    """
    評価関数の中身
    右下に大きい数字が来るようにしたい
    上方向は動かさない（他に手がない場合を除く）
    空白は多い方がいい
    ジグザグに重みをつける
    """
    gain_function = 0
    if int(board['1-3']) < int(board['1-4']):
        gain_function += 1000
    if int(board['2-3']) < int(board['2-4']):
        gain_function += 1000
    if int(board['3-3']) < int(board['3-4']):
        gain_function += 1000
    if int(board['4-3']) < int(board['4-4']):
        gain_function += 1000

    if int(board['1-3']) == int(board['1-4']):
        gain_function += 5000
    if int(board['2-3']) == int(board['2-4']):
        gain_function += 5000
    if int(board['3-3']) == int(board['3-4']):
        gain_function += 5000
    if int(board['4-3']) == int(board['4-4']):
        gain_function += 5000

    if int(board['1-3']) == int(board['1-2']):
        gain_function += 5000
    if int(board['2-3']) == int(board['2-2']):
        gain_function += 5000
    if int(board['3-3']) == int(board['3-2']):
        gain_function += 5000
    if int(board['4-3']) == int(board['4-2']):
        gain_function += 5000

    for key,value in board.items():
        if value=='0':
            gain_function += 100 # タイルの枚数が少ないほど評価値高い

        if key=='4-4':
            gain_function += math.log2(int(value)+1)*800*8
        if key=='3-4':
            gain_function += math.log2(int(value)+1)*750*8
        if key=='2-4':
            gain_function += math.log2(int(value)+1)*700*8
        if key=='1-4':
            gain_function += math.log2(int(value)+1)*650*8
        if key=='1-3':
            gain_function += math.log2(int(value)+1)*600*2
        if key=='2-3':
            gain_function += math.log2(int(value)+1)*550*2
        if key=='3-3':
            gain_function += math.log2(int(value)+1)*500*2
        if key=='4-3':
            gain_function += math.log2(int(value)+1)*450*2
        if key=='1-2':
            gain_function += math.log2(int(value)+1)
        if key=='2-2':
            gain_function += math.log2(int(value)+1)
        if key=='3-2':
            gain_function += math.log2(int(value)+1)
        if key=='4-2':
            gain_function += math.log2(int(value)+1)

    return gain_function

def move_tile(next_board,a,b):
    next_board[b] = next_board[a]
    next_board[a] = '0'
    return next_board# タイルの移動

def sum_tile(next_board,c,d):
    c_num = int(next_board[c])
    d_num = int(next_board[d])
    next_board[c] = '0'
    next_board[d] = str(c_num + d_num)
    return next_board# タイルの結合

def down_move(next_board):# 下方向移動
    if next_board['1-4']=='0':# ok
        if next_board['1-3']=='0':# ok
            if next_board['1-2']=='0':# ok
                if next_board['1-1']=='0':
                    #[0,0,0,0]->何もしない
                    logging.debug('hoge')
                elif next_board['1-1']!='0':
                    #[2,0,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'1-1','1-4')
            elif next_board['1-2']!='0':# ok
                if next_board['1-1']=='0':
                    #[0,2,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'1-2','1-4')
                elif next_board['1-1']!='0':
                    if next_board['1-1']==next_board['1-2']:
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-1','1-2')
                        next_board = move_tile(next_board,'1-2','1-4')
                    elif next_board['1-1']!=next_board['1-2']:
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-2','1-4')
                        next_board = move_tile(next_board,'1-1','1-3')
        elif next_board['1-3']!='0':# ok
            if next_board['1-2']=='0':# ok
                if next_board['1-1']=='0':# ok
                    #[0,0,2,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'1-3','1-4')
                elif next_board['1-1']!='0':# ok
                    if next_board['1-1']==next_board['1-3']:# ok
                        #[2,0,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-1','1-3')
                        next_board = move_tile(next_board,'1-3','1-4')
                    elif next_board['1-1']!=next_board['1-3']:# ok
                        #[2,0,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-1','1-3')
            elif next_board['1-2']!='0':# ok
                if next_board['1-1']=='0':# ok
                    if next_board['1-2']==next_board['1-3']:# ok
                        #[0,2,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-2','1-3')
                        next_board = move_tile(next_board,'1-3','1-4')
                    elif next_board['1-2']!=next_board['1-3']:# ok
                        #[0,2,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-2','1-3')
                elif next_board['1-1']!='0':# ok
                    if next_board['1-2']==next_board['1-3']:# ok
                        #[2,2,2,0]->[0,0,2,4]
                        next_board = sum_tile(next_board,'1-2','1-3')
                        next_board = move_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-1','1-3')
                    elif next_board['1-1']==next_board['1-2']:# ok
                        #[2,2,4,0]->[0,0,4,4]
                        next_board = sum_tile(next_board,'1-1','1-2')
                        next_board = move_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-2','1-3')
                    else:# ok
                        #[2,4,8,0]->[0,2,4,8]
                        next_board = move_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-2','1-3')
                        next_board = move_tile(next_board,'1-1','1-2')
    elif next_board['1-4']!='0':# ok
        if next_board['1-3']=='0':# ok
            if next_board['1-2']=='0':# ok
                if next_board['1-1']=='0':# ok
                    #[0,0,0,2]->何もしない
                    logging.debug('hoge')
                elif next_board['1-1']!='0':# ok
                    if next_board['1-1']==next_board['1-4']:# ok
                        #[2,0,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-1','1-4')
                    elif next_board['1-1']!=next_board['1-4']:# ok
                        #[2,0,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-1','1-3')
            elif next_board['1-2']!='0':# ok
                if next_board['1-1']=='0':# ok
                    if next_board['1-2']==next_board['1-4']:# ok
                        #[0,2,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-2','1-4')
                    elif next_board['1-2']!=next_board['1-4']:# ok
                        #[0,2,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-2','1-3')
                elif next_board['1-1']!='0':# ok
                    if next_board['1-1']==next_board['1-2']:# ok
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-1','1-2')
                        next_board = move_tile(next_board,'1-2','1-4')
                    elif next_board['1-1']!=next_board['1-2']:# ok
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'1-2','1-4')
                        next_board = move_tile(next_board,'1-1','1-3')
        elif next_board['1-3']!='0':# ok
            if next_board['1-2']=='0':# ok
                if next_board['1-1']=='0':# ok
                    if next_board['1-3']==next_board['1-4']:# ok
                        #[0,0,2,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'1-3','1-4')
                    elif next_board['1-3']!=next_board['1-4']:# ok
                        #[0,0,2,4]->[0,0,2,4]
                        logging.debug('hoge')
                elif next_board['1-1']!='0':# ok
                    if next_board['1-3']==next_board['1-4']:# ok
                        #[2,0,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-1','1-3')
                    elif next_board['1-1']==next_board['1-3']:# ok
                        #[2,0,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'1-1','1-3')
                    else:# ok
                        #[2,0,4,8]->[0,2,4,8]
                        next_board = move_tile(next_board,'1-1','1-2')
            elif next_board['1-2']!='0':# ok
                if next_board['1-1']=='0':# ok
                    if next_board['1-3']==next_board['1-4']:# ok
                        #[0,2,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'1-3','1-4')
                        next_board = move_tile(next_board,'1-2','1-3')
                    elif next_board['1-2']==next_board['1-3']:# ok
                        #[0,2,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'1-2','1-3')
                    else:# ok
                        #[0,2,4,8]->[0,2,4,8]
                        logging.debug('hoge')
                elif next_board['1-1']!='0':#全部違う場合->ok
                    if next_board['1-3']==next_board['1-4']:# ok
                        if next_board['1-1']==next_board['1-2']:# ok
                            #[2,2,2,2]->[0,0,4,4]
                            next_board = sum_tile(next_board,'1-3','1-4')
                            next_board = sum_tile(next_board,'1-1','1-2')
                            next_board = move_tile(next_board,'1-2','1-3')
                        else:# ok
                            #[2,4,2,2]->[0,2,4,4]
                            next_board = sum_tile(next_board,'1-3','1-4')
                            next_board = move_tile(next_board,'1-2','1-3')
                            next_board = move_tile(next_board,'1-1','1-2')
                    elif next_board['1-2']==next_board['1-3'] and next_board['1-3']!=next_board['1-4']:# ok
                        #[2,2,2,4]->[0,2,4,4]
                        next_board = sum_tile(next_board,'1-2','1-3')
                        next_board = move_tile(next_board,'1-1','1-2')
                    elif next_board['1-1']==next_board['1-2'] and next_board['1-2']!=next_board['1-3'] and next_board['1-3']!=next_board['1-4']:# ok
                        #[2,2,4,8]->[0,4,4,8]
                        next_board = sum_tile(next_board,'1-1','1-2')
                    else:# ok
                        #[2,4,8,16]->[2,4,8,16]
                        logging.debug('hoge')

    if next_board['2-4']=='0':# ok
        if next_board['2-3']=='0':# ok
            if next_board['2-2']=='0':# ok
                if next_board['2-1']=='0':
                    #[0,0,0,0]->何もしない
                    logging.debug('hoge')
                elif next_board['2-1']!='0':
                    #[2,0,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'2-1','2-4')
            elif next_board['2-2']!='0':# ok
                if next_board['2-1']=='0':
                    #[0,2,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'2-2','2-4')
                elif next_board['2-1']!='0':
                    if next_board['2-1']==next_board['2-2']:
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-1','2-2')
                        next_board = move_tile(next_board,'2-2','2-4')
                    elif next_board['2-1']!=next_board['2-2']:
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-2','2-4')
                        next_board = move_tile(next_board,'2-1','2-3')
        elif next_board['2-3']!='0':# ok
            if next_board['2-2']=='0':# ok
                if next_board['2-1']=='0':# ok
                    #[0,0,2,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'2-3','2-4')
                elif next_board['2-1']!='0':# ok
                    if next_board['2-1']==next_board['2-3']:# ok
                        #[2,0,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-1','2-3')
                        next_board = move_tile(next_board,'2-3','2-4')
                    elif next_board['2-1']!=next_board['2-3']:# ok
                        #[2,0,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-1','2-3')
            elif next_board['2-2']!='0':# ok
                if next_board['2-1']=='0':# ok
                    if next_board['2-2']==next_board['2-3']:# ok
                        #[0,2,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-2','2-3')
                        next_board = move_tile(next_board,'2-3','2-4')
                    elif next_board['2-2']!=next_board['2-3']:# ok
                        #[0,2,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-2','2-3')
                elif next_board['2-1']!='0':# ok
                    if next_board['2-2']==next_board['2-3']:# ok
                        #[2,2,2,0]->[0,0,2,4]
                        next_board = sum_tile(next_board,'2-2','2-3')
                        next_board = move_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-1','2-3')
                    elif next_board['2-1']==next_board['2-2']:# ok
                        #[2,2,4,0]->[0,0,4,4]
                        next_board = sum_tile(next_board,'2-1','2-2')
                        next_board = move_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-2','2-3')
                    else:# ok
                        #[2,4,8,0]->[0,2,4,8]
                        next_board = move_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-2','2-3')
                        next_board = move_tile(next_board,'2-1','2-2')
    elif next_board['2-4']!='0':# ok
        if next_board['2-3']=='0':# ok
            if next_board['2-2']=='0':# ok
                if next_board['2-1']=='0':# ok
                    #[0,0,0,2]->何もしない
                    logging.debug('hoge')
                elif next_board['2-1']!='0':# ok
                    if next_board['2-1']==next_board['2-4']:# ok
                        #[2,0,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-1','2-4')
                    elif next_board['2-1']!=next_board['2-4']:# ok
                        #[2,0,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-1','2-3')
            elif next_board['2-2']!='0':# ok
                if next_board['2-1']=='0':# ok
                    if next_board['2-2']==next_board['2-4']:# ok
                        #[0,2,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-2','2-4')
                    elif next_board['2-2']!=next_board['2-4']:# ok
                        #[0,2,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-2','2-3')
                elif next_board['2-1']!='0':# ok
                    if next_board['2-1']==next_board['2-2']:# ok
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-1','2-2')
                        next_board = move_tile(next_board,'2-2','2-4')
                    elif next_board['2-1']!=next_board['2-2']:# ok
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'2-2','2-4')
                        next_board = move_tile(next_board,'2-1','2-3')
        elif next_board['2-3']!='0':# ok
            if next_board['2-2']=='0':# ok
                if next_board['2-1']=='0':# ok
                    if next_board['2-3']==next_board['2-4']:# ok
                        #[0,0,2,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'2-3','2-4')
                    elif next_board['2-3']!=next_board['2-4']:# ok
                        #[0,0,2,4]->[0,0,2,4]
                        logging.debug('hoge')
                elif next_board['2-1']!='0':# ok
                    if next_board['2-3']==next_board['2-4']:# ok
                        #[2,0,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-1','2-3')
                    elif next_board['2-1']==next_board['2-3']:# ok
                        #[2,0,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'2-1','2-3')
                    else:# ok
                        #[2,0,4,8]->[0,2,4,8]
                        next_board = move_tile(next_board,'2-1','2-2')
            elif next_board['2-2']!='0':# ok
                if next_board['2-1']=='0':# ok
                    if next_board['2-3']==next_board['2-4']:# ok
                        #[0,2,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'2-3','2-4')
                        next_board = move_tile(next_board,'2-2','2-3')
                    elif next_board['2-2']==next_board['2-3']:# ok
                        #[0,2,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'2-2','2-3')
                    else:# ok
                        #[0,2,4,8]->[0,2,4,8]
                        logging.debug('hoge')
                elif next_board['2-1']!='0':#全部違う場合->ok
                    if next_board['2-3']==next_board['2-4']:# ok
                        if next_board['2-1']==next_board['2-2']:# ok
                            #[2,2,2,2]->[0,0,4,4]
                            next_board = sum_tile(next_board,'2-3','2-4')
                            next_board = sum_tile(next_board,'2-1','2-2')
                            next_board = move_tile(next_board,'2-2','2-3')
                        else:# ok
                            #[2,4,2,2]->[0,2,4,4]
                            next_board = sum_tile(next_board,'2-3','2-4')
                            next_board = move_tile(next_board,'2-2','2-3')
                            next_board = move_tile(next_board,'2-1','2-2')
                    elif next_board['2-2']==next_board['2-3'] and next_board['2-3']!=next_board['2-4']:# ok
                        #[2,2,2,4]->[0,2,4,4]
                        next_board = sum_tile(next_board,'2-2','2-3')
                        next_board = move_tile(next_board,'2-1','2-2')
                    elif next_board['2-1']==next_board['2-2'] and next_board['2-2']!=next_board['2-3'] and next_board['2-3']!=next_board['2-4']:# ok
                        #[2,2,4,8]->[0,4,4,8]
                        next_board = sum_tile(next_board,'2-1','2-2')
                    else:# ok
                        #[2,4,8,16]->[2,4,8,16]
                        logging.debug('hoge')

    if next_board['3-4']=='0':# ok
        if next_board['3-3']=='0':# ok
            if next_board['3-2']=='0':# ok
                if next_board['3-1']=='0':
                    #[0,0,0,0]->何もしない
                    logging.debug('hoge')
                elif next_board['3-1']!='0':
                    #[2,0,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'3-1','3-4')
            elif next_board['3-2']!='0':# ok
                if next_board['3-1']=='0':
                    #[0,2,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'3-2','3-4')
                elif next_board['3-1']!='0':
                    if next_board['3-1']==next_board['3-2']:
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-1','3-2')
                        next_board = move_tile(next_board,'3-2','3-4')
                    elif next_board['3-1']!=next_board['3-2']:
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-2','3-4')
                        next_board = move_tile(next_board,'3-1','3-3')
        elif next_board['3-3']!='0':# ok
            if next_board['3-2']=='0':# ok
                if next_board['3-1']=='0':# ok
                    #[0,0,2,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'3-3','3-4')
                elif next_board['3-1']!='0':# ok
                    if next_board['3-1']==next_board['3-3']:# ok
                        #[2,0,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-1','3-3')
                        next_board = move_tile(next_board,'3-3','3-4')
                    elif next_board['3-1']!=next_board['3-3']:# ok
                        #[2,0,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-1','3-3')
            elif next_board['3-2']!='0':# ok
                if next_board['3-1']=='0':# ok
                    if next_board['3-2']==next_board['3-3']:# ok
                        #[0,2,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-2','3-3')
                        next_board = move_tile(next_board,'3-3','3-4')
                    elif next_board['3-2']!=next_board['3-3']:# ok
                        #[0,2,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-2','3-3')
                elif next_board['3-1']!='0':# ok
                    if next_board['3-2']==next_board['3-3']:# ok
                        #[2,2,2,0]->[0,0,2,4]
                        next_board = sum_tile(next_board,'3-2','3-3')
                        next_board = move_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-1','3-3')
                    elif next_board['3-1']==next_board['3-2']:# ok
                        #[2,2,4,0]->[0,0,4,4]
                        next_board = sum_tile(next_board,'3-1','3-2')
                        next_board = move_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-2','3-3')
                    else:# ok
                        #[2,4,8,0]->[0,2,4,8]
                        next_board = move_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-2','3-3')
                        next_board = move_tile(next_board,'3-1','3-2')
    elif next_board['3-4']!='0':# ok
        if next_board['3-3']=='0':# ok
            if next_board['3-2']=='0':# ok
                if next_board['3-1']=='0':# ok
                    #[0,0,0,2]->何もしない
                    logging.debug('hoge')
                elif next_board['3-1']!='0':# ok
                    if next_board['3-1']==next_board['3-4']:# ok
                        #[2,0,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-1','3-4')
                    elif next_board['3-1']!=next_board['3-4']:# ok
                        #[2,0,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-1','3-3')
            elif next_board['3-2']!='0':# ok
                if next_board['3-1']=='0':# ok
                    if next_board['3-2']==next_board['3-4']:# ok
                        #[0,2,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-2','3-4')
                    elif next_board['3-2']!=next_board['3-4']:# ok
                        #[0,2,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-2','3-3')
                elif next_board['3-1']!='0':# ok
                    if next_board['3-1']==next_board['3-2']:# ok
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-1','3-2')
                        next_board = move_tile(next_board,'3-2','3-4')
                    elif next_board['3-1']!=next_board['3-2']:# ok
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'3-2','3-4')
                        next_board = move_tile(next_board,'3-1','3-3')
        elif next_board['3-3']!='0':# ok
            if next_board['3-2']=='0':# ok
                if next_board['3-1']=='0':# ok
                    if next_board['3-3']==next_board['3-4']:# ok
                        #[0,0,2,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'3-3','3-4')
                    elif next_board['3-3']!=next_board['3-4']:# ok
                        #[0,0,2,4]->[0,0,2,4]
                        logging.debug('hoge')
                elif next_board['3-1']!='0':# ok
                    if next_board['3-3']==next_board['3-4']:# ok
                        #[2,0,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-1','3-3')
                    elif next_board['3-1']==next_board['3-3']:# ok
                        #[2,0,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'3-1','3-3')
                    else:# ok
                        #[2,0,4,8]->[0,2,4,8]
                        next_board = move_tile(next_board,'3-1','3-2')
            elif next_board['3-2']!='0':# ok
                if next_board['3-1']=='0':# ok
                    if next_board['3-3']==next_board['3-4']:# ok
                        #[0,2,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'3-3','3-4')
                        next_board = move_tile(next_board,'3-2','3-3')
                    elif next_board['3-2']==next_board['3-3']:# ok
                        #[0,2,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'3-2','3-3')
                    else:# ok
                        #[0,2,4,8]->[0,2,4,8]
                        logging.debug('hoge')
                elif next_board['3-1']!='0':#全部違う場合->ok
                    if next_board['3-3']==next_board['3-4']:# ok
                        if next_board['3-1']==next_board['3-2']:# ok
                            #[2,2,2,2]->[0,0,4,4]
                            next_board = sum_tile(next_board,'3-3','3-4')
                            next_board = sum_tile(next_board,'3-1','3-2')
                            next_board = move_tile(next_board,'3-2','3-3')
                        else:# ok
                            #[2,4,2,2]->[0,2,4,4]
                            next_board = sum_tile(next_board,'3-3','3-4')
                            next_board = move_tile(next_board,'3-2','3-3')
                            next_board = move_tile(next_board,'3-1','3-2')
                    elif next_board['3-2']==next_board['3-3'] and next_board['3-3']!=next_board['3-4']:# ok
                        #[2,2,2,4]->[0,2,4,4]
                        next_board = sum_tile(next_board,'3-2','3-3')
                        next_board = move_tile(next_board,'3-1','3-2')
                    elif next_board['3-1']==next_board['3-2'] and next_board['3-2']!=next_board['3-3'] and next_board['3-3']!=next_board['3-4']:# ok
                        #[2,2,4,8]->[0,4,4,8]
                        next_board = sum_tile(next_board,'3-1','3-2')
                    else:# ok
                        #[2,4,8,16]->[2,4,8,16]
                        logging.debug('hoge')

    if next_board['4-4']=='0':# ok
        if next_board['4-3']=='0':# ok
            if next_board['4-2']=='0':# ok
                if next_board['4-1']=='0':
                    #[0,0,0,0]->何もしない
                    logging.debug('hoge')
                elif next_board['4-1']!='0':
                    #[2,0,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'4-1','4-4')
            elif next_board['4-2']!='0':# ok
                if next_board['4-1']=='0':
                    #[0,2,0,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'4-2','4-4')
                elif next_board['4-1']!='0':
                    if next_board['4-1']==next_board['4-2']:
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-1','4-2')
                        next_board = move_tile(next_board,'4-2','4-4')
                    elif next_board['4-1']!=next_board['4-2']:
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-2','4-4')
                        next_board = move_tile(next_board,'4-1','4-3')
        elif next_board['4-3']!='0':# ok
            if next_board['4-2']=='0':# ok
                if next_board['4-1']=='0':# ok
                    #[0,0,2,0]->[0,0,0,2]
                    next_board = move_tile(next_board,'4-3','4-4')
                elif next_board['4-1']!='0':# ok
                    if next_board['4-1']==next_board['4-3']:# ok
                        #[2,0,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-1','4-3')
                        next_board = move_tile(next_board,'4-3','4-4')
                    elif next_board['4-1']!=next_board['4-3']:# ok
                        #[2,0,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-1','4-3')
            elif next_board['4-2']!='0':# ok
                if next_board['4-1']=='0':# ok
                    if next_board['4-2']==next_board['4-3']:# ok
                        #[0,2,2,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-2','4-3')
                        next_board = move_tile(next_board,'4-3','4-4')
                    elif next_board['4-2']!=next_board['4-3']:# ok
                        #[0,2,4,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-2','4-3')
                elif next_board['4-1']!='0':# ok
                    if next_board['4-2']==next_board['4-3']:# ok
                        #[2,2,2,0]->[0,0,2,4]
                        next_board = sum_tile(next_board,'4-2','4-3')
                        next_board = move_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-1','4-3')
                    elif next_board['4-1']==next_board['4-2']:# ok
                        #[2,2,4,0]->[0,0,4,4]
                        next_board = sum_tile(next_board,'4-1','4-2')
                        next_board = move_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-2','4-3')
                    else:# ok
                        #[2,4,8,0]->[0,2,4,8]
                        next_board = move_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-2','4-3')
                        next_board = move_tile(next_board,'4-1','4-2')
    elif next_board['4-4']!='0':# ok
        if next_board['4-3']=='0':# ok
            if next_board['4-2']=='0':# ok
                if next_board['4-1']=='0':# ok
                    #[0,0,0,2]->何もしない
                    logging.debug('hoge')
                elif next_board['4-1']!='0':# ok
                    if next_board['4-1']==next_board['4-4']:# ok
                        #[2,0,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-1','4-4')
                    elif next_board['4-1']!=next_board['4-4']:# ok
                        #[2,0,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-1','4-3')
            elif next_board['4-2']!='0':# ok
                if next_board['4-1']=='0':# ok
                    if next_board['4-2']==next_board['4-4']:# ok
                        #[0,2,0,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-2','4-4')
                    elif next_board['4-2']!=next_board['4-4']:# ok
                        #[0,2,0,4]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-2','4-3')
                elif next_board['4-1']!='0':# ok
                    if next_board['4-1']==next_board['4-2']:# ok
                        #[2,2,0,0]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-1','4-2')
                        next_board = move_tile(next_board,'4-2','4-4')
                    elif next_board['4-1']!=next_board['4-2']:# ok
                        #[2,4,0,0]->[0,0,2,4]
                        next_board = move_tile(next_board,'4-2','4-4')
                        next_board = move_tile(next_board,'4-1','4-3')
        elif next_board['4-3']!='0':# ok
            if next_board['4-2']=='0':# ok
                if next_board['4-1']=='0':# ok
                    if next_board['4-3']==next_board['4-4']:# ok
                        #[0,0,2,2]->[0,0,0,4]
                        next_board = sum_tile(next_board,'4-3','4-4')
                    elif next_board['4-3']!=next_board['4-4']:# ok
                        #[0,0,2,4]->[0,0,2,4]
                        logging.debug('hoge')
                elif next_board['4-1']!='0':# ok
                    if next_board['4-3']==next_board['4-4']:# ok
                        #[2,0,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-1','4-3')
                    elif next_board['4-1']==next_board['4-3']:# ok
                        #[2,0,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'4-1','4-3')
                    else:# ok
                        #[2,0,4,8]->[0,2,4,8]
                        next_board = move_tile(next_board,'4-1','4-2')
            elif next_board['4-2']!='0':# ok
                if next_board['4-1']=='0':# ok
                    if next_board['4-3']==next_board['4-4']:# ok
                        #[0,2,2,2]->[0,0,2,4]
                        next_board = sum_tile(next_board,'4-3','4-4')
                        next_board = move_tile(next_board,'4-2','4-3')
                    elif next_board['4-2']==next_board['4-3']:# ok
                        #[0,2,2,4]->[0,0,4,4]
                        next_board = sum_tile(next_board,'4-2','4-3')
                    else:# ok
                        #[0,2,4,8]->[0,2,4,8]
                        logging.debug('hoge')
                elif next_board['4-1']!='0':#全部違う場合->ok
                    if next_board['4-3']==next_board['4-4']:# ok
                        if next_board['4-1']==next_board['4-2']:# ok
                            #[2,2,2,2]->[0,0,4,4]
                            next_board = sum_tile(next_board,'4-3','4-4')
                            next_board = sum_tile(next_board,'4-1','4-2')
                            next_board = move_tile(next_board,'4-2','4-3')
                        else:# ok
                            #[2,4,2,2]->[0,2,4,4]
                            next_board = sum_tile(next_board,'4-3','4-4')
                            next_board = move_tile(next_board,'4-2','4-3')
                            next_board = move_tile(next_board,'4-1','4-2')
                    elif next_board['4-2']==next_board['4-3'] and next_board['4-3']!=next_board['4-4']:# ok
                        #[2,2,2,4]->[0,2,4,4]
                        next_board = sum_tile(next_board,'4-2','4-3')
                        next_board = move_tile(next_board,'4-1','4-2')
                    elif next_board['4-1']==next_board['4-2'] and next_board['4-2']!=next_board['4-3'] and next_board['4-3']!=next_board['4-4']:# ok
                        #[2,2,4,8]->[0,4,4,8]
                        next_board = sum_tile(next_board,'4-1','4-2')
                    else:# ok
                        #[2,4,8,16]->[2,4,8,16]
                        logging.debug('hoge')

    return next_board

def rotate_right(next_board):# 右90度回転
    copy_board = copy.deepcopy(next_board)
    next_board['1-1'] = copy_board['1-4']
    next_board['1-2'] = copy_board['2-4']
    next_board['1-3'] = copy_board['3-4']
    next_board['1-4'] = copy_board['4-4']
    next_board['2-1'] = copy_board['1-3']
    next_board['2-2'] = copy_board['2-3']
    next_board['2-3'] = copy_board['3-3']
    next_board['2-4'] = copy_board['4-3']
    next_board['3-1'] = copy_board['1-2']
    next_board['3-2'] = copy_board['2-2']
    next_board['3-3'] = copy_board['3-2']
    next_board['3-4'] = copy_board['4-2']
    next_board['4-1'] = copy_board['1-1']
    next_board['4-2'] = copy_board['2-1']
    next_board['4-3'] = copy_board['3-1']
    next_board['4-4'] = copy_board['4-1']
    return next_board

def rotate_left(next_board):# 左90度回転
    next_board = rotate_right(next_board)
    next_board = rotate_right(next_board)
    next_board = rotate_right(next_board)
    return next_board

def flick_board(board,direction):# direction方向のフリックの結果を返す
    next_board = copy.deepcopy(board)

    if direction=='right':
        next_board = rotate_right(next_board)
        next_board = down_move(next_board)
        next_board = rotate_left(next_board)
    elif direction=='down':
        next_board = down_move(next_board)
    elif direction=='left':
        next_board = rotate_left(next_board)
        next_board = down_move(next_board)
        next_board = rotate_right(next_board)
    elif direction=='up':
        next_board = rotate_right(next_board)
        next_board = rotate_right(next_board)
        next_board = down_move(next_board)
        next_board = rotate_left(next_board)
        next_board = rotate_left(next_board)
    else:
        logging.debug('direction error')

    return next_board

def get_each_gain_function(board):# それぞれの方向の評価関数を計算する
    gain_functions = [] # 各方向の評価関数の値を格納
    dirs = ['right','down','left','up']
    for direction in dirs:
        next_board = flick_board(board,direction)# フリック
        next_gain_function = cal_gain_function(next_board)# フリック後の評価関数を計算
        gain_functions.append(next_gain_function)
    print('評価値: {}'.format(gain_functions))
    return gain_functions

def next_move():# 評価関数の値が最大のものを次の一手として選ぶ
    time.sleep(0.3)
    board = read_board()# 現在の局面を読み込む

    gain_functions = get_each_gain_function(board) # 各方向の評価関数を計算する

    if gain_functions[0]==gain_functions[1]==gain_functions[2]==gain_functions[3]:# どの方向も同じ価値を持つ場合硬直してしまう
        gain_functions[0] += randint(100)#乱数を足してほぐす
        gain_functions[2] += randint(100)
    if gain_functions[0]==gain_functions[1]:# どの方向も同じ価値を持つ場合硬直してしまう
        gain_functions[0] += randint(10)#乱数を足してほぐす
        gain_functions[1] += randint(10)
    if gain_functions[0]==gain_functions[2]:# どの方向も同じ価値を持つ場合硬直してしまう
        gain_functions[0] += randint(10)#乱数を足してほぐす
        gain_functions[2] += randint(10)
    if gain_functions[1]==gain_functions[2]:# どの方向も同じ価値を持つ場合硬直してしまう
        gain_functions[1] += randint(10)#乱数を足してほぐす
        gain_functions[2] += randint(10)
    best_dir = np.argmax(gain_functions)
    if best_dir==0:
        html_elem.send_keys(Keys.RIGHT)
    elif best_dir==1:
        html_elem.send_keys(Keys.DOWN)
    elif best_dir==2:
        html_elem.send_keys(Keys.LEFT)
    elif best_dir==3:
        html_elem.send_keys(Keys.UP)
    else:
        logging.debug('next_move_error')
        html_elem.send_keys(Keys.RIGHT)

# 2048のページを開く
browser = webdriver.Chrome()
# browser = webdriver.Firefox(executable_path="/Users/hoge/geckodriver/geckodriver")# geckodriverのpathを書く
# browser.get('https://gabrielecirulli.github.io/2048/')
browser.get('https://asset-manager.bbcchannels.com/m/2fzi3/')

# ゲーム開始の準備https://asset-manager.bbcchannels.com/m/2fzi3/
score = []# スコアの推移
html_elem = browser.find_element_by_tag_name('html')

elem_before_text = -1

# 操作の実行
for i in range(1000):
    print('{}手目：'.format(i))
    next_move()# 次の最適な一手を選択して実行
    elem = browser.find_element_by_class_name('score-container')# スコアの取得
    if elem.text == elem_before_text:
        random_num = randint(3)
        if random_num==0:
            html_elem.send_keys(Keys.RIGHT)
        if random_num==1:
            html_elem.send_keys(Keys.DOWN)
        if random_num==2:
            html_elem.send_keys(Keys.LEFT)
        time.sleep(0.3)

    score.append(elem.text)# スコアの推移をscoreに格納して記録する
    elem_before_text = elem.text
    print("スコア: {0}".format(elem.text))

logging.debug('End of program')

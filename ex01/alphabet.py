from dataclasses import dataclass
from datetime import datetime
from math import fabs
import random as rd
from select import select
CHAR_NUM = 10
CHAR_MISSING_NUM = 2
MAX_LOOP = 3

class Alphabet_Game:

    def __init__(self,char_num=CHAR_NUM,char_missing_num=CHAR_MISSING_NUM,max_loop=MAX_LOOP) -> None:
        self.char_num =char_num
        self.char_missing_num =char_missing_num
        self.max_loop=max_loop

        self.all_alphabets = [chr(i) for i in range(65,91)]

        self.selected_alphabets = list()
        self.missing_alphabets = list()
        self.show_alphabets = list()

    def start_game(self):
        count = 0
        flg = True
        stime = datetime.now()
        while count < self.max_loop:
            self.select_show_chars()
            ans = input("欠損文字はいくつ有るでしょうか:")
            if int(ans) == self.char_missing_num:
                print("正解です。それだは具体的に欠損文字を一つずつ入力してください。")
                anslist = [input(str(i+1)+"つ目の文字を入力してください") for i in range(self.char_missing_num)]

                is_correct = True
                for i in anslist:
                    is_correct = is_correct and (i in self.missing_alphabets)
                
                if is_correct:
                    flg = False
                    etime = datetime.now()
                    print("正解です。おめてでとうございます。")
                    print("-"*64)
                    print(f"時間:{etime-stime}")
                    break
                else:
                    print("不正解ですまたチャレンジしてください")
                    print("-"*64)


            else:
                print("不正解ですまたチャレンジしてください")
                print("-"*64)

            count += 1
        
        if flg: print("制限回数を超えました")


        
    def select_show_chars(self):
        self.selected_alphabets = rd.sample(self.all_alphabets,self.char_num)
        self.missing_alphabets = rd.sample(self.selected_alphabets,self.char_missing_num)

        self.show_alphabets = list(set(self.selected_alphabets)^set(self.missing_alphabets))

        print("対象文字:")
        print(self.list2str(self.selected_alphabets))
        print("表示文字:")
        print(self.list2str(self.show_alphabets))

        

    def list2str(self,list):
        return str(list).replace("'","").replace(",","").strip("[]")

def main():
    game = Alphabet_Game()
    game.start_game()

if __name__=="__main__":
    main()
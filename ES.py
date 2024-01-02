import os
import random

# 把关键词存储

status = input("是否想要记录灵感词?(Do you want to record your ideas?)\n(1)yes\n(2)no\n(3)clearallideas\n")

if status == "yes":
    print("\n")
    words = input("请输入想要记录的关键词(Please input your idea words then press enter)\n多个关键词请以 英文逗号 隔开(Split words with ','):\n")

    with open("ideas_word.txt", "a") as f:
        f.write(words)
        f.close()
    
    with open("ideas_word.txt","r") as f:
        ideas = f.read()
        idea = ideas.split(",")
        idea = list(set(idea))

    with open("ideas_word.txt", "w") as f:
        for i in range(len(idea)):
            f.write(idea[i])
            f.write(",")

# 打开文件随机输出词汇

elif status == "no":
    print("\n")
    print("开始输出灵感(Output random ideas)")

    with open("ideas_word.txt","r") as f:
        ideas = f.read()
        idea = ideas.split(",")
        idea = list(set(idea))

    total_ideanums = len(idea) - 1
    ideanums = random.randint(3,10)
    print(f"本次随机总共{ideanums}个灵感词(this time appears {ideanums} idea words total)")
    for i in range(ideanums):
        randnum = 0
        while idea[randnum] == "":
            randnum = random.randint(1,total_ideanums)
        print(idea[randnum])
        idea[randnum] = ""

    print("现在，请尽情创作吧(Now make those words become your eureka of great creations!)")

elif status == "clearallideas":
    print("\n")
    os.remove("ideas_word.txt")
    print("所有灵感词已清除(All idea words were removed)")
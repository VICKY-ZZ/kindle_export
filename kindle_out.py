import os
# kindle中My Clippings文件的地址
path = 'E:\documents\My Clippings.txt'
# 文件输出地址
out_path = 'D:\READING2022\\'
f = open(path,encoding="utf-8",errors='ignore')
lines = f.readlines()
a=0
# 可输入多本书
booknames=['晚熟的人','深度工作']
for bookname in booknames:
    booknotes=[]
    for i in range(0,len(lines),5):
        if bookname in lines[i]:
            if '笔记' in lines[i+1]:
                #*******************************************************
                #**如果想要每个标记之间空行，就用下面两行代码。ctrl+/取消注释***
                #*******************************************************
                booknotes[-1] = booknotes[-1].rstrip('\n\n')
                booknotes[-1] += ('——想法：'+ lines[i+3]+'\n')

                #！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                #！！如果不想每个标记之间空行，就用下面两行代码。ctrl+/取消注释！！
                #！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
                # booknotes[-1] = booknotes[-1].rstrip('\n')
                # booknotes[-1] += ('———想法：'+ lines[i+3])
                continue
            a += 1
            # *******************************************************
            # **如果想要每个标记之间空行，就用下面这行代码。ctrl+/取消注释****
            # *******************************************************
            booknotes.append(str(a)+'、'+lines[i+3]+'\n')

            # ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
            # ！！如果不想每个标记之间空行，就用下面这行代码。ctrl+/取消注释！！
            # ！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
            # booknotes.append(str(a)+'、'+lines[i+3])
    bookname ='《'+bookname+'》'
    file = open('%s.txt' % (out_path+bookname), 'w')
    file.writelines(booknotes)
    print('已完成'+bookname+'的导出！')
    file.close()
f.close()
print("已完成所有书籍的导出！")

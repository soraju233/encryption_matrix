
import numpy as np


plain=(input("平文をを入力してください\n"))
plainlst=list(plain)
word_count=len(plainlst)
asciilst = []
n = 26




#文字列を数値に変換
for s in plain:
    ord_num = ord(s) - 65 #Aを基準に
    asciilst.append(ord_num)
    
    
if word_count % 2 != 0:
    asciilst.append(0)
    

#print(asciilst)
#numpy配列に変換
lst_e = asciilst[::2]
lst_o = asciilst[1::2]
asciilst = lst_e + lst_o

asciinp = np.array(asciilst) #listをnumpy配列に変換

asciinp = np.reshape(asciinp,[2,-1])

#print(asciinp)


#暗号化の処理
print("暗号化鍵を入力してください")

print("[a,b]")
print("[c,d]")

a = int(input("a="))
b = int(input("b="))
c = int(input("c="))
d = int(input("d="))


key = np.array([[a,b],[c,d]])

cry_ = np.dot(key,asciinp)
#print(cry_)
cry_ = np.mod(cry_,n)
#print(cry_)

cry = cry_.T
cry = np.ravel(cry)#一次元化

cry = cry.tolist()

#print(cry)

cryascii = []
for s in cry:
    ord_num = chr(s+65)  
    cryascii.append(ord_num)

print("暗号化した結果")
print(cryascii)



#復号化

key = np.array([[d,-b],[-c,a]])
det = np.linalg.det(key) % n #行列式を求める

#nを法とした逆行列を求める。
# 商と余りと割られる数の保存先
qlist =[]
rlist =[]
wlist =[]

s = det
t = n #値の保存

r = s #とりあえず余りとしてaをおく
i = 0 #式の番号

#ユークリッドの互除法----------
while(r != 0 ):
    q = s // t
    r = s % t
    # 商と余りを式の番号ごとに保存
    qlist.append(q)
    rlist.append(r)
    wlist.append(s)

    s = t
    t = r
    i += 1
#-------------------------

#一次不定方程式------------
i = i - 2

q = qlist[i]
r = rlist[i]
bq = qlist[i-1] #前の式の商
br = rlist[i-1] #前の式の余り
w = wlist[i] #割られる数
bw = wlist[i-1] #前の式の割られる数

k = r #値の保存
v = q = -q
j = 1

while(i > 0):
    q = qlist[i]
    r = rlist[i]
    bq = qlist[i-1]
    br = rlist[i-1]
    w = wlist[i]
    bw = wlist[i-1]
    
    bq = -bq #移項
    
    h = v #値の入れ替え
    v = j + bq * v
    k = q #値の入れ替え
    j = h #値の入れ替え
    
    i = i-1
#-------------------------

print()
print("x ≡",j,"(mod",n,")" )
print()

keymod = np.mod(key,n)
keymod = keymod * j
keymod = np.mod(keymod,n)

print("複合化鍵は")
print(keymod)

cry_ = np.dot(keymod,cry_)
#print(cry_)
cry_ = np.mod(cry_,n)
#print(cry_)

cry = cry_.T
cry = np.ravel(cry)#一次元化

cry = cry.tolist()
#print(cry)


    
for s in range(word_count):
    cry[s] = int(cry[s])
    
if word_count % 2 != 0:
    cry.pop()
    word_count += 1
    
    
print(cry)


cryascii = []
for s in cry:
    ord_num = chr(s+65)  
    cryascii.append(ord_num)
    

print("複合化鍵した結果")
print(cryascii)






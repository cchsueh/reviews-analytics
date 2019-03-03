data = []
count = 0
with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
print('檔案讀取完了,總共有', len(data), '筆資料')

# 文字記數
wc = {}  # word_count
for d in data:
    words = d.split()
    for word in words:
        if word in wc:
            wc[word] += 1
        else:
            wc[word] = 1

for word in wc:
    if wc[word] > 100:
        print(word, wc[word])
print(len(wc))


while True:
    search_word = input('請輸入邀查詢的單字：')
    word = search_word
    if word == 'q':
        print('停止查詢!!')
        break
    if word in wc:
        print(word, '出現', wc[word], '次')
    else:
        print('查無此字!!')
new = []
for d in data:
    if len(d) < 100:
        new.append(d)

new = [d for d in data if len(d) < 100]

print('一共有', len(new), '筆留言長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)

good = [d for d in data if 'good' in d]
print('一共有', len(good), '筆留言裡有good')
print(good[0])
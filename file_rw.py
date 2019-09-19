with open('referat.txt', 'r', encoding='utf-8') as f:
    txt=str(f.read())
    print(f'Всего символов: {len(txt)}')

    txt_words=txt.split()
    txt_words_q=len(txt_words)
    print(f'Всего слов: {txt_words_q}')

    txt_replaced=txt.replace(".", "!")
#print(txt_replaced, file="referat2.txt")
with open('referat2.txt', 'w', encoding='utf-8') as f2:
    f2.write(txt_replaced)
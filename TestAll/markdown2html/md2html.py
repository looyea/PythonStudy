# *.* coding=utf-8 *.*
import codecs

import markdown as md

input_file = codecs.open('ZorMgmt_Func.md', mode='r', encoding='utf-8')

text = input_file.read()

html = md.markdown(text)

out_file = open('test.html', 'w')

out_file.write(html)

out_file.close()

input_file.close()


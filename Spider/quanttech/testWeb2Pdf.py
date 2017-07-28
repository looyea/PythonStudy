# _*_ coding:utf-8 _*_
import pdfkit

url = "http://bbs.quanttech.cn/article/496";

pdfkit.from_url(url, 'out.pdf')
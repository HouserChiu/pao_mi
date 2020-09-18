# coding: utf-8
import re
def format_html(htmlFilePath, saveHtmlFilePath, imgs):
    params_re = re.compile(r'\$\{(img)\}')
    if htmlFilePath:
        try:
            f = open(htmlFilePath, 'r+')
            html_str = f.read()
            # <p style="font-size:0"><img src=${img}></p>  html_str的内容
            # 循环替换
            for img in imgs:
                new_html = re.sub(params_re, img, html_str)
                # 保存路径
                with open(saveHtmlFilePath, 'a+') as f:
                    f.write(new_html)
            # with open(saveHtmlFilePath, 'r') as f:
            #     return f.read()
        finally:
            f.close()
# 购买须知
def get_html_content(filePath):
    with open(filePath, 'r', encoding="UTF-8") as f:
        return f.read()


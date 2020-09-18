# todo: 操作富文本
# coding=utf-8
# Author: tester_pei
import re
def format_html(htmlFilePath, saveHtmlFilePath, imgs):
    params_re = re.compile(r'\$\{(img)\}')
    if htmlFilePath:
        try:
            f = open(htmlFilePath, 'r+')
            html_str = f.read()
            custom_params = re.search(params_re, html_str).group()
            print(custom_params, type(custom_params))
            # 循环替换
            for img in imgs:
                new_html = re.sub(params_re, img, html_str)
                with open(saveHtmlFilePath, 'a+') as f:
                    f.write(new_html)
            with open(saveHtmlFilePath, 'r') as f:
                return f.read()
        finally:
            f.close()

def get_html_content(filePath):
    with open(filePath, 'r', encoding="UTF-8") as f:
        return f.read()

img_src = ["https://image.mydeershow.com/upload/activity/image/business/f7bf83a9-0891-4d77-a713-414c27e72b1b.jpg",
           "https://image.mydeershow.com/upload/activity/image/business/f7bf83a9-0891-4d77-a713-414c27e72b1b.jpg",
           "https://image.mydeershow.com/upload/activity/image/business/f7bf83a9-0891-4d77-a713-414c27e72b1b.jpg",
           "https://image.mydeershow.com/upload/activity/image/business/f7bf83a9-0891-4d77-a713-414c27e72b1b.jpg"]

if __name__ == '__main__':
    file = r'C:\Users\admin\Desktop\sass_pei\商品富文本模板.html'
    saveHtmlFilePath = r'C:\Users\admin\Desktop\sass_pei\8082.html'
    format_html(file, saveHtmlFilePath, img_src)
    path = (r'C:\Users\admin\Desktop\sass_pei\购买须知.html')
    print(get_html_content(path))

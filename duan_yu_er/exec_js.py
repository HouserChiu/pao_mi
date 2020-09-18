import execjs

with open('D:\\webstorm_files\\wan_mei_shi_jie.js',encoding='ANSI') as f:
    data = f.read()
getPass = execjs.compile(data)
p = getPass.call("getpwd","111111")
print(p)

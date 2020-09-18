# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


# jscode = """
# Java.perform(function () {
#     var class_u = Java.use("jd.net.ASCIISortUtil");
#     class_u.formatQueryParaMap.implementation = function (list1, list2) {
#         console.log("Success");
#         var Map = Java.use('java.util.HashMap');
#         var args_x = Java.cast(list1, Map);
#         console.log(args_x.toString());
#         console.log("list2:", list2);
#         var result = this.formatQueryParaMap(list1, list2);
#         console.log(result);
#
#         return result;
#     };
# });
# """

jscode = """
Java.perform(function () {
    var class_u = Java.use("jd.net.ASCIISortUtil");
    class_u.formatQueryParaMap.implementation = function (list1, list2) {
        console.log("Success");
        Java.openClassFile("/data/local/tmp/r0gson.dex").load();
        const gson = Java.use('com.r0ysue.gson.Gson');
        console.log(gson.$new().toJson(list1));
        console.log("list2:", list2);
        var result = this.formatQueryParaMap(list1, list2);
        console.log(result);

        return result;
    };
});
"""



# jscode = """
# var pointer = Module.findBaseAddress("libjdpdj.so").add(0x35AC6 + 1);
# console.log('MD5Update pointer:', pointer);
#
# Interceptor.attach(pointer, {
#     onEnter: function(args) {
#         console.log('参数1:', args[0]);
#         console.log('参数2:', Memory.readCString(args[1]));  // Memory.readCString()就是读取地址为字符串
#         console.log('参数3:', parseInt(args[2]));
#         console.log('----------------');
#     },
#     onLeave: function(retval) {
#     }
# })
# """

# jscode = """
# var pointer = Module.findBaseAddress("libjdpdj.so").add(0x35E7E + 1);
# console.log("hmac_sha256 pointer: ", pointer);
#
# Interceptor.attach(pointer, {
#     onEnter: function(args) {
#         console.log("参数1:", Memory.readUtf8String(args[0]));
#         console.log("参数2:", parseInt(args[1]));
#         console.log("参数3:", Memory.readCString(args[2]));
#         console.log("参数4:", parseInt(args[3]));
#         console.log('---------------');
#     },
#     onLeave:function(retval){
#     }
# });
# """

process = frida.get_usb_device().attach('com.jingdong.pdj')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()

# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

# jscode = """
# Java.perform(function () {
#     var class_u = Java.use("com.maihan.tredian.net.MhRequestUtil");
#     class_u.a.overload('java.util.Map', 'boolean', 'boolean').implementation = function (map, bool1, bool2) {
#         console.log("Success");
#
#
#         var Map = Java.use('java.util.HashMap');
#         var args_x = Java.cast(map, Map);
#         console.log(args_x.toString());
#         console.log("bool1:", bool1);
#         console.log("bool2:", bool2);
#         var result = this.a(map, bool1, bool2);
#         console.log(result);
#         console.log('------------------')
#         console.log('------------------')
#
#         return result;
#     };
# });
# """

# jscode = """
# var pointer = Module.findBaseAddress("libtre.so").add(0x18C6 + 1);
# console.log('SHA1Update pointer:', pointer);
#
# Interceptor.attach(pointer, {
#     onEnter: function(args) {
#         console.log('v32:', args[0]);
#         console.log('v14:', Memory.readCString(args[1])); // Memory.readCString()就是读取地址为字符串
#         console.log('v15:', parseInt(args[2]));
#         console.log('----------------');
#     },
#     onLeave: function(retval) {
#     }
# })
# """

jscode = """
var pointer = Module.findBaseAddress("libtre.so").add(0x188A + 1);
console.log('SHA1Update pointer:', pointer);

Interceptor.attach(pointer, {
    onEnter: function(args) {
        console.log('v10:', Memory.readCString(args[0]));
        console.log('v14:', Memory.readCString(args[1]));  
        console.log('v13:', parseInt(args[2]));
        console.log('----------------');
    },
    onLeave: function(retval) {
    }
})
"""



# jscode = """
# Java.perform(function () {
#     var class_u = Java.use("com.maihan.tredian.net.BaseUrlDealUtil");
#     class_u.b.overload('android.content.Context', 'java.lang.String').implementation = function (str1, str) {
#         console.log("Success");
#         console.log("str1:", str1);
#         console.log("str:", str);
#         var result = this.b(str1, str);
#         console.log(result);
#         console.log('------------------')
#         console.log('------------------')
#
#         return result;
#     };
# });
# """




process = frida.get_usb_device().attach('com.maihan.tredian')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()

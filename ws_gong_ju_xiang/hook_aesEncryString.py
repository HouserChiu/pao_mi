# coding: utf-8

import frida, sys

jscode = """
Java.perform(function () {
    var class_u = Java.use("com.steven.baselibrary.utils.network.AESCipher");
    class_u.aesEncryptString.implementation = function (list1) {
        console.log("Success");
        console.log("list1:", list1);
        var result = this.aesEncryptString(list1);
        console.log(result);
        return result;
    };
});
"""

# jscode = """
# Java.perform(function () {
#     var class_u = Java.use("com.steven.baselibrary.utils.network.AESCipher");
#     class_u.cipherOperation.implementation = function (list1, list2, list3) {
#         console.log("Success");
#         var Map = Java.use('java.util.HashMap');
#
#         var args_y = Java.cast(list2, Map);
#
#         console.log(args_y.toString());
#
#         var result = this.cipherOperation(list1, list2, list3);
#         console.log(result);
#         return result;
#     };
# });
# """


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


process = frida.get_usb_device().attach('com.sdx.weishang')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')

script.load()
sys.stdin.read()



# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var class_u = Java.use("com.basis_library.utils.SystemUtils");
    class_u.getSignature.overload('java.lang.String', 'java.lang.String', 'java.lang.String', 'boolean').implementation = function (str,str2,str3,str4) {
        console.log("got headers");
        console.log("str:"+str);
        console.log("str2:"+str2);
        console.log("str3:"+str3);
        console.log("str4:"+str4);
        var result = this.getSignature(str,str2,str3,str4);
        console.log(result);
        return result;
    };
});
"""

process = frida.get_usb_device().attach('com.bishijie')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()

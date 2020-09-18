# -*- coding: utf-8 -*-

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var class_u = Java.use("com.lawyee.wenshuapp.util.g");
    class_u.b.overload('java.lang.String', 'java.lang.String').implementation = function (str,str2) {
        console.log("got headers");
        console.log("str:"+str);
        console.log("str2:"+str2);      
        var result = this.b(str,str2);
        console.log(result);
        return result;
    };
});
"""

process = frida.get_usb_device().attach('com.lawyee.wenshuapp')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()
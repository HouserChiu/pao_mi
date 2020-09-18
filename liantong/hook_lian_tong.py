# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var class_u = Java.use("com.sinovatech.unicom.a.q");
    class_u.a.implementation = function (list1, list2) {
        console.log("Success");
        console.log("list1:", list1.toJSON());
        console.log("list2:", list2.toJSON());
        var result = this.a(list1, list2);
        console.log(result.toJSON());
        console.log(result.toJSON());
        return result;
    };
});
"""

process = frida.get_usb_device().attach('com.sinovatech.unicom.ui')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()

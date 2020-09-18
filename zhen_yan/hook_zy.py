# coding: utf-8

import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)


jscode = """
Java.perform(function () {
    var class_u = Java.use("com.sensetime.senseid.sdk.liveness.interactive.common.util.StringUtil");
    class_u.sha256 = function (str) {
        console.log("Success");
        console.log("str:", str);
        var result = this.sha256(str);
        console.log(result);
        return result;
    };
});
"""

process = frida.get_usb_device().attach('cn.roleft.mobile.liaoliaoapp')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()



# -*- coding: utf-8 -*-

import frida

def on_message(message, data):
    if message['type'] == 'send':
        print(message['payload'])
    elif message['type'] == 'error':
        print(message['stack'])

def js_code():
    source = '''
    rpc.exports = {
        getsig: function () {
            var ciphertext = "";
            Java.perform(function () {
                var MainActivity = Java.use('com.lawyee.wenshuapp.util.d');
                ciphertext = MainActivity.a()
            })
            return ciphertext
        }
    };
    '''
    return source


# session = frida.get_usb_device().attach('com.lawyee.wenshuapp')
# script = session.create_script(source)
# script.on('message', on_message)
# script.load()
# print(script.exports.getsig())
# session.detach()
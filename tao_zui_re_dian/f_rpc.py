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
                var MainActivity = Java.use('com.maihan.tredian.net.MhRequestUtil');
                ciphertext = MainActivity.a()
            })
            return ciphertext
        }
    };
    '''
    session = frida.get_usb_device().attach('com.maihan.tredian')
    script = session.create_script(source)
    script.on('message', on_message)
    script.load()
    ll = script.exports.getsig()
    return ll


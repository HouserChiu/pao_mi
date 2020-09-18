import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
if(Java.available){
    Java.perform(function () {
        var class_u = Java.use("com.liaoliao.modules.album.PostArticleImgAdapter");
        class_u.getHeaders.implementation = function () {
            console.log("got headers");
            console.log();
            var result = this.getHeaders();
            console.log(result);
            return result;
        };
    });
}
"""

process = frida.get_usb_device().attach('cn.roleft.mobile.liaoliaoapp')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()


rpc.exports = {
    var sig = "";
    getas: function (bArr) {
        Java.perform(
            function () {
                var currentApplication = Java.use('android.app.ActivityThread').currentApplication();
                var context = currentApplication.getApplicationContext();

                var z = Java.use('com.xxx.xxxx.util.AuthUtils');
                sig = AuthUtils.k2(bArr);

            }
        )

    }
    return sig;
};


var pointer = Module.findBaseAddress("libjdpdj.so").add(00035AC6 + 1);
console.log('MD5Update pointer:', pointer);

Interceptor.attach(pointer, {
    onEnter: function(args) {
        console.log('参数1:', args[0]);
        console.log('参数2:', Memory.readCString(args[1]));  // Memory.readCString()就是读取地址为字符串
        console.log('参数3:', parseInt(args[2]));
        console.log('----------------');
    },
    onLeave: function(retval) {
    }
})

var pointer = Module.findBaseAddress("libjdpdj.so").add(0x35E7E + 1);
console.log("hmac_sha256 pointer: ", pointer);

Interceptor.attach(pointer, {
    onEnter: function(args) {
        console.log("参数1:", Memory.readUtf8String(args[0]));
        console.log("参数2:", parseInt(args[1]));
        console.log("参数3:", Memory.readCString(args[2]));
        console.log("参数4:", parseInt(args[3]));
        console.log('---------------');
    },
    onLeave:function(retval){
    }
});



function ab2str(buf) {
    return String.fromCharCode.apply(null, new Uint8Array(buf));
}
function str2ab(str) {
    var buf = new ArrayBuffer(str.length * 2); // 每个字符占用2个字节
    var bufView = new Uint16Array(buf);
    for (var i = 0, strLen = str.length; i < strLen; i++) {
        bufView[i] = str.charCodeAt(i);
    }
    return buf;
}


Java.perform(function(){
    var soAddr = Module.findBaseAddress("libtre.so");
    send('soAddr: ' + soAddr);
    var sha1InputAddr = soAddr.add(0x1744 + 1);
    var resultPtr="";
    send('sha1InputAddr: ' + sha1InputAddr);
    Interceptor.attach(sha1InputAddr, {
        onEnter: function(args){
            var buffer = Memory.readByteArray(args[1], 1000);
            console.log("明文",ab2str(buffer));
        }
    });
});

Java.perform(function () {
    var class_u = Java.use("com.meizu.cloud.pushsdk.platform.b");
    class_u.a.overload('java.util.Map', 'java.lang.String').implementation = function (str, str2) {
        console.log("Success");
        console.log("str:", str);
        console.log("str2:" + str2);
        var result = this.a(str, str2);
        console.log(result);
        return result;
    };
});


Java.perform(function () {
    var class_u = Java.use("com.meizu.cloud.pushsdk.platform.b");
    class_u.a.overload('java.lang.String').implementation = function (str) {
        console.log("Success");
        console.log("str:", str);
        var result = this.a(str);
        console.log(result);
        return result;
    };
});

Java.perform(function () {
    var class_u = Java.use("com.sinovatech.unicom.a.q");
    class_u.a.overload('java.lang.List', 'java.lang.List').implementation = function (list1, list2) {
        console.log("Success");
        // console.log("list1:", list1);
        for (let i = 0; i < list1.length; i++) {
            // console.log(i, ' => ', list1[i])
        }
        // console.log("list2:", list2);
        for (let i = 0; i < list2.length; i++) {
            console.log(i, ' => ', list2[i])
        }
        var result = this.a(list1, list2);
        console.log(result);
        return result;
    };
});


Java.perform(function () {
    /*
    var ShufferMap = Java.use('com.xiaojianbang.app.ShufferMap');
    ShufferMap.show.implementation = function (map) {
        var result = "";
        var keyset = map.keySet();
        var it = keyset.iterator();
        while(it.hasNext()){
            var keystr = it.next().toString();
            var valuestr = map.get(keystr).toString();
            result += valuestr;
        }
        send(result);
        return this.show(map);
    }
    */
    var HashMap = Java.use('java.util.HashMap');
    var ShufferMap = Java.use('com.xiaojianbang.app.ShufferMap');
    ShufferMap.show.implementation = function (map) {
        var hm = HashMap.$new();
        hm.put("user", "dajianbang");
        hm.put("pass", "87654321");
        hm.put("code", "123456");
        return this.show(hm);
    }
});

var Map = Java.use('java.util.HashMap');
var args_map = Java.cast(arguments[j], Map);
console.log(args_map.toString());


var Map = Java.use('java.util.HashMap');
var args_x = Java.cast(x, Map);
send(args_x.toString());


import android

.
content.Context
public

class AuthUtils {
    public static native
    String

    getAS(Context

    context
,
    String
    str
)
    ;
    static {
    System
.

    loadLibrary(

    "native-lib"
)
    ;
}
}

rpc.exports = {
    var sig = "";
    getas: function (str) {
        Java.perform(
            function () {
                var currentApplication = Java.use('android.app.ActivityThread').currentApplication();
                var context = currentApplication.getApplicationContext();

                var AuthUtils = Java.use('com.xxx.xxxx.util.AuthUtils');
                sig = AuthUtils.getAS(context, str);

            }
        )

    }
    return sig;
};


rpc.exports = {
    getsig: function () {
        var ciphertext = "";
        Java.perform(function () {
            send("here")
            varMainActivity = Java.use('com.lawyee.****.util.d');
            ciphertext = MainActivity.a()
        })
        return ciphertext
    }
};



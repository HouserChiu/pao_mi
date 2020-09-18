rpc.exports = {
    getsig: function () {
        var ciphertext = "";
        Java.perform(function () {
            var MainActivity = Java.use('com.maihan.tredian.net.MhHttpEngine');
            ciphertext = MainActivity.a(context, 16, )
        })
        return ciphertext
    }
};
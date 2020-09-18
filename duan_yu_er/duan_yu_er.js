Jn = function () {
    return 56 * parseInt((new Date).getTime() / 1e4, 10)
}
    , Wn = function (t, e) {
    var n = "".concat(t)
        , i = n.substring(0, 1) + n.substring(3, n.length);
    return "".concat(i * e).substring(0, n.length)
}

function getpwd() {
    n = Jn();
    return n;
}

function getd2() {
    d2 = Wn(getpwd(), 314)
    return d2
}

function getd3() {
    d3 = Wn(getpwd(), 128)
    return d3
}

function getd4() {
    d4 = Wn(getpwd(), 435)
    return d4
}

function getd5() {
    d5 = Wn(getpwd(), 219)
    return d5
}

console.log(getpwd())
console.log(getd2())
console.log(getd3())
console.log(getd4())
console.log(getd5())
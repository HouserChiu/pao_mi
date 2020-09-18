# coding: utf-8

import base64
import hashlib

pre_enc = 'android_id=5e5e2620622f1cac&app_ver=67&channel=aliapp&device_id=5b6d40a46894881ee2d54ec17720c1c0&device_udid=8a4084ca6129765f674f02ad8f314a4a&first_time=1597298429&from=app&last_time=1597298406&limit=8&mac=74:AC:5F:CA:D6:47&nonce=9f0nsb1597299041297&os_ver_code=25&system=1&timestamp=1597299041&video_first_time=1597298406&video_last_time=1597298406&with_super=0&with_video=1b2qKgtaW4,9z9D`Fmst?K5JZbLYOY]NP6ssGf2U~;zk9oCNgoytV!}wW7ia+`w9g'
# pre_enc = pre_enc

# temp_sign = base64.b64encode(b'android_id=5e5e2620622f1cac&app_ver=67&channel=aliapp&device_id=5b6d40a46894881ee2d54ec17720c1c0&device_udid=8a4084ca6129765f674f02ad8f314a4a&first_time=1597298429&from=app&last_time=1597298406&limit=8&mac=74:AC:5F:CA:D6:47&nonce=9f0nsb1597299041297&os_ver_code=25&system=1&timestamp=1597299041&video_first_time=1597298406&video_last_time=1597298406&with_super=0&with_video=1b2qKgtaW4,9z9D`Fmst?K5JZbLYOY]NP6ssGf2U~;zk9oCNgoytV!}wW7ia+`w9g')

temp_sign = base64.b64encode(pre_enc.encode('utf-8')).decode()
# temp_sign = temp_sign

print(temp_sign)
# temp_sign = "YW5kcm9pZF9pZD01ZTVlMjYyMDYyMmYxY2FjJmFwcF92ZXI9NjcmY2hhbm5lbD1hbGlhcHAmZGV2aWNlX2lkPTViNmQ0MGE0Njg5NDg4MWVlMmQ1NGVjMTc3MjBjMWMwJmRldmljZV91ZGlkPThhNDA4NGNhNjEyOTc2NWY2NzRmMDJhZDhmMzE0YTRhJmZpcnN0X3RpbWU9MTU5NzI5ODQyOSZmcm9tPWFwcCZsYXN0X3RpbWU9MTU5NzI5ODQwNiZsaW1pdD04Jm1hYz03NDpBQzo1RjpDQTpENjo0NyZub25jZT05ZjBuc2IxNTk3Mjk5MDQxMjk3Jm9zX3Zlcl9jb2RlPTI1JnN5c3RlbT0xJnRpbWVzdGFtcD0xNTk3Mjk5MDQxJnZpZGVvX2ZpcnN0X3RpbWU9MTU5NzI5ODQwNiZ2aWRlb19sYXN0X3RpbWU9MTU5NzI5ODQwNiZ3aXRoX3N1cGVyPTAmd2l0aF92aWRlbz0xYjJxS2d0YVc0LDl6OURgRm1zdD9LNUpaYkxZT1ldTlA2c3NHZjJVfjt6azlvQ05nb3l0ViF9d1c3aWErYHc5Zw=="
eve_sign = hashlib.sha1(str(temp_sign).encode('utf-8')).hexdigest()
print(eve_sign)

#
# 5913c9da8db33f1730a0137e64ad269c320c6817
# 5913c9da8db33f1730a0137e64ad269c320c6817
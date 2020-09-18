color_dict = {'金色': 'https://img.alicdn.com/imgextra/i3/TB1Tc9nv7L0gK0jSZFxt7XWHVXa_083941.jpg_40x40q90.jpg',
              '深空灰色': 'https://img.alicdn.com/imgextra/i2/TB1EE9lv.T1gK0jSZFht7aAtVXa_083941.jpg_40x40q90.jpg',
              '银色': 'https://img.alicdn.com/imgextra/i3/TB1weykv.H1gK0jSZSyt7XtlpXa_083941.jpg_40x40q90.jpg'}
another_dict = {"['无需合约版', '深空灰色', '官方标配', '64GB']": {'price': '4149.00', 'url': ''},
                "['无需合约版', '金色', '官方标配', '64GB']": {'price': '4249.00', 'url': ''},
                "['无需合约版', '银色', '官方标配', '64GB']": {'price': '4249.00', 'url': ''}}
other_dict = {}
for key3, value3 in another_dict.items():
    key4 = eval(key3)
    for y in key4:
        if y in color_dict:
            other_dict['%s' % key3] = {'price': '%s' % value3['price'], 'url': '%s' % color_dict[y]}
print(other_dict)

other_dict = {
    "['无需合约版', '深空灰色', '官方标配', '64GB']": {'price': '4149.00', 'url': 'https://img.alicdn.com/imgextra/i2/TB1EE9lv.T1gK0jSZFht7aAtVXa_083941.jpg_40x40q90.jpg'},
    "['无需合约版', '金色', '官方标配', '64GB']": {'price': '4249.00', 'url': 'https://img.alicdn.com/imgextra/i3/TB1Tc9nv7L0gK0jSZFxt7XWHVXa_083941.jpg_40x40q90.jpg'},
    "['无需合约版', '银色', '官方标配', '64GB']": {'price': '4249.00', 'url': 'https://img.alicdn.com/imgextra/i3/TB1weykv.H1gK0jSZSyt7XtlpXa_083941.jpg_40x40q90.jpg'}
}

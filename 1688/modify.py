# coding: utf-8
import os
import time
from lxml import etree
import requests
import urllib3
import re
import json
from headers_lists import get_headers3, get_headers4, get_headers5, get_headers7, get_headers8, get_headers9, \
    get_headers2
from params_lists import get_params2, get_params3, get_params4
from info_mongoimport import mongo_info_alibaba
from handle_template import format_html


def get_cate():
    # url = 'https://dcms.1688.com/open/query.json'
    # urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    # res = requests.get(url, params=get_params1(), headers=get_headers1(), verify=False).text
    # temp = re.search('\((.*?)\)', res, re.S).group(1).replace('\\', '')
    # eve1 = re.findall(r'\"word\":\"(.*?)\"', temp, re.S)
    # print(eve1)
    # ['服饰内衣', '运动户外', '女装', '羊绒大衣', '短袖t恤女', '加绒打底裤', '劳保工作服', '雪纺衫', '婚纱', '修身连衣裙', '修身针织衫', '夏季女装', '羽绒服女',
    #  '针织开衫', '夏装新款连衣裙', '短裤女', '品牌连衣裙', '卫衣', '小脚裤', '羊绒衫', '高端女装', '短裤', '韩版女装', '中老年妈妈装', '内衣', '内裤女士',
    #  '女士内衣', '文胸内衣', '袜子', '內衣', '女士内裤', ]
    cate_list = ['内衣文胸', '胸罩', '收腹裤', '隐形文胸', '孕妇文胸', '卫裤', '地摊袜子', '儿童袜子', '平角内裤',
                 '丝袜', '文胸聚拢', '丝袜连裤袜', '纯棉睡衣', '拉拉女神', '纯棉袜子', '男装', '工装', '男式夹克', '男式印花T恤', '男t恤', '短袖t恤定做', '夹克男',
                 '长裤', 't恤男式', '牛仔裤男', 't恤圆领', '空白T恤', '运动裤', '圆领T恤', '文化衫', '男式t恤', '羽绒服', '男式毛衣', '空白t恤', '运动户外服装',
                 '男式冲锋衣', '男冲锋衣', '冲锋衣三合一', '作训服', '防晒衣男', '运动衣', '运动短裤', '冲锋衣户外', '夏短裤', '防晒皮肤衣', '抓绒衣', '自行车服', '紧身衣',
                 '女短裤', '瑜伽健身服', '运动T恤', '户外服装', '户外冲锋衣', '运动户外鞋包', '迷彩跑鞋多威', '羽毛球鞋', '户外鞋', '作战靴', '花花公子', '男足球鞋',
                 '工具包应急包', '运动鞋鞋', '臂包', '卡通手机防水袋', '战术水袋', '防水手机袋', '背包', '手机防水套', '运动鞋', '07a作训鞋', '战术背包', '军训迷彩鞋',
                 '篮球鞋', '竹炭鞋垫', '小腰包', '运动健身器材', '足球人造草坪', '甩脂机', '丙烯酸', '8字拉力器', '塑胶草坪', '浙江篮球架', '围网', '草坪仿真',
                 '乒乓球发球机', '塑身机抖抖机', '泡棉滚筒', '健身器材单杠', '人造草皮', '跳床', '球场围网', '液压篮球架', '永康健身器材', '塑胶篮球场', '硅pu球场',
                 '臂力器拉力器', '拉力器扩胸器', ]

    # '日用百货', '食品饮料', '工艺品、礼品', '装饰品', '徽章', '钥匙圈', '马口铁胸章', '相框', '气球', '金属工艺品', '金属钥匙扣', '创意沙漏', '手机防滑垫', '花盆', '木质工艺品', '纪念币', '气球广告', '金属徽章', '促销礼品', '沙漏', 'pvc钥匙扣', '生日蜡烛', '用品',
    # '胸章', '宠物及园艺', '多肉植物', '黑麦草种子', '竹子', '桂花树', '景观石', '穴盘育苗盘', '宠物用品', '育苗基质', '千层石', '狗衣服', '宠物垫',
    # '育苗盘', '72孔育苗穴盘', '各种花盆', '围栏', '笼子', '营养钵', '鸟笼', '猫玩具', '樱花苗', '烟油', '玻璃杯', '杯垫', '饭盒', '置物架', '开瓶器',
    # '保温饭盒', '购物车', '太阳伞', '暖宝宝', '强光手电筒', '厨房置物架', '勺子', '垃圾袋', '保温袋', '收纳袋', '打火机', '陶瓷刀', '青花瓷碗', '电子秤',
    # '电子烟', '眼镜及配件', '新款太阳镜', '儿童蛤蟆镜', '夜视镜', '太阳墨镜', '复古太阳镜', '金属眼镜', '男士眼镜', '声控发光眼镜', '儿童眼镜', 'vr眼镜',
    # '太阳镜盒', '江湖老花镜', '眼镜架', '太阳镜女士', '眼镜', '复古眼镜', '纤维眼镜布', '夹片', 'tr90眼镜架', 'TR90眼镜框', '游泳眼镜', '食品', '槟榔',
    # '海参', '酵素果冻', '瓜子', '野燕麦', '鱿鱼丝', '巧克力', '代餐粉', '红枣', '玛咖', '零食', '阿胶糕', '进口零食', '休闲食品', '牛肉干', '阿胶',
    # '零食食品', '进口食品', '枸杞', '糖果', '杏仁', '饮料', '蜂蜜', '红糖', '法国进口葡萄酒', '袋泡茶', '干果', '白茶', '茶叶', '红树莓酒', '玫瑰花茶',
    # '苦荞茶', '牛栏山', '纯天然蜂蜜', '茉莉花茶', '奶粉', '小米', '普洱茶', '红茶', '调料', '三七', '啤酒', '茅台',
    #
    # '母婴', '玩具', '童装', '宝宝袜', '童T恤', '韩版亲子装', '宝宝袜子', '公主裙', '亲子装', '童裙', '童装羽绒服', '秋季童装', '新款童装', '儿童内衣', '女童连衣裙', '儿童羽绒服',
    # '男女童装', '婴儿连体衣', '儿童长裤', '春款童装', '泡泡枪', '芭比娃娃', '四轴飞行器', '地摊玩具', '积木', '儿童礼物', '早教机', '戏水玩具', '儿童益智玩具',
    # '毛绒公仔', '婴幼儿玩具', '充气城堡', '早教玩具', '沙滩球', '有声挂图', '玩具球', '儿童玩具', '婚庆娃娃', '礼物', '磁力片', '母婴用品', '宝宝罩衣',
    # '孕妇裤打底裤', '隔汗巾', '围嘴', '婴儿纸尿裤', '湿巾', '睡袋', '安全别针', '夏季孕妇装', '隔尿垫', '妈咪包', '三角口水巾', '婴儿腰凳', '婴儿床',
    # '宝宝围兜', '浴巾', '洗头帽', '尿裤', '纸尿裤', '婴儿用品', '婴儿车',
    #
    # '鞋包', '配饰', '鞋靴', '儿童雪地靴', '跑步鞋', '凉鞋新款', '真皮凉鞋', '凉拖鞋', '品牌童鞋', '劳保鞋', '凉鞋厚底', '夏季拖鞋', '新款儿童鞋', '休闲鞋女', '女童凉鞋', '运动休闲鞋', '卡通拖鞋', '高跟鞋', '新款童鞋', '厚底女鞋',
    # '真皮小白鞋', '沙滩鞋', '豆豆鞋', '箱包', '女士钱包', '手包', '草编包', '广州女包', '卡包', '斜挎小包', '零钱包', '男包', '地摊货源', '胸包',
    # '民族风包包', '男士钱包', '女包新款', '欧美包包', '小包', '女包单肩', '錢包', '学生书包', '万向轮拉杆箱', '太阳帽', '水晶手链', '袖扣', '真皮皮带',
    # '玛瑙散珠', '皮带扣', '鸭舌帽', '儿童发饰', '丝巾', '棒球帽', '韩版饰品', '头巾', '手环', '帽子韩版', '毛衣链', '领带', '发带', '精品礼物', '腰带',
    # '发饰', '小叶紫檀手串',
    #
    # '美妆', '日化', '美容护肤市场', '面膜贴', '曼秀雷敦', '婴儿面膜', '美白蚕丝面膜', '化妆品OEM', '香皂', '乳液', '面膜oem', '洁面膏', '青春定格液', '原液玻尿酸保湿', '男士须后水', '薰衣草纯露', '洗面奶洁面乳', '免洗睡眠面膜', '韩国男士化妆品', '软膜粉', '修复因子微针', '韩洛依',
    # '整形原液', '控油祛痘洗面奶', '身体护理市场', '缩阴凝胶', '泡脚粉', '进口精油', '按摩油', '田七一洗白', '希腊橄榄油', '脚气喷剂', '初榨橄榄油', '脚臭',
    # '薰衣草精油', '护手霜', '牛奶沐浴露', '葡萄籽油', '泡澡药包', '单方精油', '精油原料', '棒女郎', '浴盐', '喷剂', '中药肚脐贴', '家清纸品/女性护理市场',
    # '湿巾定做', '抽纸纸巾', '大盘纸', '厕纸', '钱夹纸巾', '盒装面巾纸', '广告荷包纸巾', '面巾纸', '盒装纸巾', '抽纸', '成人纸尿裤', '卷纸', '定做餐巾纸',
    # '护理垫', '酒店专用小盘纸', '手帕纸', '卫生巾立体绵网', '广告湿巾', '卫生巾', '彩妆/化妆工具市场', '眉夹', 'mts', '牛角梳', '色料', '洗脸刷', '檀木梳',
    # '面膜碗', '单支化妆刷', '面膜', '嫁接假睫毛', '专业化妆刷', '粉扑', '种植睫毛', '纹身机', '嫁接睫毛', '腮红刷', '洗面扑', '画眉卡', '塑料梳子',
    # '美容棒', '理发剪刀', '美发造型市场', '正品洗发水', '发泥', '马油洗发水', '美发产品', '白发', '洗发水oem', '染发剂', '伉美沅补水神器', 'coco洗发水',
    # '还原酸护发素', '染发粉', '控油洗发水', '染发笔', '去屑洗发水', '正品发膜', '日用品', '染发蜜粉', '护发素', '植物染发剂', '补水神器', '理发围布',
    # '家庭清洁市场', '清洁用品', '万能去污膏', '万用去污膏', '皮革手感剂', '展销会', '万能去污清洁膏', '除味竹炭包', '洗衣机槽清洁剂', '超能', '汽车香水', '半成品',
    # '地板清洗剂', '熏香', '洗衣粉出口', '地板护理精油', '家用空调清洗剂', '清洁护理皮具', '精油', '好太太洗衣液', '尘推油',
    #
    # '数码家电', '汽车用品', '数码/电脑', '手表手机', '手机数据线', '迷你自拍杆', '手机钢化膜', '手机皮套', '手机充电器', '无线鼠标', '屏蔽器', '保护套', 'usb充电器', '手机套', '车载支架',
    # '电源适配器', '头戴式耳机', '苹果6手机壳', '耳机', '懒人手机支架', '移动电源套料', '充电器', '万能手机套', '家用电器', '酸奶机', '除湿机', '户外音响',
    # '电视', '蒸汽挂烫机', '饮水机', '液晶电视机', '挂烫机', '液晶电视', '电风扇', '剃须刀', '电动牙刷头', '电热水龙头', '看戏机', '灶具', '蓝牙音箱',
    # '理发器', '直发梳', '蓝牙音响', '电视支架', '理疗仪', '防锈蜡', '摩托车大灯', '静电贴', '倒车摄像头', '车载烟灰缸', '汽车坐垫', '发动机护板', '导航',
    # '后视镜', '车位锁', '道闸', '座垫', '电动观光车', '玻璃水配方', '汽车挂件', '电动车挡风被', '密封条', '小圆镜', '蜡掸', '车充',
    #
    # '机械', '五金', '仪表', '机械及行业设备', '离心泵', '玻璃钢化粪池', '铆钉', '清洗机', '自动售货机', '电动调节阀', '高压清洗机', '生产线', '汽车烤漆房', '数控切割机',
    # '螺丝', '超市货架', '不锈钢螺丝', '气动隔膜泵', '真空泵', '轴承', '除尘器', '锅炉', '流水线', '五金/工具/机床', '机床', '摇臂钻', '砂轮', '倒角机',
    # '气动冲床', '防水接头', '打气筒', '升降机', '扭力扳手', '剪扳机', '真空吸盘', '锯床', '车床', '滚丝机', '钳工工作台', '丝杆', '喷头', '剪刀',
    # '井盖', '内六角扳手', '自动抛光机', '仪器/仪表', '温湿度计', '电子称', '涂层测厚仪', '水表', '动平衡机', '鼓风干燥箱', '高低温试验箱', '气体检测仪',
    # '流量计', '电能表', '试验机', '热电偶', '电子拉力试验机', '冷热冲击试验箱', '电阻测试仪', '耐震压力表', '恒温恒温试验箱', '测试仪', '温度计', '磁翻板液位计',
    #
    # '包装', '办公文教', '物流包装/辅材市场', '塑料托盘', '泡沫箱', '扎带', '彩盒', '不干胶贴纸', '纸盒', '自封袋', '封箱胶带', '托盘', '编织袋',
    # '纸箱定做', '背心袋', '纸箱', '包装盒', '茶叶包装盒', '无纺布环保袋', '环保袋', '气柱袋', '铝箔袋', '透明胶带', '塑料包装市场', '水写布', '签字笔',
    # '橡皮', '蜡烛', '金蛋', '金属圆珠笔', '档案盒', '文件夹', '收银纸', '复印纸', '便利贴', '黑板', '硒鼓', '画架', '打孔机', '荧光棒', '商务笔记本',
    # '台历', '相册', '仿真花', '纸包装/布包装/其他包装市场', '屏风', '传真机', '投影机', '打印机', '磁带', '墨盒', '色带', '电脑椅', '文件柜', '排椅',
    # '碎纸机', '一体机', '书桌', '大班桌', '办公桌', '办公沙发',
    #
    # '电工', '安防', '电工、电气市场', '开关电源', '加热器', '振动电机', '导热硅胶片', '电力电缆', '墙壁开关', '硅胶线', '触摸开关', '马弗炉', '高温线', '空气开关', '烘箱', '控制柜', '伺服电机', '电缆桥架', '逆变器', '音频线', '电木板',
    # '轻触开关', '工业烤箱', '无尘布', '个人防护市场', '离子风枪', '防护面屏', '防尘口罩', '安全帽', '防护耳塞', '防割手套', '棉安全套', '防护服', '棉安全帽',
    # '防静电刷', '玻璃钢安全帽', '防尘服', '一次性防护', '电焊服', '防砸防刺穿', '隔热服', '防护鞋', '洗眼器', '一次性口罩', '防冲击眼镜', '防毒面具',
    # '消防/监控市场', '钢质防火门', '闭门器', '金属检测机', '反光膜', '无线摄像头', '护栏', '智能卡', '道路护栏', '液晶拼接屏', '浪涌保护器', '灭火器',
    # '太阳能爆闪灯', '橡胶减速带', '门铃', '安全柜', '边坡防护网', '监控支架', '声光报警器', '消防水带', '监控摄像头',
    #
    # '照明', '电子', '照明市场', '应急灯', '路灯杆', 'LED应急灯', '铝型材', '灯具', 'led中国结', '灯泡', '彩灯', 'elt恤', '家用太阳能灯', '舞台灯光', 'led灯串', '树灯', '紫外线灯管',
    # 'led灯泡', '陶瓷灯头', '照明路灯', '三防灯', '灯杆', '太阳能庭院灯', '灯串', 'LED灯配城', '套件', 'led日光灯', 'led日光灯管', '投光灯外壳',
    # 'LED工矿灯', '灯珠', 'LED灯带', '灯带', '服装店射灯', '日光灯管', 'led节能灯', 'LED投光灯', 'led节能灯泡', 'led应急灯', 'led灯珠',
    # 'led天花灯', '电子市场', '电路板', '工字电感', '液晶屏', '金属膜电阻', '场效应管', '电容', '贴片保险丝', '电容器', 'pcb线路板', 'fpc', '陶瓷管',
    # '激光器', '端子', '保险丝', '电解电容', '汽车保险丝', '小型继电器', '陶瓷片', '散热器', '贴片电感',
    #
    # '家装建材', '家纺家饰', '五金主材', '折叠桌', '防水卷材', '烧结砖', '塑木地板', '弯头', '浴室柜', '鞋柜', '阳光板', '合页', '彩钢夹芯板', '餐桌椅', '办公椅', '花洒', '耐力板', '马桶', '书架',
    # '家具', '椅子', '瓷砖', '干发帽', '酒店床上用品', '蚊帐', '记忆枕', '宾馆床上用品', '抱枕芯', '地毯地垫', '四件套', '酒店毛巾', '蚕丝被', '被芯',
    # '纯棉浴巾', '坐垫', '绣花窗帘', '床上四件套', '毯子', '窗帘', '宾馆用品', '窗帘布', '家具灯具', '吧台椅', '办公屏风', '学生床', '工程灯具', '创意灯具',
    # '课桌椅', '地灯', '酒店台灯', '儿童凳', '吸顶灯', '鞋架',
    #
    # '橡塑', '化工', '冶金矿产', '过滤网', '珍珠岩', '铝棒', '筛网', '钢丝网', '铝合金', '强磁', '冲孔网', '稀土', '网片', '铅板', '圆形磁铁', '铜套', '型材', '哈氏合金', '钕铁硼', '紫铜板', '6061铝板', '1060铝板', '精细化学品',
    # '聚丙烯酸钠', '麦芽糊精', '阻垢剂', '超声波清洗剂', '明胶', '油漆', '防锈油', '高温润滑脂', '木糖醇', '荧光增白剂', '魔芋粉', '稀释剂', '香精',
    # '颗粒活性炭', '环氧地坪漆', '高岭土', '增稠剂', '防水涂料', '涂料', '絮凝剂', 'pp管', 'TPE', '塑料水箱', '硅胶密封圈', '亚克力', 'pe给水管',
    # '硅胶板', '软管', '橡胶圈', '透明胶垫', 'PP板', '塑料', '尼龙管', '薄膜', '硅胶充气密封圈', 'abs', 'pom', '橡胶减震器', '排水管', 'abs板',
    # '橡胶脚垫', '氧化铝', '包装海绵', 'ab胶水', '高分子树脂', '塑料量杯', '磷酸二氢钾', '水性聚氨酯树脂', '硝酸钾', '海绵', '硬脂酸', '磷酸三钠', '漏斗',
    # '工艺品树脂', 'edta四钠', '阳离子交换树脂', '铅玻璃生产', '氢氧化镁', '海棉', '水杨酸', '无碱玻璃纤维布', '发泡海绵', '能源', '乳化沥青', '120号溶剂油',
    # '煤油', '环保燃料', '彩色沥青', '块煤', '沥青', '液化气气化炉', '脱臭煤油', '生物颗粒', '东莞柴油', '柴油0', '风力发电机叶片', '无烟煤', '电池板',
    # '生物质燃料', '200溶剂油', '进口石油焦', '石油沥青', '神木煤炭',
    #
    # '钢铁', '热轧板卷', '普热轧板', '普热轧卷', 'Q235B', '花纹板', '花纹卷', 'Q235', '低合金板', '低合金卷', 'Q345B', '冷轧涂镀类', '涂镀', '镀锌板', '镀锌卷', 'DX51D', '彩涂板卷', '镀铝', '冷轧板卷', '冷轧板',
    # 'SPCC', '不锈钢类', '不锈钢板', '不锈钢带', '不锈钢管', '不锈钢圆管', '不锈钢方管', '不锈钢焊管', '304不锈钢', '201不锈钢', '316不锈钢',
    # '建材型材', '螺纹钢', '圆钢', '槽钢', '盘螺', 'H型钢', '扁钢', '角钢', '工字钢', '高线', '管材', '无缝管', '焊管', '20#钢管', '圆管',
    # '方管', '矩管', '镀锌管', '方矩管', '螺旋管', '中厚板及其他', '中厚板', '普中板', '中厚板加工', '带钢', '硅钢', '优特钢', '不锈钢镜面板']
    return cate_list


def get_params(cate, i):
    params2 = [
        {'beginpage': '%s' % i, 'asyncreq': '1', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
        {'beginpage': '%s' % i, 'asyncreq': '2', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
        {'beginpage': '%s' % i, 'asyncreq': '3', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
        {'beginpage': '%s' % i, 'asyncreq': '4', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
        {'beginpage': '%s' % i, 'asyncreq': '5', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
        {'beginpage': '%s' % i, 'asyncreq': '6', 'keywords': '%s' % cate, 'sortType': '', 'descendOrder': '',
         'province': '', 'city': '', 'priceStart': '', 'priceEnd': '', 'dis': '',
         'spm': 'a2609.11209760.it2i6j8a.30.44292de113BNUL', 'cosite': 'baidujj_pz', 'trackid': '{trackid}',
         'location': 're', 'pageid': '17145fa7ralgjD', 'p4pid': 'd2fef991cc224360934c4c4d84f38001',
         'callback': 'jsonp_{}_51591'.format(int(round(time.time() * 1000))),
         '_': '%s' % int(round(time.time() * 1000)), },
    ]
    yield params2


def one_page(params, headers_eve):
    url = 'https://data.p4psearch.1688.com/data/ajax/get_premium_offer_list.json'
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=headers_eve, params=params, verify=False).text
    res_temp = '{"data' + re.search('data(.*?)ret', res, re.S).group(1).rstrip('"').rstrip(',') + '}'
    res_eve = json.loads(res_temp)
    if res_eve["data"] != {}:
        temp = re.findall(r'\"eurl\":\"(.*?)\"', res, re.S)
        for eve in temp:
            # print(eve)
            yield eve


def get_detail(url):
    print(url)
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    res = requests.get(url, headers=get_headers3(), verify=False).text
    product_info = {}
    product_info['title'] = ''.join(etree.HTML(res).xpath("//html[@lang='zh-CN']/head/title/text()"))
    product_info['shop_name'] = re.search('<meta.*?og:product:nick.*?name=(.*?);.*?>', res, re.S).group(1)
    product_info['goods_id'] = re.search('<meta.*?b2c_auction.*?content=\"(\d+)\".*?>', res, re.S).group(1)
    product_info['source'] = "https://detail.1688.com/offer/{}.html".format(product_info['goods_id'])
    # 商品图，创建product_img文件夹并下载图片
    product_info['imgsSrc'] = re.findall('<li.*?tab-trigger.*?original\"\:\"(.*?)\"', res, re.S)
    os.chdir('C:/Users/admin/Desktop/1688')
    if os.path.exists('./4/' + '%s' % product_info['goods_id']) == False:
        os.makedirs('./4/' + '%s' % product_info['goods_id'] + '/product_img')
        os.chdir('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/product_img')
        i = 1
        for temp_img in product_info['imgsSrc']:
            with open('%s' % i + '.jpg', 'wb') as f:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                eve_image = requests.get(temp_img, verify=False).content
                f.write(eve_image)
                i += 1

        # 视频页面,创建product_video文件夹并下载视频
        memberId = re.search('member_id.*?\"(.*?)\"', res, re.S).group(1)
        videoId = re.search('videoId.*?\"(\d+)\"', res, re.S).group(1)
        if videoId != '0':
            res2 = requests.get('https://apps.1688.com/event/app/videoInfo/getVideoById.htm',
                                params=get_params3(videoId, memberId), headers=get_headers4(), verify=False).text
            os.chdir('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'])
            os.mkdir('./product_video')
            os.chdir('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/product_video')
            with open('%s' % product_info['goods_id'] + '.mp4', 'wb') as f:
                urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                video = requests.get(product_info['videoUrl'], verify=False).content
                f.write(video)
            if os.path.getsize('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/product_video/' + '%s' % product_info['goods_id'] + '.mp4') < 10000:
                product_info['videoUrl'] = re.search('address\"\:\"(.*?)\"', res2, re.S).group(1)
            else:
                pass
        try:
            # 分销、代发页面
            url3 = 'https://detail.1688.com/offer/{}.html?sk=consign'.format(product_info['goods_id'])
            res3 = requests.get(url3, headers=get_headers7(product_info['goods_id']), verify=False,
                                allow_redirects=False, timeout=None).text
            # 是否有分销界面解析规则不一样
            try:
                skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res3, re.S).group(1).rstrip('"').strip().rstrip(
                    ',')
                skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res3, re.S).group(1).rstrip('"').strip().rstrip(
                    ',').rstrip(
                    '}').strip().rstrip(',')
                Specifications1 = json.loads(skuProps)
                Specifications2 = json.loads(skuMap)

            except json.decoder.JSONDecodeError:
                skuProps = '[' + re.search('skuProps.*?\[(.*?)skuMap', res3, re.S).group(1).rstrip('"').strip().rstrip(
                    ',')
                skuMap = '{' + re.search('skuMap.*?\{(.*?)end', res3, re.S).group(1).strip().rstrip(',')
                Specifications1 = json.loads(skuProps)
                Specifications2 = json.loads(skuMap)

            product_info['spcification_amount'] = skuProps

            base_price = re.search('consignBasePrice\"\:\"(.*?)\"', res3, re.S).group(1)
            if '-' in base_price:
                base_price_eve = base_price.split('-')[1]
            else:
                base_price_eve = base_price

            # 运费页面
            url4 = 'https://laputa.1688.com/offer/ajax/widgetList.do'
            res4 = requests.get(url4, headers=get_headers9(product_info['goods_id']),
                                params=get_params4(product_info['goods_id']),
                                verify=False).text
            res_temp = '{"data' + re.search('data(.*?)message', res4, re.S).group(1).rstrip('"').rstrip(',') + '}'
            res_eve = json.loads(res_temp)
            if res_eve['data']['data']['offerdetail_ditto_postage']['showFreightCost'] == False:
                fee = 10
            elif res_eve['data']['data']['offerdetail_ditto_postage']['freightCost'] == []:
                fee = 0
            else:
                fee = res_eve['data']['data']['offerdetail_ditto_postage']['freightCost'][0]['costItems'][0]['value']
            # 产品最终价格，分销/代发价+运费
            product_info['price'] = float(base_price_eve) + float(fee)

            # 有规格图，无价格
            img_dict = {}
            for value_eve in Specifications1:
                for vv_eve in value_eve['value']:
                    if "imageUrl" in vv_eve.keys():
                        img_dict["%s" % vv_eve["name"]] = {"price": "", "url": vv_eve['imageUrl']}
            # 有价格，无规格图
            price_dict = {}
            for k, v in Specifications2.items():
                if "price" in v.keys():
                    price_dict[k.replace('gt;', '').replace("/", "").replace("*", "")] = {'price': v['price'],
                                                                                          'url': ''}
                else:
                    price_dict[k.replace('gt;', '').replace("/", "").replace("*", "")] = {
                        'price': product_info['price'],
                        'url': ''}
            # 构建新的json，含有价格和规格图，存入新的文件中
            for key1, value1 in img_dict.items():
                for key2, value2 in price_dict.items():
                    if key1 in key2:
                        price_dict['%s' % key2]['url'] = img_dict['%s' % key1]['url']

            product_info['spcification'] = price_dict
            # 创建规格文件夹颜色
            os.chdir('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'])
            os.makedirs('./product_specifications/color')
            os.chdir(
                'C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/product_specifications/color')
            with open('%s' % product_info['goods_id'] + '.json', 'w') as fp:
                fp.write(json.dumps(price_dict, indent=4, ensure_ascii=False))
            for key3, value3 in price_dict.items():
                with open('%s' % key3 + '.jpg', 'wb') as f:
                    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
                    if "https" in value3['url']:
                        specification_img = requests.get(value3['url'], verify=False).content
                        f.write(specification_img)
            # 尺寸
            if len(Specifications1) >= 2:
                os.chdir('C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'])
                os.makedirs('./product_specifications/size')
                os.chdir(
                    'C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/product_specifications/size')
                for key4 in Specifications1:
                    for kk_eve in key4['value']:
                        with open('%s' % kk_eve['name'].replace("/", "").replace("*", "") + '.txt', 'w') as f:
                            f.write('1')
        except AttributeError:
            pass

        # 富文本图链接
        html_url = re.search('data-tfs-url=\"(.*?)\"', res, re.S).group(1)
        params = {'t': '%s' % int(round(time.time() * 1000))}
        res1 = requests.get(html_url, headers=get_headers5(), params=params, verify=False).text.replace('\\', '')

        # 匹配图片用于富文本构造
        result = re.findall('alt.*?src=\"(.*?)\"', res1, re.S)
        file = 'C:/Users/admin/Desktop/1688/html_template.html'
        saveHtmlFilePath = 'C:/Users/admin/Desktop/1688/4/' + '%s' % product_info['goods_id'] + '/' + '%s' % \
                           product_info[
                               'goods_id'] + '.html'
        # 参数依次为富文本模板，保存路径，图片列表
        format_html(file, saveHtmlFilePath, result)
        print(product_info)
        mongo_info_alibaba.insert_item(product_info)


def main(cate, i, headers_eve):
    params3 = get_params(cate, i)
    for params2 in params3:
        for params1 in params2:
            url_temp = one_page(params1, headers_eve)
            for url_eve in url_temp:
                get_detail(url_eve)


if __name__ == '__main__':
    cates = get_cate()
    for cate in cates:
        headers_eve = get_headers2(cate)
        for i in range(1, 51):
            main(cate, i, headers_eve)
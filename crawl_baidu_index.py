import datetime
import json
import time
import pandas as pd
import requests

province_dict = {
        "山东省":'901',
        "贵州省":'902',
        "江西省":'903',
        "重庆市":'904',
        "内蒙古自治区":'905',
        "湖北省":'906',
        "辽宁省":'907',
        "湖南省":'908',
        "福建省":'909',
        "上海市":'910',
        "北京市":'911',
        "广西壮族自治区":'912',
        "广东省":'913',
        "四川省":'914',
        "云南省":'915',
        "江苏省":'916',
        "浙江省":'917',
        "青海省":'918',
        "宁夏回族自治区":'919',
        "河北省":'920',
        "黑龙江省":'921',
        "吉林省":'922',
        "天津市":'923',
        "陕西省":'924',
        "甘肃省":'925',
        "新疆维吾尔自治区":'926',
        "河南省":'927',
        "安徽省":'928',
        "山西省":'929',
        "海南省":'930',
        "台湾省":'931',
        "西藏自治区":'932',
        "香港特别行政区":'933',
        "澳门特别行政区":'934',
}
citycode2name_dict = {
    '1':"济南市",
    '2':"贵阳市",
    '3':"黔南布依族苗族自治州",
    '4':"六盘水市",
    '5':"南昌市",
    '6':"九江市",
    '7':"鹰潭市",
    '8':"抚州市",
    '9':"上饶市",
    '10':"赣州市",
    '11':"重庆市",
    '13':"包头市",
    '14':"鄂尔多斯市",
    '15':"巴彦淖尔市",
    '16':"乌海市",
    '17':"阿拉善盟",
    '19':"锡林郭勒盟",
    '20':"呼和浩特市",
    '21':"赤峰市",
    '22':"通辽市",
    '25':"呼伦贝尔市",
    '28':"武汉市",
    '29':"大连市",
    '30':"黄石市",
    '31':"荆州市",
    '32':"襄阳市",
    '33':"黄冈市",
    '34':"荆门市",
    '35':"宜昌市",
    '36':"十堰市",
    '37':"随州市",
    '38':"恩施土家族苗族自治州",
    '39':"鄂州市",
    '40':"咸宁市",
    '41':"孝感市",
    '42':"仙桃市",
    '43':"长沙市",
    '44':"岳阳市",
    '45':"衡阳市",
    '46':"株洲市",
    '47':"湘潭市",
    '48':"益阳市",
    '49':"郴州市",
    '50':"福州市",
    '51':"莆田市",
    '52':"三明市",
    '53':"龙岩市",
    '54':"厦门市",
    '55':"泉州市",
    '56':"漳州市",
    '57':"上海市",
    '59':"遵义市",
    '61':"黔东南苗族侗族自治州",
    '65':"湘西土家族苗族自治州",
    '66':"娄底市",
    '67':"怀化市",
    '68':"常德市",
    '73':"天门市",
    '74':"潜江市",
    '76':"滨州市",
    '77':"青岛市",
    '78':"烟台市",
    '79':"临沂市",
    '80':"潍坊市",
    '81':"淄博市",
    '82':"东营市",
    '83':"聊城市",
    '84':"菏泽市",
    '85':"枣庄市",
    '86':"德州市",
    '87':"宁德市",
    '88':"威海市",
    '89':"柳州市",
    '90':"南宁市",
    '91':"桂林市",
    '92':"贺州市",
    '93':"贵港市",
    '94':"深圳市",
    '95':"广州市",
    '96':"宜宾市",
    '97':"成都市",
    '98':"绵阳市",
    '99':"广元市",
    '100':"遂宁市",
    '101':"巴中市",
    '102':"内江市",
    '103':"泸州市",
    '104':"南充市",
    '106':"德阳市",
    '107':"乐山市",
    '108':"广安市",
    '109':"资阳市",
    '111':"自贡市",
    '112':"攀枝花市",
    '113':"达州市",
    '114':"雅安市",
    '115':"吉安市",
    '117':"昆明市",
    '118':"玉林市",
    '119':"河池市",
    '123':"玉溪市",
    '124':"楚雄彝族自治州",
    '125':"南京市",
    '126':"苏州市",
    '127':"无锡市",
    '128':"北海市",
    '129':"钦州市",
    '130':"防城港市",
    '131':"百色市",
    '132':"梧州市",
    '133':"东莞市",
    '134':"丽水市",
    '135':"金华市",
    '136':"萍乡市",
    '137':"景德镇市",
    '138':"杭州市",
    '139':"西宁市",
    '140':"银川市",
    '141':"石家庄市",
    '143':"衡水市",
    '144':"张家口市",
    '145':"承德市",
    '146':"秦皇岛市",
    '147':"廊坊市",
    '148':"沧州市",
    '149':"温州市",
    '150':"沈阳市",
    '151':"盘锦市",
    '152':"哈尔滨市",
    '153':"大庆市",
    '154':"长春市",
    '155':"四平市",
    '156':"连云港市",
    '157':"淮安市",
    '158':"扬州市",
    '159':"泰州市",
    '160':"盐城市",
    '161':"徐州市",
    '162':"常州市",
    '163':"南通市",
    '164':"天津市",
    '165':"西安市",
    '166':"兰州市",
    '168':"郑州市",
    '169':"镇江市",
    '172':"宿迁市",
    '173':"铜陵市",
    '174':"黄山市",
    '175':"池州市",
    '176':"宣城市",
    '177':"巢湖市",
    '178':"淮南市",
    '179':"宿州市",
    '181':"六安市",
    '182':"滁州市",
    '183':"淮北市",
    '184':"阜阳市",
    '185':"马鞍山市",
    '186':"安庆市",
    '187':"蚌埠市",
    '188':"芜湖市",
    '189':"合肥市",
    '191':"辽源市",
    '194':"松原市",
    '195':"云浮市",
    '196':"佛山市",
    '197':"湛江市",
    '198':"江门市",
    '199':"惠州市",
    '200':"珠海市",
    '201':"韶关市",
    '202':"阳江市",
    '203':"茂名市",
    '204':"潮州市",
    '205':"揭阳市",
    '207':"中山市",
    '208':"清远市",
    '209':"肇庆市",
    '210':"河源市",
    '211':"梅州市",
    '212':"汕头市",
    '213':"汕尾市",
    '215':"鞍山市",
    '216':"朝阳市",
    '217':"锦州市",
    '218':"铁岭市",
    '219':"丹东市",
    '220':"本溪市",
    '221':"营口市",
    '222':"抚顺市",
    '223':"阜新市",
    '224':"辽阳市",
    '225':"葫芦岛市",
    '226':"张家界市",
    '227':"大同市",
    '228':"长治市",
    '229':"忻州市",
    '230':"晋中市",
    '231':"太原市",
    '232':"临汾市",
    '233':"运城市",
    '234':"晋城市",
    '235':"朔州市",
    '236':"阳泉市",
    '237':"吕梁市",
    '239':"海口市",
    '241':"万宁市",
    '242':"琼海市",
    '243':"三亚市",
    '244':"儋州市",
    '246':"新余市",
    '253':"南平市",
    '256':"宜春市",
    '259':"保定市",
    '261':"唐山市",
    '262':"南阳市",
    '263':"新乡市",
    '264':"开封市",
    '265':"焦作市",
    '266':"平顶山市",
    '268':"许昌市",
    '269':"永州市",
    '270':"吉林市",
    '271':"铜川市",
    '272':"安康市",
    '273':"宝鸡市",
    '274':"商洛市",
    '275':"渭南市",
    '276':"汉中市",
    '277':"咸阳市",
    '278':"榆林市",
    '280':"石河子市",
    '281':"庆阳市",
    '282':"定西市",
    '283':"武威市",
    '284':"酒泉市",
    '285':"张掖市",
    '286':"嘉峪关市",
    '287':"台州市",
    '288':"衢州市",
    '289':"宁波市",
    '291':"眉山市",
    '292':"邯郸市",
    '293':"邢台市",
    '295':"伊春市",
    '297':"大兴安岭地区",
    '300':"黑河市",
    '301':"鹤岗市",
    '302':"七台河市",
    '303':"绍兴市",
    '304':"嘉兴市",
    '305':"湖州市",
    '306':"舟山市",
    '307':"平凉市",
    '308':"天水市",
    '309':"白银市",
    '310':"吐鲁番市",
    '311':"昌吉回族自治州",
    '312':"哈密市",
    '315':"阿克苏地区",
    '317':"克拉玛依市",
    '318':"博尔塔拉蒙古自治州",
    '319':"齐齐哈尔市",
    '320':"佳木斯市",
    '322':"牡丹江市",
    '323':"鸡西市",
    '324':"绥化市",
    '331':"乌兰察布市",
    '333':"兴安盟",
    '334':"大理白族自治州",
    '335':"昭通市",
    '337':"红河哈尼族彝族自治州",
    '339':"曲靖市",
    '342':"丽江市",
    '343':"金昌市",
    '344':"陇南市",
    '346':"临夏回族自治州",
    '350':"临沧市",
    '352':"济宁市",
    '353':"泰安市",
    '356':"莱芜市",
    '359':"双鸭山市",
    '366':"日照市",
    '370':"安阳市",
    '371':"驻马店市",
    '373':"信阳市",
    '374':"鹤壁市",
    '375':"周口市",
    '376':"商丘市",
    '378':"洛阳市",
    '379':"漯河市",
    '380':"濮阳市",
    '381':"三门峡市",
    '383':"阿勒泰地区",
    '384':"喀什地区",
    '386':"和田地区",
    '391':"亳州市",
    '395':"吴忠市",
    '396':"固原市",
    '401':"延安市",
    '405':"邵阳市",
    '407':"通化市",
    '408':"白山市",
    '410':"白城市",
    '417':"甘孜藏族自治州",
    '422':"铜仁市",
    '424':"安顺市",
    '426':"毕节市",
    '437':"文山壮族苗族自治州",
    '438':"保山市",
    '456':"东方市",
    '457':"阿坝藏族姜族自治州",
    '466':"拉萨市",
    '467':"乌鲁木齐市",
    '472':"石嘴山市",
    '479':"凉山彝族自治州",
    '480':"中卫市",
    '499':"巴音郭楞蒙古自治州",
    '506':"来宾市",
    '514':"北京市",
    '516':"日喀则市",
    '520':"伊犁市",
    '525':"延边朝鲜族自治州",
    '563':"塔城地区",
    '582':"五指山市",
    '588':"黔西南布依族苗族自治州",
    '608':"海西蒙古族藏族自治州",
    '652':"海东市",
    '653':"克孜勒苏柯尔克孜自治州",
    '654':"天门仙桃市",
    '655':"那曲地区",
    '656':"林芝市",
    '657':"None市",
    '658':"防城市",
    '659':"玉树藏族自治州",
    '660':"伊犁哈萨克自治州",
    '661':"五家渠市",
    '662':"思茅市",
    '663':"香港市",
    '664':"澳门市",
    '665':"崇左市",
    '666':"普洱市",
    '667':"济源市",
    '668':"西双版纳傣族自治州",
    '669':"德宏傣族景颇族自治州",
    '670':"文昌市",
    '671':"怒江傈僳族自治州",
    '672':"迪庆藏族自治州",
    '673':"甘南藏族自治州",
    '674':"陵水黎族自治县市",
    '675':"澄迈县市",
    '676':"海南藏族自治州",
    '677':"山南市",
    '678':"昌都市",
    '679':"乐东黎族自治县市",
    '680':"临高县市",
    '681':"定安县市",
    '682':"海北藏族自治州",
    '683':"昌江黎族自治县市",
    '684':"屯昌县市",
    '685':"黄南藏族自治州",
    '686':"保亭黎族苗族自治县市",
    '687':"神农架林区",
    '688':"果洛藏族自治州",
    '689':"白沙黎族自治县市",
    '690':"琼中黎族苗族自治县市",
    '691':"阿里地区",
    '692':"阿拉尔市",
    '693':"图木舒克市",
}

provincecode2name_dict = {
    '901':"山东省",
    '902':"贵州省",
    '903':"江西省",
    '904':"重庆市",
    '905':"内蒙古自治区",
    '906':"湖北省",
    '907':"辽宁省",
    '908':"湖南省",
    '909':"福建省",
    '910':"上海市",
    '911':"北京市",
    '912':"广西壮族自治区",
    '913':"广东省",
    '914':"四川省",
    '915':"云南省",
    '916':"江苏省",
    '917':"浙江省",
    '918':"青海省",
    '919':"宁夏回族自治区",
    '920':"河北省",
    '921':"黑龙江省",
    '922':"吉林省",
    '923':"天津市",
    '924':"陕西省",
    '925':"甘肃省",
    '926':"新疆维吾尔自治区",
    '927':"河南省",
    '928':"安徽省",
    '929':"山西省",
    '930':"海南省",
    '931':"台湾省",
    '932':"西藏自治区",
    '933':"香港特别行政区",
    '934':"澳门特别行政区",
}

def decrypt(e,t):
    n = []
    for x in t:
        n.append(x)
    a = {}
    r = []
    o = 0
    while o < len(n) / 2:
        a[n[o]] = n[int(len(n) / 2) + o]
        o += 1
    s = 0
    r = []
    while s < len(e):
        r.append(a[e[s]])
        s += 1
    rst = (''.join(r)).split(',')
    return rst

def getJsonByUrl(url):
    time.sleep(3)
    try:
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
            "content-type": "application/json;charset=UTF-8",
            "cache-control": "max-age=0",
            "cookie": 'ab_jid=dc792464332f184b8ad588b1dfa8c6c2272f; ab_jid_BFESS=dc792464332f184b8ad588b1dfa8c6c2272f; __bid_n=187bd41241a7392cef4207; FPTOKEN=wkogThTRttSgx/1gOK0hY+5q7eunGmpJbqZmiQn1pbUCSL7OgHWMq+w2km1B9y4hYf+fwLNTZn9y8YrbUcUKUeJ7UExXjSMQCwGZbyEsWZ2NHPAHseOewLlfEFUT17WSTDIhNV+NPlJBmxmJ4MAon5nNiKdd6w5/xNIs7Bme9bUUv6OAE5hAOZ79/1QY81aqKNko6mN6GRDVyUVsc/0kQc9MlYBaeNg3Nz1WmYv7EoGxldPSo1VkgzkAEORJhPAVHS1ovb/gF6b4uUw3TasMgJ4JJy+BZzbiyDX9/HHNeQ47biAkAQ3/kz8nMZ4v9BBudJTMrIRxRHAchZAf/uDN382BJ1JO6U4h+syc/7OwLB2oHarWpiT69ZctyC4T2jUSmt5ZIfDasKn47U09Fjoz7A==|oU++VOIeIoXT/3YyunlczSS/UOOUUdnP2i4dL738Ujs=|10|4c0948403df8518ead64c86e453b3975; BIDUPSID=E7A997B266E9F80F20A1A0B7902F8184; PSTM=1686643423; BAIDU_WISE_UID=wapp_1687092926856_108; ZFY=w8Tq8WB6:BrQJ5CLgReoQvgwma:BYtr7AdQyFCPPOAJak:C; MCITY=-289%3A; BAIDUID=78589B7E565B83727BC5DD9DB0177A4C:FG=1; BAIDUID_BFESS=78589B7E565B83727BC5DD9DB0177A4C:FG=1; BDUSS=tvcHdUWEVoS3VnYjRwWEVzSHJGNm1wdXdKWC1CNllIazcyQVd0eFJzVHYyYTFsRUFBQUFBJCQAAAAAAAAAAAEAAAB29ALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO9MhmXvTIZlV0; bdindexid=63hseel6v9mhbq73482j1jb9h1; SIGNIN_UC=70a2711cf1d3d9b1a82d2f87d633bd8a045331501553fRUxfRbXOgW%2BtHHbaFD%2BNoUMaBmcaWj2LISwG7HxZTsCREBcrTns0ip9dca0F7GY4MLqc8H1TB00avFYu8ru6iY9Wv0Eg42nXcEAcKf48IZQ0ZvnlI0wqfZOo911VvFX9hTURyRtue5wpCtCxy7iD7CgaNudhWmKTMxOrfjMyLjuhvxRxYQGyyF7yjEsg5ajpqKMCSslYzsZVNRitRa0bqvv0liyvLARlYSeVLg%2FDkYGE1KJ4D2TDOuI8QEvG9Okyxac4oGHt%2BubBOGce%2BQITe%2Fy2B3ePdFn7n8uk7J3q4%3D29254445503994742452686099277797; BDUSS_BFESS=tvcHdUWEVoS3VnYjRwWEVzSHJGNm1wdXdKWC1CNllIazcyQVd0eFJzVHYyYTFsRUFBQUFBJCQAAAAAAAAAAAEAAAB29ALTAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAO9MhmXvTIZlV0; ab_bid=bb05b8e20fd8f6f257603bd883c3928e77aa; ab_sr=1.0.1_ZTVjMWE0ZjI3ZTNmZDYxM2M1Y2RmMDA2YjI2ZWQ3YmNhZmNhYzI0MzZiZmIxZTEwNjgxZWFkYzRlMTc3MDcxY2EyZDJiNzc0ZGIxMzU3Mzg1Njg0ZDdiYmE1MDViOGZiZGQ5MDc5NmQ0MDFkMjgwMDYyZDMyYWMyM2I5ZDNhZTFiZWY1ZWM5ZThhMWMyYjEwZTViMWU5ZjdiZDQyOGZjMg==; RT="z=1&dm=baidu.com&si=17cf5258-cbd2-4802-b6d4-cbc0edc185ac&ss=lqhh1j6n&sl=u&tt=xs6&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=4wd9n"',
            "upgrade-insecure-requests": "1",
            "Cipher-Text": "1655708473479_1655718409632_pTD8uXff9pQBNaZQyKDT7OnT7n5bex7JgdVlRI9K6ivOXbDuKBDpxpgudDBAaCCBNYjJ03+R4il8dxhj949vJGemDwnUjEo+ASWHUy2w/AR0fT4DfdE+fO+s4MjbprW/FAxBRIfFqKg9O0mqjbceigyPILYAp3ca8zLHYvdG9NVpTze/5p9DgIB/FK6vtG+FMKA+o1V0D7aXhY+EEzy9LRKGE5Sq6mjoxCaAiwtF4mzPLwGjQF87/s2NVso1JpxIvLtLgnDbsUQs2uzCMEdZ4jZaflVb5bh4QXt7qQllMNaQF3iQssMkCrETBZk4sXQYQZpRg1kiVBKzJ9PAzwvBiPsHmnCpgaoE2RWAVcgIt5Neccuw/+V9qRs1EaPlPI1Qgt/ENyrVC1j8YtnhQUC56DJNEJPVC0+SJBqM/dRFuLA19WDZNsGlXwM62MLMVOLb",
            "Host": "index.baidu.com",
            "Referer": "https://index.baidu.com/v2/main/index.html",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0"
        }
        r = requests.get(url, headers = headers , timeout = 5)
        return json.loads(r.text)
    except Exception as e:
        print('time out : ' + url)
        return getJsonByUrl(url)

def getOneKeywordSearchIndex(keyword, start_year, end_year, all_platform):

    #城市级
    for c in citycode2name_dict.keys():
        getOneKeywordSearchIndexOneArea(keyword, c, c, citycode2name_dict[c], start_year,end_year,all_platform)

def getOneKeywordSearchIndexOneArea(keyword, area, city, province,start_year,end_year,all_platform):
    sql_data_list = []
    last_t = ''
    last_uniqid = ''
    for i in range(max(start_year,2022),end_year + 1):
        url = "https://index.baidu.com/api/SearchApi/index?area=" + area + "&word=[[%7B%22name%22:%22" + keyword + "%22,%22wordType%22:1%7D]]" + "&startDate=%d-01-01&endDate=%d-12-31" % (i,i)
        print('%s - %s - %s - %d start(ALL).' %(keyword, province, city, i))
        print(url)
        index_json = getJsonByUrl(url)
        try:
            uniqid = index_json['data']['uniqid']
        except Exception as e:
            print(str(index_json))
        if last_t == '' or last_uniqid != uniqid:
            t = getJsonByUrl("https://index.baidu.com/Interface/ptbk?uniqid=%s" % uniqid)
            last_uniqid = uniqid
            last_t = t
        else:
            t = last_t
        all_rst = decrypt(index_json['data']['userIndexes'][0]['all']['data'], t['data'])
        pc_rst = decrypt(index_json['data']['userIndexes'][0]['pc']['data'], t['data'])
        wise_rst = decrypt(index_json['data']['userIndexes'][0]['wise']['data'], t['data'])

        start_date = '%d-01-01' % i
        for i in range(0,len(all_rst)):
            if all_rst[i] == '':continue
            current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=i)
            current_date_str = current_date.strftime('%Y-%m-%d')
            sql_data_list.append((keyword, current_date_str, '综合', city, province, all_rst[i]))
        if all_platform is False:
            continue
        for i in range(0,len(pc_rst)):
            if pc_rst[i] == '':continue
            current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=i)
            current_date_str = current_date.strftime('%Y-%m-%d')
            sql_data_list.append((keyword, current_date_str, 'PC端', city, province, pc_rst[i]))
        for i in range(0,len(wise_rst)):
            if wise_rst[i] == '':continue
            current_date = datetime.datetime.strptime(start_date, "%Y-%m-%d") + datetime.timedelta(days=i)
            current_date_str = current_date.strftime('%Y-%m-%d')
            sql_data_list.append((keyword, current_date_str, '移动端', city, province, wise_rst[i]))

    for sql_data in sql_data_list:
        print(sql_data)
    df = pd.DataFrame(sql_data_list, columns=["关键词", "时间", "端口", "4", "位置", "指数"])
    df.to_excel(f"./perday{province}.xlsx", index=False)

if __name__ == "__main__":
    getOneKeywordSearchIndex('非物质文化遗产', 2022, 2022, True)









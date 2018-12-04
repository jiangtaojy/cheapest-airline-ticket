import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import json
import time


def airchina():
    head = {'Accept': '*/*',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Connection': 'keep-alive',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'JSESSIONID=AB19E21A02F15D7395972BD9B32BD09E; current_PoS=AIRCHINA_CN; currentLang=zh_CN; _gcl_au=1.1.78957716.1542775969; BIGipServerWeb_http=1292508844.20480.0000; locationName0=%u5E7F%u5DDE%u767D%u4E91%u673A%u573A; locationCode0=CAN; countryCode0=CN; locationName1=%u5317%u4EAC%u9996%u90FD%u56FD%u9645%u673A%u573A; locationCode1=PEK; countryCode1=CN; locationName2=%u4E2D%u6587/%u82F1%u6587/%u62FC%u97F3; locationCode2=; countryCode2=; locationName3=%u4E2D%u6587/%u82F1%u6587/%u62FC%u97F3; locationCode3=; countryCode3=; flightType=oneWay; deptDateShowGo=2019-01-20; deptDateShowBack=2019-01-22; _Jo0OQK=294FAAAA59626311280E37F96A3925116B6F6C5932D3210F35FD9AAB363B8ACDB73BD26EBCE0F0051E4C727C86877711D91B4B6DE17EFC20269337E66A2D8743FC9DAE7347217C5D15F471E060E1072BC0F2344F5383CCD31FFB4B6DE17EFC2026936259345EBA3EBEA276E64A59DFA244EGJ1Z1JQ==; Hm_lvt_c3e8634de774fd5ce040e37109942dc7=1542766297,1543480757,1543818803,1543837683; Hm_lpvt_c3e8634de774fd5ce040e37109942dc7=1543837683; _pzfxuvpc=1542766240015%7C1244794164283685917%7C46%7C1543839938328%7C10%7C5983490540770241784%7C9671876833113379924; _pzfxsvpc=9671876833113379924%7C1543837661060%7C14%7Chttps%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fD7UwC0CEGX0rGgAsjg7sNT00000ZCRqNb00000v9rwjW.THv4SoJq0A3qmh7GuZNCUvd-gLKM0ZnquhN9P1b4uynsnj0smWKbufKd5RuDwHwKnWn3rDfznRRdf1uDPW01nDRdnYn3Pju7PYfY0ADqI1YhUyPGujY1nHRYrjf4n10LFMKzUvwGujYkP6K-5y9YIZ0lQzqLILT8my-zmv9GUhD8mvqVQhP8Q1qWpyfqf-cVTA-8Xh9dmy3lnW0krjDsn1DlRYNPrbF9pywdfWGjiD3lnj0snjD0mLFW5HR4PWnL%26tpl%3Dtpl_11533_18472_14460%26l%3D1509233786%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E4%2525B8%2525AD%2525E5%25259B%2525BD%2525E5%25259B%2525BD%2525E8%252588%2525AA(Air%252520China)%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%2526xp%253Did(%252522m3154849307_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D161%26wd%3D%25E5%259B%25BD%25E8%2588%25AA%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1074; s_pers=%20s_fid%3D5FB7078DCCA994E1-2296BE535BFCB825%7C1701606346513%3B; s_sess=%20s_sq%3D%3B%20s_cc%3Dtrue%3B; mbox=session#1543837660818-848682#1543841812|check#true#1543840012',
            'Origin': 'http://et.airchina.com.cn',
            'Referer': 'http://et.airchina.com.cn/InternetBooking/AirOneWayCombinableCalendarForwardAction.do',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36}'
            }
    req = requests.get("http://et.airchina.com.cn/InternetBooking/AirOneWayCombinableCalendarForwardAction.do",
                       headers=head)
    html = req.text
    soup = BeautifulSoup(html, features='lxml')
    data = soup.find_all('td', {"class": "available"})
    min_price = 10000
    min_date = ""
    for m in data[7:13]:
        tmp_date = m['id']
        price = m.find("div", {"class": "colPrice"})
        tmp_price = int(price.get_text().strip().replace(',', ''))
        if tmp_price < min_price:
            min_price = tmp_price
            min_date = tmp_date[4:]

    head_shenzhen = {'Accept': '*/*',
                     'Accept-Encoding': 'gzip, deflate',
                     'Accept-Language': 'zh-CN,zh;q=0.9',
                     'Connection': 'keep-alive',
                     'Content-Type': 'application/x-www-form-urlencoded',
                     'Cookie': 'JSESSIONID=AB19E21A02F15D7395972BD9B32BD09E; current_PoS=AIRCHINA_CN; currentLang=zh_CN; _gcl_au=1.1.78957716.1542775969; BIGipServerWeb_http=1292508844.20480.0000; locationName0=%u5E7F%u5DDE%u767D%u4E91%u673A%u573A; locationCode0=CAN; countryCode0=CN; locationName1=%u5317%u4EAC%u9996%u90FD%u56FD%u9645%u673A%u573A; locationCode1=PEK; countryCode1=CN; locationName2=%u4E2D%u6587/%u82F1%u6587/%u62FC%u97F3; locationCode2=; countryCode2=; locationName3=%u4E2D%u6587/%u82F1%u6587/%u62FC%u97F3; locationCode3=; countryCode3=; flightType=oneWay; deptDateShowGo=2019-01-20; deptDateShowBack=2019-01-22; _Jo0OQK=294FAAAA59626311280E37F96A3925116B6F6C5932D3210F35FD9AAB363B8ACDB73BD26EBCE0F0051E4C727C86877711D91B4B6DE17EFC20269337E66A2D8743FC9DAE7347217C5D15F471E060E1072BC0F2344F5383CCD31FFB4B6DE17EFC2026936259345EBA3EBEA276E64A59DFA244EGJ1Z1JQ==; Hm_lvt_c3e8634de774fd5ce040e37109942dc7=1542766297,1543480757,1543818803,1543837683; Hm_lpvt_c3e8634de774fd5ce040e37109942dc7=1543837683; _pzfxuvpc=1542766240015%7C1244794164283685917%7C44%7C1543839863164%7C10%7C5983490540770241784%7C9671876833113379924; _pzfxsvpc=9671876833113379924%7C1543837661060%7C12%7Chttps%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fD7UwC0CEGX0rGgAsjg7sNT00000ZCRqNb00000v9rwjW.THv4SoJq0A3qmh7GuZNCUvd-gLKM0ZnquhN9P1b4uynsnj0smWKbufKd5RuDwHwKnWn3rDfznRRdf1uDPW01nDRdnYn3Pju7PYfY0ADqI1YhUyPGujY1nHRYrjf4n10LFMKzUvwGujYkP6K-5y9YIZ0lQzqLILT8my-zmv9GUhD8mvqVQhP8Q1qWpyfqf-cVTA-8Xh9dmy3lnW0krjDsn1DlRYNPrbF9pywdfWGjiD3lnj0snjD0mLFW5HR4PWnL%26tpl%3Dtpl_11533_18472_14460%26l%3D1509233786%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E4%2525B8%2525AD%2525E5%25259B%2525BD%2525E5%25259B%2525BD%2525E8%252588%2525AA(Air%252520China)%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%2526xp%253Did(%252522m3154849307_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D161%26wd%3D%25E5%259B%25BD%25E8%2588%25AA%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1074; s_pers=%20s_fid%3D5FB7078DCCA994E1-2296BE535BFCB825%7C1701606272804%3B; s_sess=%20s_sq%3D%3B%20s_cc%3Dtrue%3B; mbox=session#1543837660818-848682#1543841736|check#true#1543839936',
                     'Origin': 'http://et.airchina.com.cn',
                     'Referer': 'http://et.airchina.com.cn/InternetBooking/AirOneWayCombinableCalendarForwardAction.do',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36}'
                     }
    req1 = requests.get("http://et.airchina.com.cn/InternetBooking/AirOneWayCombinableCalendarForwardAction.do",
                        headers=head_shenzhen)
    html1 = req1.text
    soup1 = BeautifulSoup(html1, features='lxml')
    data1 = soup1.find_all('td', {"class": "available"})
    min_price1 = 10000
    min_date1 = ""
    for m in data1[7:13]:
        tmp_date = m['id']
        price = m.find("div", {"class": "colPrice"})
        tmp_price = int(price.get_text().strip().replace(',', ''))
        if tmp_price < min_price1:
            min_price1 = tmp_price
            min_date1 = tmp_date[4:]
    if min_price < min_price1:
        return min_price, min_date, "airchina", "guangzhou"
    else:
        return min_price1, min_date1, "airchina", "shenzhen"


def southern_airchina():  # 不需要更新cookie，时间已定
    head = {'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Content-Length': '70',
            'Content-Type': 'application/json',
            'Cookie': 'JSESSIONID=82F73DFB3151306F6EC1933ED591E8DA; likev_user_id=d773a4b6-2da4-473f-d81a-ed9e29b1843a; sid=2861ba7895354329a28e813e15d0b08e; language=zh_CN; zsluserCookie=true; JSESSIONID=C2FFA010C7C8A9A75ECD6D9F7BCCD69D; last_session_stm_8mrmut7r76ntg21b=1543817593298; likev_session_id_8mrmut7r76ntg21b=41af2c2d-278b-4f40-a400-e61aa07e779e; last_session_id_8mrmut7r76ntg21b=41af2c2d-278b-4f40-a400-e61aa07e779e; temp_zh=cou%3D0%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2019-01-20%3B%E5%B9%BF%E5%B7%9E-%E5%8C%97%E4%BA%AC%3B1%2C0%2C0%3B%26; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(CAN)%3AWT.al_dstcity1(PEK)%3AWT.al_orgdate1(2019-01-20); _gcl_au=1.1.1228579889.1543817605; WT-FPC=id=218.19.145.14-367520240.30703935:lv=1543820076254:ss=1543817592897:fs=1542766117912:pn=4:vn=2; likev_session_etm_8mrmut7r76ntg21b=1543820173674',
            'Host': 'b2c.csair.com',
            'Origin': 'http://b2c.csair.com',
            'Proxy-Connection': 'keep-alive',
            'Referer': 'http://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=CAN&c2=PEK&d1=2019-01-20&at=1&ct=0&it=0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
            }
    data = json.dumps({'depCity': "CAN", 'arrCity': "PEK", 'month': "2019-01", 'channel': "B2CPC1"})
    req = requests.post("http://b2c.csair.com/portal/minPrice/queryMinPriceInMonth",
                        headers=head, data=data)
    month = json.loads(req.text)
    data = month['data']
    min_price = 10000
    min_date = ""
    for m in data[19:25]:
        tmp_price = m['price']
        if tmp_price < min_price:
            min_price = tmp_price
            min_date = m['date']

    head_shenzhen = {'Accept': 'application/json, text/javascript, */*; q=0.01',
                     'Accept-Encoding': 'gzip, deflate',
                     'Accept-Language': 'zh-CN,zh;q=0.9',
                     'Content-Length': '70',
                     'Content-Type': 'application/json',
                     'Cookie': 'JSESSIONID=82F73DFB3151306F6EC1933ED591E8DA; likev_user_id=d773a4b6-2da4-473f-d81a-ed9e29b1843a; sid=2861ba7895354329a28e813e15d0b08e; language=zh_CN; zsluserCookie=true; JSESSIONID=C2FFA010C7C8A9A75ECD6D9F7BCCD69D; last_session_stm_8mrmut7r76ntg21b=1543817593298; likev_session_id_8mrmut7r76ntg21b=41af2c2d-278b-4f40-a400-e61aa07e779e; last_session_id_8mrmut7r76ntg21b=41af2c2d-278b-4f40-a400-e61aa07e779e; temp_zh=cou%3D0%3Bsegt%3D%E5%8D%95%E7%A8%8B%3Btime%3D2019-01-20%3B%E5%B9%BF%E5%B7%9E-%E5%8C%97%E4%BA%AC%3B1%2C0%2C0%3B%26; WT.al_flight=WT.al_hctype(S)%3AWT.al_adultnum(1)%3AWT.al_childnum(0)%3AWT.al_infantnum(0)%3AWT.al_orgcity1(CAN)%3AWT.al_dstcity1(PEK)%3AWT.al_orgdate1(2019-01-20); _gcl_au=1.1.1228579889.1543817605; WT-FPC=id=218.19.145.14-367520240.30703935:lv=1543820076254:ss=1543817592897:fs=1542766117912:pn=4:vn=2; likev_session_etm_8mrmut7r76ntg21b=1543820173674',
                     'Host': 'b2c.csair.com',
                     'Origin': 'http://b2c.csair.com',
                     'Proxy-Connection': 'keep-alive',
                     'Referer': 'http://b2c.csair.com/B2C40/newTrips/static/main/page/booking/index.html?t=S&c1=SZX&c2=PEK&d1=2019-01-20&at=1&ct=0&it=0',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
                     'X-Requested-With': 'XMLHttpRequest',
                     }
    data_shenzhen = json.dumps({'depCity': "SZX", 'arrCity': "PEK", 'month': "2019-01", 'channel': "B2CPC1"})
    req = requests.post("http://b2c.csair.com/portal/minPrice/queryMinPriceInMonth",
                        headers=head_shenzhen, data=data_shenzhen)
    month1 = json.loads(req.text)
    data1 = month1['data']
    min_price1 = 10000
    min_date1 = ""
    for m in data1[19:25]:
        tmp_price = m['price']
        if tmp_price < min_price1:
            min_price1 = tmp_price
            min_date1 = m['date']
    if min_price < min_price1:
        return min_price, min_date, "southern_airchina", "guangzhou"
    else:
        return min_price1, min_date1, "southern_airchina", "shenzhen"


def xiamen_air():  # 时间已定，不需要更新cookie
    head = {
        'Host': 'et.xiamenair.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Referer': 'https://et.xiamenair.com/xiamenair/book/findFlights.action?tripType=0&queryFlightInfo=CAN,PEK,2019-01-10&cabinClass=1&psgrInfo=0,1;1,0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=Pw4S+PlhyD+stfG9I8EjISDd.mfb2cServer1; Webtrends=123.103.125.44.1543826293603226; Hm_lvt_a0f83bbc1d09b6e5a33928301f402485=1543826312; _gcl_au=1.1.1474798873.1543826314; _ga=GA1.3.1357111498.1543826314; _gid=GA1.3.2129352422.1543826314; X-LB=2.5.6.9078738d.50; Hm_lpvt_a0f83bbc1d09b6e5a33928301f402485=1543826390; _dc_gtm_UA-96517318-3=1; WT_FPC=id=2fd6f221ac180ab65371543826311557:lv=1543826401364:ss=1543826311557'
    }
    req = requests.get(
        "https://et.xiamenair.com/xiamenair/common/lpCalendar.json?org=CAN&dst=PEK&beginDate=2019-01-10&tripType=0&channelId=1",
        headers=head)
    month = json.loads(req.text)
    data = month['lpDataList']
    min_price = 10000
    min_date = ""
    for m in data[9:15]:
        if m['price'] != '--':
            tmp_price = int(m['price'])
            if tmp_price < min_price:
                min_price = tmp_price
                min_date = m['cDate']

    head_shenzhen = {
        'Host': 'et.xiamenair.com',
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Referer': 'https://et.xiamenair.com/xiamenair/book/findFlights.action?tripType=0&queryFlightInfo=SZX,PEK,2019-01-20&cabinClass=1&psgrInfo=0,1;1,0',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'JSESSIONID=Si+iL+3tDluArlt7fp-u8HGt.mfb2cServer1; Webtrends=123.103.125.44.1543826293603226; _gcl_au=1.1.1474798873.1543826314; _ga=GA1.3.1357111498.1543826314; _gid=GA1.3.2129352422.1543826314; Hm_lvt_a0f83bbc1d09b6e5a33928301f402485=1543826312,1543835450,1543835462,1543835752; X-LB=2.4.5.66a2a7ae.50; Hm_lpvt_a0f83bbc1d09b6e5a33928301f402485=1543836033; _dc_gtm_UA-96517318-3=1; WT_FPC=id=2fd6f221ac180ab65371543826311557:lv=1543836034819:ss=1543835449030'
    }
    req1 = requests.get(
        "https://et.xiamenair.com/xiamenair/common/lpCalendar.json?org=SZX&dst=PEK&beginDate=2019-01-10&tripType=0&channelId=1",
        headers=head_shenzhen)
    month1 = json.loads(req1.text)
    data1 = month1['lpDataList']
    min_price1 = 10000
    min_date1 = ""
    for m in data1[9:15]:
        if m['price'] != '--':
            tmp_price = int(m['price'])
            if tmp_price < min_price1:
                min_price1 = tmp_price
                min_date1 = m['cDate']
    if min_price < min_price1:
        return min_price, min_date, "xiamen_air", "guangzhou"
    else:
        return min_price1, min_date1, "xiamen_air", "shenzhen"


def hainan_air():  # 需要更新cookie,时间有问题
    head = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'zip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'Cache-Control': 'max-age=0',
            'Connection': 'keep-alive',
            'Cookie': 'JSESSIONID=3E3E5229083E583EA39463177D7E5959.HUIBEServer10; gdpr_state=open; _ga=GA1.2.1589105882.1543827123; _gid=GA1.2.1131784149.1543827123; Webtrends=218.19.145.14.1543827122976214; X-LB=2.5a7.5a8.4a22ab70.50; declarehugdpr=agreeusecookie',
            'Host': 'new.hnair.com',
            'Referer': 'https://new.hnair.com/hainanair/ibe/air/searchResults.do',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
            }
    req = requests.get(
        "https://new.hnair.com/hainanair/ibe/air/searchResults.do", headers=head)
    html = req.text
    soup = BeautifulSoup(html, features='lxml')
    data = soup.find_all('p', {"class": "ca-price-p"})
    min_price = 10000
    min_date = ""
    for m in data:
        tmp_date = m.find("input", {"class": "radio"})['value']
        price = m.find("span", {"class": "ca-price"})
        tmp_price = int(price.get_text().replace('￥', ''))
        if tmp_price < min_price:
            min_price = tmp_price
            min_date = tmp_date

    head_shenzhen = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                     'Accept-Encoding': 'zip, deflate, br',
                     'Accept-Language': 'zh-CN,zh;q=0.9',
                     'Cache-Control': 'max-age=0',
                     'Connection': 'keep-alive',
                     'Cookie': 'JSESSIONID=056F438A9E83F9F66486C55CF1C42206.HUIBEServer10; gdpr_state=open; _ga=GA1.2.1589105882.1543827123; _gid=GA1.2.1131784149.1543827123; Webtrends=218.19.145.14.1543827122976214; X-LB=2.5a7.5a8.4a22ab70.50; declarehugdpr=agreeusecookie; _gat_TrueMetrics=1; _gat=1',
                     'Host': 'new.hnair.com',
                     'Referer': 'https://new.hnair.com/hainanair/ibe/air/searchResults.do',
                     'Upgrade-Insecure-Requests': '1',
                     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
                     }
    req1 = requests.get(
        "https://new.hnair.com/hainanair/ibe/air/searchResults.do", headers=head_shenzhen)
    html1 = req1.text
    soup1 = BeautifulSoup(html1, features='lxml')
    data1 = soup1.find_all('p', {"class": "ca-price-p"})
    min_price1 = 10000
    min_date1 = ""
    for m in data1:
        tmp_date = m.find("input", {"class": "radio"})['value']
        price = m.find("span", {"class": "ca-price"})
        tmp_price = int(price.get_text().replace('￥', ''))
        if tmp_price < min_price1:
            min_price1 = tmp_price
            min_date1 = tmp_date
    if min_price < min_price1:
        return min_price, min_date, "hainanair", "guangzhou"
    else:
        return min_price1, min_date1, "hainanair", "shenzhen"


def eastern_airchina():  # 似乎不需要更新cookie，时间已定
    head = {
        'Host': 'www.ceair.com',
        'Proxy-Connection': 'keep-alive',
        'Content-Length': '195',
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Origin': 'http://www.ceair.com',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Referer': 'http://www.ceair.com/booking/can-pek-190120_CNY.html',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'Webtrends=2c337834.57c197702dbc7; language=zh_CN; _ga=GA1.2.36082000.1543823697; _gid=GA1.2.1789303987.1543823697; JSESSIONID=eBq05XQifI8hBH0gBpnbUhho.laputaServer3; ecrmWebtrends=218.19.145.14.1543823698055; _gat=1; _gat_UA-80008755-11=1; _pzfxuvpc=1543823697790%7C2489452855152166793%7C7%7C1543824317554%7C1%7C%7C1369108221597501779; _pzfxsvpc=1369108221597501779%7C1543823697790%7C7%7Chttps%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DXTbi0g80N9q26bUzYPjmcA4_LNIa5YxHk4Lw8el6awi%26wd%3D%26eqid%3Db3bff05b00000b2a000000065c04e14c'
    }

    data_guangzhou = {'cond.monthOffSet': '0',
                      'cond.depCode': 'CAN',
                      'cond.arrCode': 'PEK',
                      'cond.depCityCode': 'CAN',
                      'cond.arrCityCode': 'BJS',
                      'cond.deptAirport': '',
                      'cond.arrAirport': '',
                      'cond.trip': 'OW',
                      'cond.goDt': '',
                      'cond.depDate': '2019-01-20',
                      'cond.currency': 'CNY'}
    data_shenzhen = {'cond.monthOffSet': '0',
                     'cond.depCode': 'SZK',
                     'cond.arrCode': 'PEK',
                     'cond.depCityCode': 'SZK',
                     'cond.arrCityCode': 'BJS',
                     'cond.deptAirport': '',
                     'cond.arrAirport': '',
                     'cond.trip': 'OW',
                     'cond.goDt': '',
                     'cond.depDate': '2019-01-20',
                     'cond.currency': 'CNY'}
    req = requests.post("http://www.ceair.com/booking/new-low-price-calendar!getDynDayLowPriceEc.shtml",
                        headers=head, data=data_guangzhou)
    month = json.loads(req.text)
    data = month['currentList']
    min_price = 10000
    min_date = ""
    for m in data[15:21]:
        tmp_price = int(float(m['p']))
        if tmp_price < min_price and tmp_price != -1:
            min_price = tmp_price
            min_date = m['d']
    req_shenzhen = requests.post("http://www.ceair.com/booking/new-low-price-calendar!getDynDayLowPriceEc.shtml",
                                 headers=head, data=data_shenzhen)
    month1 = json.loads(req_shenzhen.text)
    data1 = month1['currentList']
    min_price1 = 10000
    min_date1 = ""
    for m in data1[15:21]:
        tmp_price = int(float(m['p']))
        if tmp_price < min_price1 and tmp_price != -1:
            min_price1 = tmp_price
            min_date1 = m['d']
    if min_price < min_price1:
        return min_price, min_date, "eastern_airchina", "guangzhou"
    else:
        return min_price1, min_date1, "eastern_airchina", "shenzhen"


total_min_price = 10000
while (True):
    result1 = airchina()
    result2 = southern_airchina()
    result3 = xiamen_air()
    result4 = eastern_airchina()
    results = [result1, result2, result3, result4]
    price = [result1[0], result2[0], result3[0], result4[0]]
    index = price.index(min(price))
    result = results[index]
    print(result1, result2, result3, result4)
    if total_min_price > result[0]:
        total_min_price = result[0]
        # Your Account SID from twilio.com/console
        account_sid = "***********"
        # Your Auth Token from twilio.com/console
        auth_token = "**********"
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            # 这里中国的号码前面需要加86
            to="+*********",
            from_="+*********",
            body="The cheapest price of " + result[1] + " from " + result[3] + " is " + str(
                total_min_price) + " and the airline is " + result[2])
        print(message.sid)
    time.sleep(120)

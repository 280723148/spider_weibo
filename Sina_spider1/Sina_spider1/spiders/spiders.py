# encoding=utf-8
import re
import datetime
from scrapy.spider import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from Sina_spider1.items import InformationItem, TweetsItem, FollowsItem, FansItem


class Spider(CrawlSpider):
    name = "sinaSpider"
    host = "http://weibo.cn"
    '''start_urls = [
        5235640836, 5676304901, 5871897095, 2139359753, 5579672076, 2517436943, 5778999829, 5780802073, 2159807003,
        1756807885, 3378940452, 5762793904, 1885080105, 5778836010, 5722737202, 3105589817, 5882481217, 5831264835,
        2717354573, 3637185102, 1934363217, 5336500817, 1431308884, 5818747476, 5073111647, 5398825573, 2501511785,
    ]    
    start_urls = [
        GNZ48-王盈-, GNZ48-龙亦瑞, GNZ48-农燕萍, GNZ48-杨可璐, GNZ48-刘嘉怡-, GNZ48-王翠菲,
        6034778078, 6034492357, 6034212582, 6034780322, 6033922472, 6034777428, 
        GNZ48-陈桂君, GNZ48-代玲, GNZ48-赵欣雨, GNZ48-王偲越, GNZ48-王秭歆, GNZ48-陈梓荧, 
        6034777701, 6047256977, 6047258201, 6034210438, 6034785630, 6034488423,
        GNZ48-赵翊民, GNZ48-王炯义, GNZ48-杜秋霖, GNZ48-张心雨, GNZ48-于珊珊, GNZ48-杨媛媛, 
        6047257712, 6033924165, 6034495212, 6034787484, 6034779235, 6034493369,

        BEJ48-石羽莎,BEJ48-叶苗苗,BEJ48-王雨煊,BEJ48-葛司琪,BEJ48-房蕾,BEJ48-张韩紫陌,
        6016757708, 6013595409, 6017033285, 6013595120, 6013823016, 6013595603,
        BEJ48-孙语姗,BEJ48-刘闲,BEJ48-任心怡,BEJ48-张怀瑾,BEJ48-黄恩茹,BEJ48-杨晔,
        6013595744, 5617036654, 6013595317, 5617256267, 6013611098, 6013595830,
        BEJ48-陈雅钰,BEJ48-李泓瑶,BEJ48-任玥霖,BEJ48-单习文,BEJ48-许婉玉,
        6017289512, 6013595694, 5617036657, 6017032776, 6019361685,

        BEJ48-陈逸菲,BEJ48-吴月黎,BEJ48-杨一帆,BEJ48-李_娜,
        6013806959, 6013807023, 6013822815, 6013807210,
        GNZ48-李伊虹,GNZ48-戴欣佚,GNZ48-黄黎蓉,GNZ48-向芸,
        6033312477, 6033035492,6033592700, 6033593819,

        SNH48-姚祎纯-,SNH48-祁静,SNH48-徐诗琪,SNH48-曾晓雯,SNH48-袁一琦,
        6022589086, 6019913036, 6020796878, 6019913274, 6021695822, 
        SNH48-刘瀛,SNH48-张雅梦,SNH48-刘菊子,SNH48-江真仪,SNH48-徐真,SNH48-许逸,
        6022570907, 6022563429, 6020769478, 6021669925, 6020242753,6022573703,
        SNH48-吕一,SNH48-潘燕琦,SNH48-赵韩倩,
        6021143413, 6020242374, 6022034041,

        
        六：
        GNZ48-张琼予,GNZ48-周倩玉,GNZ48-罗寒月,GNZ48-胡怡莹, 
        5886585193, 5885155590, 5886586996, 5886587197,

        BEJ48-刘姝贤,BEJ48-林溪荷,BEJ48-胡博文,BEJ48-牛聪聪,BEJ48-青钰雯,BEJ48-孙姗 
        5886797197,5886997271, 5880065713,5886998248 ,5886798137 ,5886798570,
        BEJ48-文妍 ,BEJ48-夏越,BEJ48-张梦慧 ,
        5886998975,5891499998 ,5891710058,

        

        SNH48-李佳恩-, SNH48-吕梦莹, SNH48-张嘉予_,SNH48-林忆宁,SNH48-王金铭- ,SNH48-孙珍妮 ,SNH48-黄彤扬-,SNH48-成珏,
        5863012981, 5861952965,5861113498 ,5861422056,5861422830,5861115930,5863498042,5861419679,
        
        BEJ48-顼凘炀,BEJ48-毕梦媛,BEJ48-陈姣荷,BEJ48-陈倩楠,BEJ48-冯思佳,BEJ48-李诗彦,
        5891500145,5879769942 ,5880065358 , 5880065475,5880065587 ,5880066349,
        BEJ48-李想 ,BEJ48-李媛媛 ,BEJ48-李梓_  ,BEJ48-林堃 ,BEJ48-刘胜男 ,BEJ48-罗雪丽_ ,
        5879771257,5879771383 ,5880066726 ,5879772356 ,5886797095 ,5886797408,
        BEJ48-马玉灵,BEJ48-苏杉杉,BEJ48-易妍倩,BEJ48-张笑盈,BEJ48-郑一凡
        5886797829,5886998602 ,5891709949 ,5891711600 ,5891502165,
        
        GNZ48-左嘉欣,GNZ48-陈欣妤,GNZ48-冯嘉希,GNZ48-刘力菲,GNZ48-熊心瑶,GNZ48-卢静,
        5885722642, 5886364814, 5887712082, 5887863238,5887697862 ,5886364444, 
        GNZ48-郑丹妮-,GNZ48-左婧媛 ,GNZ48-肖文铃 ,GNZ48-陈慧婧 ,GNZ48-孙馨 ,GNZ48-陈楠茜 ,
        5887697249,5885812685 ,5885954688 ,5887698175 ,5887714199 ,5886589255 ,
        GNZ48-唐莉佳,GNZ48-洪静雯 ,GNZ48-冼燊楠 ,GNZ48-刘倩倩-,
        5885940120,5885955392 ,5887054947 ,5885708534 ,

        
        五：
        SNH48-陈韫凌,SNH48-邹佳佳-,SNH48-蒋舒婷-,SNH48-张怡,SNH48-洪珮雲,SNH48-宋雨珊--,
        5681003434, 5786685220, 5681072386, 5690216533, 5686134819, 5786322468,
        SNH48-严佼君-,SNH48-费沁源--,SNH48-陈音,SNH48-潘瑛琪,SNH48-於佳怡-,SNH48-刘增艳
        5786679436, 5680343342, 5680341906, 5691239843, 5786337191, 5681431767,
        SNH48-张文静-,SNH48-姜杉,
        5787012546, 5690264778,

         

        SNH48-沈梦瑶,SNH48-王露皎,SNH48-袁航-,SNH48-周怡-,         
        5681945173, 5682588352, 5691250627, 5693244741,

        BEJ48-陈美君,BEJ48-段艺璇,BEJ48-冯雪莹,BEJ48-胡晓慧 ,BEJ48-宋思娴_ ,田姝丽,
        5681353210, 5681004199,5685088161 ,5691238431 ,5690266096 ,5786991235,
        BEJ48-徐佳丽,BEJ48-熊素君 , 
        5692183212, 5787002847,

        GNZ48-陈珂,GNZ48-陈雨琪-,GNZ48-杜雨微 ,SNH48-高源婧-,GNZ48-李沁洁,GNZ48-林嘉佩,
        5680339910,5681354886 ,5681355162,5685467003 ,5681479865 ,5681828458 ,
        GNZ48-刘梦雅 ,GNZ48-刘筱筱,GNZ48-谢蕾蕾-,GNZ48-阳青颖,GNZ48-曾艾佳,GNZ48-张凯祺,
        5681476803, 5681480311, 5786332015,5786337946 ,5787334703,5787347460 , 


        四：
        BEJ48-闫明筠,
        5490236021, 

        SNH48-汪佳翎,SNH48-汪束--,SNH48-李晶,SNH48-王晓佳,SNH48-陈琳,SNH48-孙歆文,
        5478873704, 5491330253, 5462211905, 5490234918, 5460950220, 5478872932,
        SNH48-李钊-,SNH48-张嘉予_,SNH48-杨冰怡,SNH48-冯晓菲,SNH48-宋昕冉,SNH48-邵雪聪-,
        5460951688, 5861113498, 5491331848, 5461287018, 5479678683, 5460952383,
        SNH48-杨韫玉--,SNH48-张丹三,SNH48-谢天依,
        5490958194, 5461288256, 5490615346,

        三：
        SNH48-吴燕文，SNH48-徐伊人，SNH48-许杨玉琢，SNH48-郝婉晴，SNH48-徐晗-，SNH48-张昕，
        5230875267,5228057280, 5228056212, 5229579490,5230456780, 5228234876,
        SNH48-刘佩鑫,SNH48-林楠,SNH48-刘炅然-,SNH48-王柏硕,SNH48-杨惠婷-,SNH48-李清扬,
        5230468891, 5231176541, 5230466807, 5230465572, 5227765832, 5231168847,
        SNH48-谢妮, SNH48-陈怡馨-,
        5230874533, 5221053921, 
        SNH48-张雨鑫,SNH48-赵晔，SNH48-袁丹妮,
        5225534295, 5221220112, 5225886388,

        一：
        SNH48-孔肖吟,SNH48-钱蓓婷,SNH48-徐_晨辰,SNH48-陈观慧,SNH48-莫寒,SNH48-李宇琪,
        3058127927, 3055272517, 3050758665, 3050708243, 3053424305, 3050792913,
        SNH48-陈思,SNH48-吴哲晗,SNH48-张语格,SNH48-许佳琪,SNH48-邱欣怡,SNH48-戴萌,
        3050742117, 3050731261, 3050783091, 3050737061, 3062769307,3050709151,
        
        二：
        SNH48-孙芮,SNH48-袁雨桢,SNH48-徐子轩,SNH48-沈之琳,SNH48-蒋芸,SNH48-温晶婕,
        3669091483, 3720838047, 3675905275, 3668820134, 3675573934, 3675603887,

        SNH48-林思意,SNH48-李艺彤,SNH48-陆婷,SNH48-陈问言,SNH48-董艳芸,SNH48-罗兰,
        3675865547, 3700233717, 3669120105, 5103897733, 3675584885, 273344863,
        SNH48-何晓玉,SNH48-龚诗淇,SNH48-易嘉爱,SNH48-陈佳莹,SNH48-赵粤,SNH48-黄婷婷,
        3675885002, 3705939425, 3675601605, 3668830595, 3668829440,3668822213,
        SNH48-万丽娜,SNH48-鞠婧祎,SNH48-曾艳芬,SNH48-唐安琪,SNH48-冯薪朵,
        3705941004, 3669102477, 3669076064, 3675587802,3675868752,

    ]
    =SUMIF(A2:A143,A300,B2:B143)/COUNTIF(A2:A143,A300)
    =SUMIF(A2:A568,A1201,B2:B568)/COUNTIF(A2:A1201,A300)
    七：
    start_urls = [
        6034778078, 6034492357, 6034212582, 6034780322, 6033922472, 6034777428, 
        6034777701, 6047256977, 6047258201, 6034210438, 6034785630, 6034488423, 
        6047257712, 6033924165, 6034495212, 6034787484, 6034779235, 6034493369, 
        6016757708, 6013595409, 6017033285, 6013595120, 6013823016, 6013595603,
        6013595744, 5617036654, 6013595317, 5617256267, 6013611098, 6013595830,
        6017289512, 6013595694, 5617036657, 6017032776, 6019361685,
        6013806959, 6013807023, 6013822815, 6013807210,
        6033312477, 6033035492, 6033592700, 6033593819,
        6022589086, 6019913036, 6020796878, 6019913274, 6021695822, 
        6022570907, 6022563429, 6020769478, 6021669925, 6020242753, 6022573703,
        6021143413, 6020242374, 6022034041,
    ]
    六：
    start_urls = [
        5886585193, 5885155590, 5886586996, 5886587197,
        5886797197, 5886997271, 5880065713, 5886998248 ,5886798137 ,5886798570,
        5886998975,5891499998 ,5891710058,
        5863012981, 5861952965,5861113498 ,5861422056,5861422830,5861115930,5863498042,5861419679,
        5891500145,5879769942 ,5880065358 , 5880065475,5880065587 ,5880066349,
        5879771257,5879771383 ,5880066726 ,5879772356 ,5886797095 ,5886797408,
        5886797829,5886998602 ,5891709949 ,5891711600 ,5891502165 ,
        5885722642, 5886364814, 5887712082, 5887863238,5887697862 ,5886364444,
        5887697249,5885812685 ,5885954688 ,5887698175 ,5887714199 ,5886589255 ,
        5885940120,5885955392 ,5887054947 ,5885708534 ,
    ]

    五：
    start_urls = [
        5681003434, 5786685220, 5681072386, 5690216533, 5686134819, 5786322468, 
        5786679436, 5680343342, 5680341906, 5691239843, 5786337191, 5681431767,
        5787012546, 5690264778,
        5681945173, 5682588352, 5691250627, 5693244741,
        5681353210, 5681004199, 5685088161 ,5691238431 ,5690266096 ,5786991235,
        5692183212, 5787002847,
        5680339910, 5681354886 ,5681355162,5685467003 ,5681479865 ,5681828458 ,
        5681476803, 5681480311, 5786332015,5786337946 ,5787334703 ,5787347460 ,
    ]

    四：
    start_urls = [
        5490236021, 
        5478873704, 5491330253, 5462211905, 5490234918, 5460950220, 5478872932,
        5460951688, 5861113498, 5491331848, 5461287018, 5479678683, 5460952383,
        5490958194, 5461288256, 5490615346,
    ]

    三：
    start_urls = [
        5230875267, 5228057280, 5228056212, 5229579490, 5230456780, 5228234876, 
        5230468891, 5231176541, 5230466807, 5230465572, 5227765832, 5231168847,
        5230874533, 5221053921, 
        5225534295, 5221220112, 5225886388,
    ]

    二：
    start_urls = [
        3669091483, 3720838047, 3675905275, 3668820134, 3675573934, 3675603887,
        3675865547, 3700233717, 3669120105, 5103897733, 3675584885, 273344863,
        3675885002, 3705939425, 3675601605, 3668830595, 3668829440, 3668822213,
        3705941004, 3669102477, 3669076064, 3675587802, 3675868752,
    ]
    一：
    start_urls = [
        3058127927, 3055272517, 3050758665, 3050708243, 3053424305, 3050792913,
        3050742117, 3050731261, 3050783091, 3050737061, 3062769307, 3050709151,
    ]



    mongod.exe --dbpath D:\workzone\venv\Scrapy\mongodb
    '''


    start_urls = [
        6034778078, 6034492357, 6034212582, 6034780322, 6033922472, 6034777428, 
        6034777701, 6047256977, 6047258201, 6034210438, 6034785630, 6034488423, 
        6047257712, 6033924165, 6034495212, 6034787484, 6034779235, 6034493369, 
        6016757708, 6013595409, 6017033285, 6013595120, 6013823016, 6013595603,
        6013595744, 5617036654, 6013595317, 5617256267, 6013611098, 6013595830,
        6017289512, 6013595694, 5617036657, 6017032776, 6019361685,
        6013806959, 6013807023, 6013822815, 6013807210,
        6033312477, 6033035492, 6033592700, 6033593819,
        6022589086, 6019913036, 6020796878, 6019913274, 6021695822, 
        6022570907, 6022563429, 6020769478, 6021669925, 6020242753, 6022573703,
        6021143413, 6020242374, 6022034041,
    ]
    scrawl_ID = set(start_urls)  # 记录待爬的微博ID
    finish_ID = set()  # 记录已爬的微博ID

    def start_requests(self):
        while True:
            ID = self.scrawl_ID.pop()
            self.finish_ID.add(ID)  # 加入已爬队列
            ID = str(ID)
            follows = []
            followsItems = FollowsItem()
            followsItems["_id"] = ID
            followsItems["follows"] = follows
            fans = []
            fansItems = FansItem()
            fansItems["_id"] = ID
            fansItems["fans"] = fans

            url_follows = "http://weibo.cn/%s/follow" % ID
            url_fans = "http://weibo.cn/%s/fans" % ID
            url_tweets = "http://weibo.cn/%s/profile?filter=1&page=1" % ID
            url_information0 = "http://weibo.cn/attgroup/opening?uid=%s" % ID
            #yield Request(url=url_follows, meta={"item": followsItems, "result": follows},
            #              callback=self.parse3)  # 去爬关注人
            #yield Request(url=url_fans, meta={"item": fansItems, "result": fans}, callback=self.parse3)  # 去爬粉丝
            yield Request(url=url_information0, meta={"ID": ID}, callback=self.parse0)  # 去爬个人信息
            yield Request(url=url_tweets, meta={"ID": ID}, callback=self.parse2)  # 去爬微博

    def parse0(self, response):
        """ 抓取个人信息1 """
        informationItems = InformationItem()
        selector = Selector(response)
        text0 = selector.xpath('body/div[@class="u"]/div[@class="tip2"]').extract_first()
        if text0:
            num_tweets = re.findall(u'\u5fae\u535a\[(\d+)\]', text0)  # 微博数
            num_follows = re.findall(u'\u5173\u6ce8\[(\d+)\]', text0)  # 关注数
            num_fans = re.findall(u'\u7c89\u4e1d\[(\d+)\]', text0)  # 粉丝数
            if num_tweets:
                informationItems["Num_Tweets"] = int(num_tweets[0])
            if num_follows:
                informationItems["Num_Follows"] = int(num_follows[0])
            if num_fans:
                informationItems["Num_Fans"] = int(num_fans[0])
            informationItems["_id"] = response.meta["ID"]
            url_information1 = "http://weibo.cn/%s/info" % response.meta["ID"]
            yield Request(url=url_information1, meta={"item": informationItems}, callback=self.parse1)

    def parse1(self, response):
        """ 抓取个人信息2 """
        informationItems = response.meta["item"]
        selector = Selector(response)
        text1 = ";".join(selector.xpath('body/div[@class="c"]/text()').extract())  # 获取标签里的所有text()
        nickname = re.findall(u'\u6635\u79f0[:|\uff1a](.*?);', text1)  # 昵称
        gender = re.findall(u'\u6027\u522b[:|\uff1a](.*?);', text1)  # 性别
        place = re.findall(u'\u5730\u533a[:|\uff1a](.*?);', text1)  # 地区（包括省份和城市）
        signature = re.findall(u'\u7b80\u4ecb[:|\uff1a](.*?);', text1)  # 个性签名
        birthday = re.findall(u'\u751f\u65e5[:|\uff1a](.*?);', text1)  # 生日
        sexorientation = re.findall(u'\u6027\u53d6\u5411[:|\uff1a](.*?);', text1)  # 性取向
        marriage = re.findall(u'\u611f\u60c5\u72b6\u51b5[:|\uff1a](.*?);', text1)  # 婚姻状况
        url = re.findall(u'\u4e92\u8054\u7f51[:|\uff1a](.*?);', text1)  # 首页链接

        if nickname:
            informationItems["NickName"] = nickname[0]
        if gender:
            informationItems["Gender"] = gender[0]
        if place:
            place = place[0].split(" ")
            informationItems["Province"] = place[0]
            if len(place) > 1:
                informationItems["City"] = place[1]
        if signature:
            informationItems["Signature"] = signature[0]
        if birthday:
            try:
                birthday = datetime.datetime.strptime(birthday[0], "%Y-%m-%d")
                informationItems["Birthday"] = birthday - datetime.timedelta(hours=8)
            except Exception:
                pass
        if sexorientation:
            if sexorientation[0] == gender[0]:
                informationItems["Sex_Orientation"] = "gay"
            else:
                informationItems["Sex_Orientation"] = "Heterosexual"
        if marriage:
            informationItems["Marriage"] = marriage[0]
        if url:
            informationItems["URL"] = url[0]
        yield informationItems

    def parse2(self, response):
        """ 抓取微博数据 """
        selector = Selector(response)
        tweets = selector.xpath('body/div[@class="c" and @id]')
        for tweet in tweets:
            tweetsItems = TweetsItem()
            id = tweet.xpath('@id').extract_first()  # 微博ID
            content = tweet.xpath('div/span[@class="ctt"]/text()').extract_first()  # 微博内容
            cooridinates = tweet.xpath('div/a/@href').extract_first()  # 定位坐标
            like = re.findall(u'\u8d5e\[(\d+)\]', tweet.extract())  # 点赞数
            transfer = re.findall(u'\u8f6c\u53d1\[(\d+)\]', tweet.extract())  # 转载数
            comment = re.findall(u'\u8bc4\u8bba\[(\d+)\]', tweet.extract())  # 评论数
            others = tweet.xpath('div/span[@class="ct"]/text()').extract_first()  # 求时间和使用工具（手机或平台）

            tweetsItems["ID"] = response.meta["ID"]
            tweetsItems["_id"] = response.meta["ID"] + "-" + id
            if content:
                tweetsItems["Content"] = content.strip(u"[\u4f4d\u7f6e]")  # 去掉最后的"[位置]"
            if cooridinates:
                cooridinates = re.findall('center=([\d|.|,]+)', cooridinates)
                if cooridinates:
                    tweetsItems["Co_oridinates"] = cooridinates[0]
            if like:
                tweetsItems["Like"] = int(like[0])
            if transfer:
                tweetsItems["Transfer"] = int(transfer[0])
            if comment:
                tweetsItems["Comment"] = int(comment[0])
            if others:
                others = others.split(u"\u6765\u81ea")
                tweetsItems["PubTime"] = others[0]
                if len(others) == 2:
                    tweetsItems["Tools"] = others[1]
            yield tweetsItems
        #url_next = selector.xpath(
        #    u'body/div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href').extract()
        #if url_next:
        #    yield Request(url=self.host + url_next[0], meta={"ID": response.meta["ID"]}, callback=self.parse2)

    def parse3(self, response):
        """ 抓取关注或粉丝 """
        items = response.meta["item"]
        selector = Selector(response)
        text2 = selector.xpath(
            u'body//table/tr/td/a[text()="\u5173\u6ce8\u4ed6" or text()="\u5173\u6ce8\u5979"]/@href').extract()
        for elem in text2:
            elem = re.findall('uid=(\d+)', elem)
            if elem:
                response.meta["result"].append(elem[0])
                ID = int(elem[0])
                if ID not in self.finish_ID:  # 新的ID，如果未爬则加入待爬队列
                    self.scrawl_ID.add(ID)
        url_next = selector.xpath(
            u'body//div[@class="pa" and @id="pagelist"]/form/div/a[text()="\u4e0b\u9875"]/@href').extract()
        if url_next:
            yield Request(url=self.host + url_next[0], meta={"item": items, "result": response.meta["result"]},
                          callback=self.parse3)
        else:  # 如果没有下一页即获取完毕
            yield items

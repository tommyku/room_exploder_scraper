import scrapy, os, re
from scrapy.contrib.exporter import JsonItemExporter
from room_exploder.items import TimeslotItem

class TimeslotSpider(scrapy.Spider):
    name = "timeslot"
    allowed_domains = ["ust.hk"]
    start_urls = [
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ACCT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/AESF",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/BIEN",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/BIPH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/BTEC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CBME",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CENG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CHEM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CHMS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CIEM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CIVL",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/COMP",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CPEG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CSIC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/CSIT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ECON",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/EEMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/EESM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ELEC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ENGG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ENTR",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ENVR",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ENVS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/EVNG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/EVSM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/FINA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/GBUS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/GNED",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/HART",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/HLTH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/HMMA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/HUMA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/IBTM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/IDPO",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/IELM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/IIMP",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/ISOM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/JEVE",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/LABU",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/LANG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/LIFS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MAED",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MAFS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MARK",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MATH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MECH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MESF",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MGCS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MGMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MILE",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MIMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/MSBD",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/NANO",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/PDEV",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/PHYS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/PPOL",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/RMBI",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SBMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SCIE",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SHSS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SOSC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SSMA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/SUST",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/TEMG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1710/subject/UROP",
    ]
    exporters = []

    def __init__(self, category=None, *args, **kwargs):
        super(TimeslotSpider, self).__init__(*args, **kwargs)
        # 7 exporters, 7 files for 7 week days
        for i in range(7):
            f = open('./timeslots/'+str(i)+'.json', "w+")
            self.exporters.append(JsonItemExporter(f))
            self.exporters[i].start_exporting()

    def closed(self, reason):
        for i in self.exporters:
            i.finish_exporting()


    def parse(self, response):
        dept = response.url.split("/")[-1]

        courses = response.xpath('//*[@id="classes"]/div[@class="course"]/h2')
        pattern = {
 	    'oneDay': '[a-zA-Z]{2} [0-9]{2}\:[0-9]{2}(PM|AM) - [0-9]{2}\:[0-9]{2}(PM|AM)', 
            'twoDay': '[a-zA-Z]{4} [0-9]{2}\:[0-9]{2}(PM|AM) - [0-9]{2}\:[0-9]{2}(PM|AM)'
        }

        for i in range(0, len(courses)):
            # for each course, get its sections
            sections = response.xpath('//*[@id="classes"]/div['+str(i+1)+']/table/tr[position()>1]')
            course = response.xpath('//*[@id="classes"]/div['+str(i+1)+']/h2/text()').re('^([A-Z]{4}) ([0-9]{4}[A-Z]{0,1}) - (.*) \(([0-9]{1,2}) unit')

            for row in sections:
                if (len(row.xpath('@class').re('newsect'))):
                    # new session, check td2 and td3
                    tstr = row.xpath('td[2]/text()').extract()[0]
                    room = row.xpath('td[3]/text()').extract()[0]
                else:
                    # not new session, check td1 and td 2
                    tstr = row.xpath('td[1]/text()').extract()[0]
                    room = row.xpath('td[2]/text()').extract()[0]

                timeslot = TimeslotItem()
                if (re.match(pattern['oneDay'], tstr)):
                    # one day
                    timeslot['wd'] = self.getWeekDayIndexFromName(tstr[0:2])
                    timeslot['start'] = self.getTimeIndexFromTimeStr(tstr[3:10])
                    timeslot['end'] = self.getTimeIndexFromTimeStr(tstr[13:20])
                    timeslot['room'] = room
                    self.exporters[timeslot['wd']].export_item(timeslot)
                elif (re.match(pattern['twoDay'], tstr)):
                    # two day
                    timeslot['wd'] = self.getWeekDayIndexFromName(tstr[0:2])
                    timeslot['start'] = self.getTimeIndexFromTimeStr(tstr[5:12])
                    timeslot['end'] = self.getTimeIndexFromTimeStr(tstr[15:22])
                    timeslot['room'] = room
                    self.exporters[timeslot['wd']].export_item(timeslot)
                    timeslot = TimeslotItem()
                    timeslot['wd'] = self.getWeekDayIndexFromName(tstr[2:4])
                    timeslot['start'] = self.getTimeIndexFromTimeStr(tstr[5:12])
                    timeslot['end'] = self.getTimeIndexFromTimeStr(tstr[15:22])
                    timeslot['room'] = room
                    self.exporters[timeslot['wd']].export_item(timeslot)

    def getTimeIndexFromTimeStr(self, tstr):
        val = (int(tstr[0:2])-8)*2 # i really should use sth like 09:00:00 or simply 9
        val += 1 if (tstr[3:5] in ["20","30"]) else 0
        val += 2 if (tstr[3:5] == "50") else 0
        val += 24 if (tstr[5:7] == "PM" and tstr[0:2] != "12") else 0
        return val;

    def getWeekDayIndexFromName(self, tstr):
        if (tstr == "Mo"): return 1
        elif (tstr == "Tu"): return 2
        elif (tstr == "We"): return 3
        elif (tstr == "Th"): return 4
        elif (tstr == "Fr"): return 5
        elif (tstr == "Sa"): return 6
        elif (tstr == "Su"): return 0
        return -1

    def getRoom(self, room):
        return room

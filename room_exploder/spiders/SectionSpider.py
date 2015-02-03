import scrapy, os, re
from scrapy.contrib.exporter import JsonItemExporter
from room_exploder.items import SessionItem

class SectionSpider(scrapy.Spider):
    name = "section"
    allowed_domains = ["ust.hk"]
    start_urls = [
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ACCT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/BIEN",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/BTEC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CBME",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CENG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CHEM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CIEM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CIVL",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/COMP",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/CSIT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ECON",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/EEMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/EESM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ELEC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ENEG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ENGG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ENTR",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ENVR",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ENVS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/EVNG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/EVSM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/FINA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/FYTG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/GBUS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/GFIN",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/GNED",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/HART",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/HLTH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/HUMA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/IBTM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/IDPO",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/IELM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/ISOM",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/JEVE",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/LABU",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/LANG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/LIFS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MAFS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MARK",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MATH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MECH",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MESF",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MGCS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MGMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/MIMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/NANO",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/PDEV",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/PHYS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/RMBI",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SBMT",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SCED",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SCIE",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SHSS",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SOSC",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/SSMA",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/TEMG",
        "https://w5.ab.ust.hk/wcq/cgi-bin/1430/subject/UROP"
    ]

    def parse(self, response):
        dept = response.url.split("/")[-1]

        courses = response.xpath('//*[@id="classes"]/div[@class="course"]/h2')

        f = open('./sections/'+dept+'.json', "w+")
        exporter = JsonItemExporter(f)
        exporter.start_exporting()

        for i in range(0, len(courses)):
            # for each course, get its sections
            sections = response.xpath('//*[@id="classes"]/div['+str(i+1)+']/table/tr[position()>1]')
            course = response.xpath('//*[@id="classes"]/div['+str(i+1)+']/h2/text()').re('^([A-Z]{4}) ([0-9]{4}[A-Z]{0,1}) - (.*) \(([0-9]{1,2}) unit')
            dept, code, name, credit = course[0], course[1], course[2], course[3]
            session = None
            for row in sections:
                if (len(row.xpath('@class').re('newsect'))):
                    # new session
                    if (session != None):
                        # close the last session if not None
                        session['instructor'] = list(session['instructor'])
                        exporter.export_item(session)
                    session = SessionItem()
                    session['dept'] = dept
                    session['code'] = code
                    session['name'] = name # course name
                    session['session'] = self.getSectionName(row.xpath('td[1]/text()')) # e.g. L1, LA1
                    session['instructor'] = set(row.xpath('td[4]/a/text()').extract()) # set() makes sure it is unique
                    session['code'] = self.getClassCode(row.xpath('td[1]/text()')) # class code beside session
                    session['timeslots'] = []
                    session['timeslots'] = session['timeslots'] + (self.parseTime(row.xpath('td[2]/text()').extract()[0], row.xpath('td[3]/text()').extract()[0]))
                else:
                    # not new session, add instructor and timeslots
                    session['instructor'] = session['instructor'].union(set(row.xpath('td[4]/a/text()').extract()))
                    session['timeslots'] = session['timeslots'] + (self.parseTime(row.xpath('td[1]/text()').extract()[0], row.xpath('td[2]/text()').extract()[0]))

        if (session != None):
            # close the last one
            session['instructor'] = list(session['instructor'])
            exporter.export_item(session)

        exporter.finish_exporting()

    def getSectionName(self, td):
        r = td.re('^([A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1})')
        if (len(r)):
            return r[0]
        else:
            return ''

    def getClassCode(self, td):
        r = td.re('^[A-Z]{1,2}[0-9]{1,2}[A-Z]{0,1} \(([0-9]{3,5})\)')
        if (len(r)):
            return r[0]
        else:
            return ''

    def getTimeIndexFromTimeStr(self, tstr):
        val = (int(tstr[0:2])-8)*2
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

    def parseTime(self, tstr, room):
        room = self.getRoom(room)
        if (re.match('[a-zA-Z]{2} [0-9]{2}\:[0-9]{2}(PM|AM) - [0-9]{2}\:[0-9]{2}(PM|AM)',tstr)):
            rtnObj = [{"wd":self.getWeekDayIndexFromName(tstr[0:2]), "start": self.getTimeIndexFromTimeStr(tstr[3:10]), "end": self.getTimeIndexFromTimeStr(tstr[13:20]), "room": room}]
            return rtnObj

        if (re.match('[a-zA-Z]{4} [0-9]{2}\:[0-9]{2}(PM|AM) - [0-9]{2}\:[0-9]{2}(PM|AM)',tstr)):
            rtnObj = [{"wd":self.getWeekDayIndexFromName(tstr[0:2]), "start": self.getTimeIndexFromTimeStr(tstr[5:12]), "end": self.getTimeIndexFromTimeStr(tstr[15:22]), "room": room}]
            rtnObj.append({"wd":self.getWeekDayIndexFromName(tstr[2:4]),"start":rtnObj[0]["start"],"end":rtnObj[0]["end"], "room": room})
            return rtnObj

        return [{"wd":0, "start": 0, "end": 0, "room": ""}]

import scrapy, os
from scrapy.contrib.exporter import JsonItemExporter
from room_exploder.items import CourseItem

class CourseSpider(scrapy.Spider):
    name = "course"
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

        courses = response.xpath('//*[@id="classes"]/div[@class="course"]/h2/text()').re('^([A-Z]{4}) ([0-9]{4}[A-Z]{0,1}) - (.*) \(([0-9]{1,2}) units\)')

        f = open('./courses/'+dept+'.json', "w+")
        exporter = JsonItemExporter(f)

        exporter.start_exporting()
        for i in range(0, len(courses), 4):
            dept, code, name, credit = courses[i], courses[i+1], courses[i+2], courses[i+3]
            print dept, code, name, credit

            item = CourseItem()
            item['dept'] = dept
            item['code'] = code
            item['name'] = name
            item['credit'] = credit
            exporter.export_item(item)

        exporter.finish_exporting()

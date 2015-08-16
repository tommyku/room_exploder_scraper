Room exploder
=============

Room exploder is a python scrapy project which fetch and prase the [HKUST course catalogue](w5.ab.ust.hk/wcq/cgi-bin/) to extra various course-related data. From which one can generate a list of empty classroom at each 30-minute timeslot of a weekday.

Requirements
------------

- Python 2.7
- Scrapy 0.24.4

Configuration
-------------

1. Install Python 2.7 and pip

   ```bash
   sudo apt-get install python2.7 python2.7-dev pip
   ```

2. Install Scrapy

   ```bash
   pip install Scrapy
   ```

Usage
-----

3 spiders are created to grab course information, section information and timeslot information respectively. You should change the URLs listed within each spider if you are parsing data for another semester from the course catalog.

1. To grab course information, run in the application folder

   ```bash
   scrapy crawl course
   ```

2. To grab section information, run in the application folder

   ```bash
   scrapy crawl section
   ```

3. To grab timeslot information, run in the application folder

   ```bash
   scrapy crawl timeslot
   ```

There is an extra Python script created to convert results from timeslot spider into JSON format that the UST爆房 needs.

```bash
python timeslotsSorter.py
```

After executing that, there is a `database.json` created that works with UST爆房's data seeder class to feed the data into MySQL database.

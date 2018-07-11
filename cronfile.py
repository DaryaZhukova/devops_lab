from crontab import CronTab
from configparser import ConfigParser
parser = ConfigParser()
parser.read('simple.ini')
my_cron = CronTab(user='student')
job = my_cron.new(command='python ~/PycharmProjects/hometask2/monitoring.py')
job.minute.every(parser.get("common", "interval"))
my_cron.write()

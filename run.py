import datetime, os
import unittest
from HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    test_dir = 'auction_interface'
    report_dir = './report/'
    report_name = report_dir + (datetime.datetime.now()).strftime('%Y-%m-%d%H%M%S') + 'report.html'
    discover = unittest.defaultTestLoader.discover(test_dir, 'auction_interface.py')
    fp = open(report_name, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'测试报告', description=u'用例执行情况:')
    runner.run(discover)
    fp.close()

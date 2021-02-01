import unittest
import HTMLTestRunner
class Search(unittest.TestCase):
    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断1==1")

    def test_notequal(self):
        print("不相等")
        #self.assertNotEqual(1,2,"判断1！=2")
        self.assertTrue(1==1,"verify")

class Search1(unittest.TestCase):
    def test_equal(self):
        print("断言相等1")
        self.assertEqual(1,1,"判断1==1")

    def test_notequal(self):
        print("不相等1")
        #self.assertNotEqual(1,2,"判断1！=2")
        self.assertTrue(1==1,"verify")

if __name__ == '__main__':
    # 1、执行当前文件所有的unittest测试用例
    # unittest.main()
    #2、执行指定的测试用例，添加到将要执行的测试套件里
    # suite=unittest.TestSuite()
    # suite.addTest(Search("test_equal"))
    # unittest.TextTestRunner().run(suite)
    # 3、执行某个测试类 将测试类添加到测试套件里
    # suite1=unittest.TestLoader().loadTestsFromTestCase(Search)
    # suite3=unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite3)
    report_title = '测试用例执行报告'
    desc = '用于展示修改样式后的HTMLTestRunner'
    report_file = 'result.html'

    suite1 = unittest.TestLoader().loadTestsFromTestCase(Search)
    suite3=unittest.TestSuite([suite1])
    # unittest.TextTestRunner(verbosity=2).run(suite3)

    with open(report_file, 'wb') as report:
        runner = HTMLTestRunner(stream=report, title=report_title, description=desc)
        runner.run(suite3)
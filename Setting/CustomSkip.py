import types
import unittest
from functools import wraps


# 根据unitest库下的skipIf类自定义跳过测试用例，返回自定义跳过理由
def skip_dependent(depend=""):
    # def __new__(self, depend=""):
    #     """
    #     :param depend: 依赖的用例函数名，默认为空
    #     :return: wraper_func
    #     """

    def wraper_func(test_func):
        @wraps(test_func)  # @wraps: 避免被装饰函数自身的信息丢失
        def inner_func(self):
            if depend == test_func.__name__:
                raise ValueError("[] cannot depend on itself".format(depend))
            # print("self._outcome", self._outcome.__dict__)
            # 此方法适用Fpython3.4 +
            # 如是低版本的python3，请将self._outcome.result修欧为self._outcomeForDoCleanups
            # 如你是python2版本，请将self._outcome.result修欧为self._resultForDoCleanups
            failures = str([fail[0] for fail in self._outcome.result.failures])
            errors = str([error[0] for error in self._outcome.result.errors])
            skipped = str([error[0] for error in self._outcome.result.skipped])
            flag = (depend in failures) or (depend in errors) or (depend in skipped)
            if failures.find(depend) != -1:
                # 输出结果 [< main .TestDemo testMethod=test Login>]
                # 如果依赖的用例名在failures 中，则判定为失败，以下两种信况同理
                # find()方法，查找子字符串，若找到返回从0开始的下标值，若找不到返回 - 1
                test = unittest.skipIf(flag, "{} failed".format(depend))(test_func)
            elif errors.find(depend) != -1:
                test = unittest.skipIf(flag, "{} error".format(depend))(test_func)
            elif skipped.find(depend) != -1:
                test = unittest.skipIf(flag, "{} skipped".format(depend))(test_func)
            else:
                test = test_func
            return test(self)

        return inner_func

    return wraper_func


def skip_failed_cases(reason):
    """根据reason直接跳过"""
    def decorator(test_item):
        if isinstance(test_item, type):
            @wraps(test_item)
            def skip_wrapper(self, *args, **kwargs):
                print(type(test_item))
                if super(self).__unittest_expecting_failure__:
                    # 假设expecting_failure截取到true,跳过test_item
                    raise unittest.SkipTest(reason)
            test_item = skip_wrapper
        else:
            pass

        # 非func就跳过所有类
        test_item.__unittest_skip__ = True
        test_item.__unittest_skip_why__ = reason
        return test_item

    if isinstance(reason, types.FunctionType):
        test_item = reason
        reason = ''
        return decorator(test_item)
    return decorator


def stop_on_failure(cls):
    orig_run = cls.run

    def run_with_stop(self, result=None):
        if result is None:
            result = self.defaultTestResult()

        def stop_on_failure_test(self, test, err):
            if result.wasSuccessful():
                # 如果之前有测试用例失败，则停止执行当前测试用例
                # cls._callTearDown
                raise StopIteration
            return stop_on_failure_test

        result.addError = stop_on_failure_test.__get__(result, result.__class__)
        result.addFailure = stop_on_failure_test.__get__(result, result.__class__)

        orig_run(self, result)

    cls.run = run_with_stop
    return cls


def stop_on(cls):
    """
    装饰器函数，用于停止运行发现失败的unittest测试用例
    """
    orig_run = cls.run

    def new_run(self, result=None):
        """
        新的run函数，用于停止运行发现失败的用例
        """
        if result is None:
            result = self.defaultTestResult()

        class FailStopResult(unittest.TextTestResult):
            """
            重写TextTestResult类，用于停止运行发现失败的用例
            """
            def addFailure(self, test, err):
                super().addFailure(test, err)
                self.shouldStop = True  # 设置shouldStop为True，停止运行

            def addError(self, test, err):
                super().addError(test, err)
                self.shouldStop = True  # 设置shouldStop为True，停止运行

        result.__class__ = FailStopResult
        return orig_run(cls, result)

    cls.run = new_run
    return cls


"""
def run(self, result=None):
    try:
        self._outcome = outcome

        with outcome.testPartExecutor(self):
            self._callSetUp()
        if outcome.success:
            outcome.expecting_failure = expecting_failure
            with outcome.testPartExecutor(self, isTest=True):
                self._callTestMethod(testMethod)
                # Check if an error occurred
                if outcome.errors:
                    return result  # If error occurred, return immediately
            outcome.expecting_failure = False
            with outcome.testPartExecutor(self):
                self._callTearDown()
"""
"""
class Myskip(object):

    def __new__(cls):
         :return inner_func


        def wrap_func(test_item):
            @wraps(test_item)
            def inner_func(self):
                # 判断当前item类型是class还是method
                failures = str([fail[0] for fail in self._outcome.result.failures])
                # if inspect.isclass(self.test_item):
                    # print("object is class")
                    # functions = self.test_item.__dict__
                    # funcList = difflib.get_close_matches('test_', functions, 20, cutoff=0.7)
                    # print(funcList)
                for name, method in super().__dict__.items():
                    if name.startswith('test_'):
                        if name.find(failures) != -1:
                            raise unittest.SkipTest("{} do not execute because {} is failed".format(name,
                                  self._outcome.result.failures[0][0]._testMethodName))

                # else:
                #     # failures = str([fail[0] for fail in self._outcome.result.failures])
                #     test_func = test_item.__name__
                #     if test_func.find(failures) != -1:
                #         raise unittest.SkipTest("{} do not execute because {} is failed".format(test_func.name,
                #                 self._outcome.result.failures[0][0]._testMethodName))
                        return name(self)
                return inner_func
        return wrap_func
"""
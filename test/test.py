def check_login(session,SECRET_KEY):
    print(123)
    def check_login_dec(func):
        def wrapper( *args):
            return func(1)
        return wrapper
    return check_login_dec
@check_login("12",1)
def testb(test):
    print("hi",test)
if __name__ == '__main__':
    print(testb("aaa"))

import utils.token as glv
from testcase.test01_login import TestLogin

glv.__init__()
token_l = TestLogin.test_001_login_success.token_l
glv.set_token("token", token_l)

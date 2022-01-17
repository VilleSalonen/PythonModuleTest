from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn

@library
class BrowserUtils:
    """ Browser Utils """
    @keyword
    def some_browser_util(self):
        """ Foobar some documentation """
        BuiltIn().log("called some_browser_util")

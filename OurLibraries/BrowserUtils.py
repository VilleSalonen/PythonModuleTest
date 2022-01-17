from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn

from OurLibraries.SomeOtherUtils import super_secret_source
from OurLibraries.AnotherSecret import SecretFactory

@library
class BrowserUtils:
    """ Browser Utils """
    @keyword
    def some_browser_util(self):
        """ Foobar some documentation """
        BuiltIn().log_to_console("read secret: " + super_secret_source())
        BuiltIn().log_to_console("factory secret: " + SecretFactory.secret_factory_function())

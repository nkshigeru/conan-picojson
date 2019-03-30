import os
from conans import ConanFile, tools


class PicojsonConan(ConanFile):
    name = "picojson"
    version = "1.3.0"
    license = "BSD 2-Clause"
    author = "<Put your name here> <And your email here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Picojson here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    no_copy_source = True

    def source(self):
        tools.get("https://github.com/kazuho/picojson/archive/v%s.tar.gz" % self.version)
        os.rename("picojson-%s" % self.version, "picojson")

    def package(self):
        self.copy("picojson/picojson.h", dst="include", keep_path=False)

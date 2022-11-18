import pyqrcode
import png
urlstring = "https://github.com/CaliburnSlash/zk-SNARKS"

url = pyqrcode.create(urlstring)

url.png('zk_snarks_github_url.png', scale=6)
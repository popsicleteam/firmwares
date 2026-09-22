include("$(PORT_DIR)/boards")

include("$(MOD_DIR)/fos")
include("$(MOD_DIR)/blerepl")
include("$(MOD_DIR)/macutils")
include("$(MOD_DIR)/settings")

require("base64")
require("hmac")
require("logging")
require("threading")

require("aioble")
require("aioespnow")
require("aiohttp")
require("ntptime")
require("umqtt.simple")

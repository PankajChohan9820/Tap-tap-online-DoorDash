from os import access
import jwt.utils
import time
import math

accessKey = {
  "developer_id": "d2386634-120a-48ca-8f8f-f86e80b0056b",
  #Your key
  "key_id": "",
  "signing_secret": ""
}

token = jwt.encode(
    {
        "aud": "doordash",
        "iss": accessKey["developer_id"],
        "kid": accessKey["key_id"],
        "exp": str(math.floor(time.time() + 60)),
        "iat": str(math.floor(time.time())),
    },
    jwt.utils.base64url_decode(accessKey["signing_secret"]),
    algorithm="HS256",
    headers={"dd-ver": "DD-JWT-V1"})

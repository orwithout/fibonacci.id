from fastapi import HTTPException
from jose import ExpiredSignatureError, JWTError, jwt
import os
from .login_env import init_settings  # 导入 settings 对象

def verify_token(user_id: int, verify_token=False, token_in_header: str = "", token_in_url: str = ""):
   
    if not token_in_header:
        token_in_header = token_in_url
    if not token_in_header:
        raise HTTPException(status_code=401, detail="Could not validate credentials 1")

    settings = init_settings(str(user_id))
    
    try:
        payload = jwt.decode(token_in_header, settings.secret_key, algorithms=[settings.algorithm])
        account: str = payload.get("sub")
        login_method: str = payload.get("mod")
        if account is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials 2")
        print("ffffffffff")
        
        # 检查黑名单
        blacklist_path = os.path.join(str(user_id), ".auth", "token_blacklist.txt")
        if os.path.exists(blacklist_path):
            print("ffffffffffx1")
            with open(blacklist_path, "r") as blacklist_file:
                print("ffffffffffx2")
                if token_in_header in blacklist_file.read():
                    print("ffffffffffx3")
                    raise HTTPException(status_code=401, detail="Could not validate credentials 3")
    except ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Could not validate credentials 4")
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials 5")

    # 从文件加载用户数据
    passwd_file = os.path.join(str(user_id), ".auth", f"{login_method}.{account}.txt")
    if not os.path.exists(passwd_file):
        raise HTTPException(status_code=401, detail="Could not validate credentials 6")
    else:
        return account



# fetch('http://your-api-url.com/0/some-protected-route', {
#   method: 'GET',
#   headers: {
#     'token_in_header': 'token'
#   }
# })
# .then(response => response.json())
# .then(data => console.log(data));


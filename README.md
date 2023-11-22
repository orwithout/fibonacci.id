# Fibonacci.id（AI多轮对话应用助理的后端）项目说明

查看： 设计文档 （正在准备中）




## 一、演示
**DEMO** v0.0.1: http://fibonacci.id （正在准备中）


## 二、安装

1. 克隆项目  
    项目源代码可以直接下载然后解压：https://github.com/orwithout/fibonacci.id/archive/refs/heads/main.zip  
    如果想要使用git 克隆，需要先安装git软件（下载: https://git-scm.com/downloads ），然后打开电脑系统的命令终端，运行：（它会把源代码下载到当前命令终端的工作目录）
    ```bash
    git clone https://www.github.com/orwithout/fibonacci.id.git
    ```



2. 安装 Python 环境  
    Windows 系统 安装方法（记得在安装过程中选上“Add Python 3.x to PATH”，如果忘记了，可卸载并再次安装）：https://docs.python.org/zh-cn/3.13/using/windows.html  
    Linux 系统 安装方法：[https://docs.python.org/zh-cn/3.13/using/unix.html](https://docs.python.org/zh-cn/3.13/using/unix.html)
   
3. 导航到解压或克隆下来的 `fibonacci.id` 目录：
    ```bash
    cd fibonacci.id
    ```
4. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
    **对于windows conda环境 可使用 set_conda.cmd*
5. 启动：
    ```bash
    # windows 系统 执行：
    start.cmd
    # Linux系统 执行：
    start.sh
    ```
6. 访问 http://127.0.0.1:8002/0/a00 ，然后可以看到浏览器显示 fibonacci.id/0/a00 中的示例数据


### 附：
- [服务化配置（Systemd后台进程守护）](https://github.com/orwithout/fibonacci.id/blob/main/readme/README.systemd.md)
- [Nginx配置](https://github.com/orwithout/fibonacci.id/blob/main/readme/README.nginx.md)
- [fastapi入门参考](https://fastapi.tiangolo.com/zh/#:~:text=%E8%B4%9F%E8%B4%A3%E6%95%B0%E6%8D%AE%E9%83%A8%E5%88%86%E3%80%82-,%E5%AE%89%E8%A3%85,-%C2%B6)
- [FastAPI 官方文档](https://fastapi.tiangolo.com/zh/)
- [git克隆github项目方法的更多说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)


## 三、如何添加功能
1. 项目启动简要说明  
    启动项目，会侦听8002端口，载入 main/main.py （在项目根目录）以处理URL路径路由。  
    示例URL: http://127.0.0.1:8002/0/a00?fn=m002_crud/read.py?args_in_url=abcxyz  
    (这将读取并返回项目根目录 0/a00/ 中内容)


2. 新建功能模块  
   例如新建 fibonacci.id/main/m003_ex/hello_world.py ，写入以下内容并保存：
    ```python
    # 存在于文件 fibonacci.id/main/m003_ex/hello_world.py
    import json

    def hello_world(verify_token=False, user_id="", full_path="", sub_path="", temp_file_path="", fn="", accept="", content_type="", args_in_url="", token_in_url="", args_in_header="", token_in_header="", headers="", body=""):
        data = {
            "user_id": str(user_id),
            "full_path": str(full_path),
            "sub_path": str(sub_path),
            "temp_file_path": str(temp_file_path),
            "fn": str(fn),
            "accept": str(accept),
            "content_type": str(content_type),
            "args_in_url": str(args_in_url),
            "token_in_url": str(token_in_url),
            "args_in_header": str(args_in_header),
            "token_in_header": str(token_in_header),
            "headers": str(headers),
            "body": str(body),
            "message": "hello world"
        }
        return data

    ```
    启动后，访问：  
    http://127.0.0.1:8002/0/a00?fn=m003_ex/hello_world.py&args_in_url=abcxyz&token_in_url=eyJhbGciOiJIUzI……  
    （使用?分割路径与参数，使用&分隔多个参数）  
    浏览器将显示：（这是所有可用的预定义参数变量）
    ```json
    {
        "user_id": "0",
        "full_path": "D:\\agent\\fibonacci.id\\0\\a00",
        "sub_path": "0\\a00",
        "temp_file_path": "",
        "fn": "m003_ex/hello_world.py",
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "content_type": "None",
        "args_in_url": "abcxyz",
        "token_in_url": "eyJhbGciOiJIUzI……",
        "args_in_header": "None",
        "token_in_header": "None",
        "headers": "Headers({'host': '127.0.0.1:8002', 'connection': 'keep-alive', 'sec-ch-ua': '\"Microsoft Edge\";v=\"119\", \"Chromium\";v=\"119\", \"Not?A_Brand\";v=\"24\"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '\"Windows\"', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.0.0', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'})",
        "body": "None",
        "message": "hello world"
    }
    ```
3. 启用token认证  
   如果要给函数启用token认证，可在函数的参数定义中添加 verify_token=True ，并使用 token_in_url 或 token_in_header 参数变量来传递token密钥。参数变量的使用，请往下看
   
## 四、可通过 url 传递的参数变量，以及如何在你要定义的函数中获取
1. fn  
   前端传递方法，url中添加：fn=m003_ex/hello_world.py  
   函数中如何获取(在参数值声明fn即可)：
   ```python
   def hello_world(verify_token=False, fn:str) {
    return fn
   }
   ```
2. url的请求路径  
   例如上面示例的 url 中指定了路径 /0/a00  
   函数中获取（参数值声明full_path 或 sub_path 即可,一个是绝对路径，一个是相对路径）：
   ```python
   def hello_world(verify_token=False, full_path:str, sub_path:str) {
    return {full_path,sub_path}
   }
   ```
3. args_in_url  
   前端传递方法，url中添加：args_in_url=balabalabulubiubulubiu……  
   函数中获取方法(在参数值声明args_in_url)：
   ```python
   def hello_world(verify_token=False, args_in_url:str) {
    return args_in_url
   }
   ```
4. token_in_url
   前端传递方法，url中添加：token_in_url=balabalabulubiubulubiu……  
   函数中获取方法(在参数值声明token_in_url)：
   ```python
   def hello_world(verify_token=False, token_in_url:str) {
    return token_in_url
   }
   ```

## 五、可通过 header 或 body 传递的参数变量  
1. args_in_header  
   前端在http请求头中添加 args_in_header 的赋值  
   函数获取(在参数值声明 args_in_header 即可)：
   ```python
   def hello_world(verify_token=False, args_in_header:str) {
    return args_in_header
   }
   ```
2. token_in_header  
   前端在http请求头中添加 token_in_header 的赋值  
   函数获取(在参数值声明 token_in_header 即可)：
   ```python
   def hello_world(verify_token=False, token_in_header:str) {
    return token_in_header
   }
   ```
3. file  
   前端如何上传的文件  （不好意思，我也还在学）  
   后端函数获取(在参数值声明 temp_file_path 即可，已上传的文件在后端的临时路径)：
   ```python
   def hello_world(verify_token=False, temp_file_path:str) {
    return temp_file_path
   }
   ```





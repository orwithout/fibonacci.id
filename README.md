# senseVine 项目说明

查看： 设计文档 （正在准备中）




## 一、演示
**DEMO** v0.0.1: http://fibonacci.id （正在准备中）


## 二、开发环境设定

1. 克隆项目  
    项目源代码可以直接下载然后解压：https://github.com/orwithout/fibonacci.id/archive/refs/heads/main.zip  
    如果想要使用git 克隆，需要先安装git软件（下载: https://git-scm.com/downloads ），然后打开电脑系统的命令终端，运行(它会把源代码下载到当前命令终端的工作目录)：
    ```bash
    git clone https://www.github.com/orwithout/fibonacci.id.git
    ```



2. 安装 Python 环境  
    Windows 系统 安装方法（记得在安装过程中选上“Add Python 3.x to PATH”。如果忘记了，则卸载并再次安装）：https://docs.python.org/zh-cn/3.13/using/windows.html  
    Linux 系统 安装方法：[https://docs.python.org/zh-cn/3.13/using/unix.html](https://docs.python.org/zh-cn/3.13/using/unix.html)
   
3. 导航到解压或克隆下来的 `fibonacci.id` 目录：
    ```bash
    cd fibonacci.id
    ```
4. 安装依赖：
    ```bash
    pip install -r requirements.txt
    ```
5. 启动：
    ```bash
    # windows 系统 执行：
    start.cmd
    # Linux系统 执行：
    start.sh
    ```
- **[fastapi入门参考](https://fastapi.tiangolo.com/zh/#:~:text=%E8%B4%9F%E8%B4%A3%E6%95%B0%E6%8D%AE%E9%83%A8%E5%88%86%E3%80%82-,%E5%AE%89%E8%A3%85,-%C2%B6)**
- **[FastAPI 官方文档](https://fastapi.tiangolo.com/zh/)**
- **[git克隆github项目方法的更多说明](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)**

### 附：
1. [后台运行 Systemd守护配置](https://github.com/orwithout/fibonacci.id/blob/main/README.systemd.md)
2. [Nginx配置](https://github.com/orwithout/fibonacci.id/blob/main/README.nginx.md)






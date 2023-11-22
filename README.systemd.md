# Systemd 启动使用说明

- 后端svd.py 的systemd 启动模板 ：

    ```
    [Unit]
    Description=senseVine-backend
    After=network.target

    [Service]
    Type=simple
    User=User1
    Group=User1
    WorkingDirectory=/home/mian/fibonacci.id/
    ExecStart=/home/mian/.local/bin/uvicorn main.main:app --port 8002
    ExecReload=/bin/kill -HUP ${MAINPID}
    RestartSec=1
    Restart=always


    [Install]
    WantedBy=multi-user.target
    ```


1. **编辑其中 `WorkingDirectory、User、Group、ExecStart`字段**: 确保都设置为您的工作目录或用户。
2. **保存为 `/etc/systemd/system/fibonacci.id.service`**

## 基础命令

- **启动服务**
    ```bash
    sudo systemctl start fibonacci.id.service
    ```
    使用此命令启动名为 `fibonacci.id.service` 的 systemd 服务。

- **设置开机自启**
    ```bash
    sudo systemctl enable fibonacci.id.service
    ```
    使用此命令将 `fibonacci.id.service` 设置为开机自启动。

- **查看服务状态**
    ```bash
    sudo systemctl status fibonacci.id.service
    ```
    使用此命令可以查看 `fibonacci.id.service` 的运行状态信息。

## 复合命令

- **一键操作**
    ```bash
    sudo cp fibonacci.id.service /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl start fibonacci.id.service ;sudo systemctl status fibonacci.id.service
    ```
    这是一个复合命令，用于一次性执行多个操作：复制服务文件、重新加载 systemd、启动服务，并查看其状态。

## 其他命令

- **重新加载 systemd**
    ```bash
    sudo systemctl daemon-reload
    ```
    当你修改了 systemd 的服务定义文件后，使用此命令使改动生效。

- **查看最近的 50 条日志**
    ```bash
    journalctl -u fibonacci.id.service -n 50
    ```
    使用此命令可以查看 `fibonacci.id.service` 的最近 50 条日志。

- **查看最近 10 分钟的日志**
    ```bash
    journalctl -u fibonacci.id.service --since "10 minutes ago"
    ```
    使用此命令查看过去 10 分钟内 `fibonacci.id.service` 的日志。

- **实时查看 Nginx 错误日志**
    ```bash
    sudo tail -f /var/log/nginx/error.log
    ```
    使用此命令可以实时查看 Nginx 的错误日志。

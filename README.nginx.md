
# Nginx 配置指南
请自行替配置文件中使用的域名 fibonacci.id 为你自己的域名，并设置A记录解析到你的主机服务器  
下面以配置 fibonacci.id 域名为例子
## 安装 Nginx

### Ubuntu

```bash
sudo apt update
sudo apt install nginx
```

## 启动和停止 Nginx

启动 Nginx：

```bash
sudo systemctl start nginx
```

停止 Nginx：

```bash
sudo systemctl stop nginx
```


## 配置虚拟主机

在 `/etc/nginx/sites-available/` 目录下创建一个新的配置文件，例如 `fibonacci.id`：

```bash
sudo nano /etc/nginx/sites-available/fibonacci.id
```

然后将以下内容粘贴到该文件中：

```nginx
server {
    listen 80;
    server_name fibonacci.id; //实际部署时，无比将 fibonacci.id 改为你的域名

    location / {
        proxy_pass http://localhost:8002;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

保存并退出编辑器。

接下来，创建一个软链接到 `/etc/nginx/sites-enabled/` 目录：

```bash
sudo ln -s /etc/nginx/sites-available/sensevine.com /etc/nginx/sites-enabled/
```

测试 Nginx 配置以确保没有语法错误：

```bash
sudo nginx -t
```

如果测试成功，重新加载 Nginx 以应用新的配置：

```bash
sudo systemctl reload nginx
```

现在，您应该可以通过访问 `http://fibonacci.id` 来看到相应的内容。  
（实际部署时，无比将 fibonacci.id 改为你的域名）


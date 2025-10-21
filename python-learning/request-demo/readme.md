# http测试工具：httpbin

## 用途：

httpbin.org 可以测试 HTTP 请求和响应的各种信息，比如 cookie、ip、headers 和登录验证等，且支持 GET、POST 等多种方法。对 web 开发和测试很有帮助。

简单来说就是可以用于查看我们发送的http请求信息。你需要查看请求中的哪一部分信息，就调用对应接口即可查看。


## 网站介绍

httpbin 是一个使用 Python + Flask 编写的 HTTP HTTP Request & Response Service。，是一个开源项目。

主要用于测试 HTTP 库。

你可以向他发送请求，然后他会按照指定的规则将你的请求返回。

httpbin支持HTTP/HTTPS，支持所有的HTTP动词，能模拟302跳转乃至302跳转的次数，还可以返回一个HTML文件或一个XML文件或一个图片文件（还支持指定返回图片的格式）。


## Httpbin访问方式

Httpbin的使用方法非常简单，你只需要把请求的地址修改为httpbin.org即可。

例如GET请求：http://httpbin.org/get。

如果使用本地部署 (本地部署请接着往下看) 的Httpbin服务，访问：http://127.0.0.1:[自己设置的端口号]/请求路径

页面中每个选项都可以点开，里边有对应的接口说明。
Httpbin接口调试


## 常用接口地址：

    get请求网址：https://httpbin.org/get
    post请求网址：https://httpbin.org/post
    put请求网址：https://httpbin.org/put
    patch请求网址：https://httpbin.org/patch
    delete请求网址：https://httpbin.org/delete
    返回headers信息：https://httpbin.org/headers
    返回你使用的访问此链接的IP地址：https://httpbin.org/ip
    返回USER-AGENT信息：https://httpbin.org/user-agent


## 在Linux系统中部署Httpbin服务

Linux系统中我们通常使用Docker的方式部署Httpbin服务，这样非常的方便简单。

一共只有两步就可以完成：

第一，拉取镜像；

第二，启动镜像。

### （1）拉取Httpbin服务的Docker镜像到本地

    [root@localhost ~]# docker pull kennethreitz/httpbin
    Using default tag: latest
    latest: Pulling from kennethreitz/httpbin
    473ede7ed136: Pull complete
    c46b5fa4d940: Pull complete
    93ae3df89c92: Pull complete
    6b1eed27cade: Pull complete
    0373952b589d: Pull complete
    7b82cd0ee527: Pull complete
    a36b2d884a89: Pull complete
    Digest: sha256:599fe5e5073102dbb0ee3dbb65f049dab44fa9fc251f6835c9990f8fb196a72b
    Status: Downloaded newer image for kennethreitz/httpbin:latest
    docker.io/kennethreitz/httpbin:latest

### （2）启动本地Httpbin服务的Docker镜像

    [root@localhost ~]# docker run -p 80:80 kennethreitz/httpbin
    [2021-05-20 02:13:00 +0000] [1] [INFO] Starting gunicorn 19.9.0
    [2021-05-20 02:13:00 +0000] [1] [INFO] Listening at: http://0.0.0.0:80 (1)
    [2021-05-20 02:13:00 +0000] [1] [INFO] Using worker: gevent
    [2021-05-20 02:13:00 +0000] [9] [INFO] Booting worker with pid: 9

当然我们可以后台运行Docker镜像，执行命令：docker run -d -p 9999:80 kennethreitz/httpbin。

### （3）浏览器中访问本地Httpbin服务

192.168.134.129为Linux服务器或者虚拟机的地址。

这样我们就可以在本地使用Httpbin接口服务了，速度会非常的快。

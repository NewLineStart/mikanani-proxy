# 蜜柑计划 RSS 代理服务器

悲报！被墙了！所以这里是解决方案。【轻量到我甚至不想写配置文件】

## 使用方法

1. 编辑 `main.py`
   - `host_name`: 对外暴露的域名或者 IP(取决于你的run_host的ip:run_port的端口，有域名就直接域名)，
   - `proxy_ip`: 梯子的代理地址(建议直接内网ip)，
   - `mikan_token`: 蜜柑计划的 RSS Token，看一眼你的 RSS URL 就知道了。
   - `user_token`: 设一个你自己的 Token，用于验证身份。
   - `run_host`: Host IP（不知道这个是什么意思的就别动）。
   - `run_port`: 端口
   
2. 运行

   **宿主机**

   ```bash
   python main.py
   ```

   **docker**

   ```bash
   docker run -itd --name=mikanani-proxy \
           -p 9115:9115 \
           -e host_name='http://xxx' \
           -e proxy_ip='http://xxx' \
           -e mikan_token='' \
           -e user_token='' \
   miraclemie/mikanani-proxy:latest
   ```

   

3. torrent 下载器的 RSS 如下配置：
   ```
   http(s)://内网ip:9115/?token=<user_token>
   ```

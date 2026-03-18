from wecom_notify import WechatWork

corpid = "ww9509b70b32dc272b"
appid = "1000003"
corpsecret = "A0JWQe8NDavETG6ybEO6sUdnaKcquhlsXQrMU8ujVbc"
users = ["HuangHongZhe"]
w = WechatWork(corpid=corpid, appid=appid, corpsecret=corpsecret)
# 发送文本
res = w.send_text("Hello World!", users)
print(res)

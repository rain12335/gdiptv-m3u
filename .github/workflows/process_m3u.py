import requests

url = "https://raw.githubusercontent.com/Tzwcard/ChinaTelecom-GuangdongIPTV-RTP-List/refs/heads/master/GuangdongIPTV_rtp_hd.m3u"
replace_prefix = "http://192.168.9.133:7088/udp/"

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    content = response.text
    new_content = content.replace("rtp://", replace_prefix)

    with open("GuangdongIPTV_http.m3u", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("M3U 文件处理成功。")
except Exception as e:
    print("下载或处理出错：", str(e))

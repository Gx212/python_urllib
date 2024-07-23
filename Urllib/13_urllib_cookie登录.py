#使用cookie访问需要登录的网页（免登录）
import urllib.request

url = 'https://user.qzone.qq.com/3052007158'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    # 'Accept-Encoding': 'gzip, deflate, br, zstd',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Cache-Control': 'max-age=0',
    'Cookie': 'qq_domain_video_guid_verify=31437028209f66c1; _qimei_uuid42=1851917030710095507cfa18116d19eccdf4a3ed3f; pgv_pvid=3339838308; _qimei_q36=; _qimei_h38=19c53a3f507cfa18116d19ec02000008f18519; RK=fR39qAfy5c; ptcz=728010bb24331a906ded393c4bf7c460dacc3cb108030534f2a85826805c855c; tvfe_boss_uuid=d0e376ea33ad98e5; pac_uid=0_XR1Yjrtj18Ces; suid=0_XR1Yjrtj18Ces; o_cookie=3052007158; _qimei_fingerprint=f7b6194c7aec29ed5a7d663cd745c0e5; _qpsvr_localtk=0.8801233730698497; pgv_info=ssid=s8643116704; uin=o3052007158; skey=@aq5ufFGLk; p_uin=o3052007158; pt4_token=ZsMo-BLCmUq3lPCK76kj3aE6kK7QmdLluwJrmVbi3B0_; p_skey=-h2t*mvjQSZDgY89V7TQ2u6g91f*XLm*PPmMzQdqZV8_; Loading=Yes; qz_screen=1707x1067; 3052007158_todaycount=0; 3052007158_totalcount=2350; QZ_FE_WEBP_SUPPORT=1; cpu_performance_v8=0; __Q_w_s__QZN_TodoMsgCnt=1',
    'If-Modified-Since': 'Fri, 19 Jul 2024 10:01:53 GMT',
    'Priority': 'u=0, i',
    'Referer': 'https://qzs.qq.com/',
    'Sec-Ch-Ua': '"Not/A)Brand";v="8", "Chromium";v="126", "Google Chrome";v="126"',
    'Sec-Ch-Ua-Mobile': '?0',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-site',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'
}
request = urllib.request.Request(url = url,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

with open('qq.html','w',encoding='utf-8') as fp:
    fp.write(content)
print("爬取完成")

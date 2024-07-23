import urllib.request
import datetime

"""下载气象数据"""
start_date = datetime.date(2011, 5, 5)  # 开始日期
end_date = datetime.date(2011, 5, 31)

data = start_date
while data <= end_date:
    data_now = data.strftime("%Y-%m-%d")
    url = f"https://ncss.hycom.org/thredds/ncss/GLBv0.08/expt_53.X/data/2011?var=water_u&var=water_v&north=60.0000&west=100.0000&east=180.0000&south=00.0000&disableProjSubset=on&horizStride=1&time={data_now}T21%3A00%3A00Z&vertStride=4&accept=netcdf4"
    save_path = f"D:/4、智能感知与预警/HY COM/{data_now}.nc4"
    urllib.request.urlretrieve(url,save_path)
    print(f"下载完成{data_now}")
    data += datetime.timedelta(days=1)

print("下载完成")

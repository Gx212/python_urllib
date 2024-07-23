import json

#将11爬取的json数据进行提取

input_filename = 'kfc_1.json'
output_filename = 'kfc_store_name_address.txt'

#加载json数据
with open(input_filename,'r',encoding='utf-8') as json_file:
    data = json.load(json_file)

if "Table1" in data and isinstance(data["Table1"],list):
    with open(output_filename,'w') as txt_file:
        for item in data["Table1"]:
            store_name = item.get('storeName', '')#字典中不存在这个值就返回第二个参数
            store_address = item.get('addressDetail', '')
            txt_file.write(f"{store_name},{store_address}\n")
    print("转换完成")
else:
    print("JSON格式不是预期的列表")
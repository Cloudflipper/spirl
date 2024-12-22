import pandas as pd
import numpy as np
 # 用于安全地解析字符串为 Python 对象

def parse_state(column):
    import ast 
    parsed = []  # 存储解析结果
    for item in column:
        try:
            # 对 item 进行预处理和修改
            item = item.replace("\n", "").strip()  # 去掉换行符和首尾空格
            item = item.replace("     ", ",")
            item = item.replace("    ", ",")
            item = item.replace("   ", ",")
            item = item.replace("  ", ",")
            item = item.replace(" ", ",")
            item = item.replace("[,", "[")
            item = item.replace(",]", "]")
            item = item.replace(",,", ",")
            # 解析字符串为数组
            parsed_item = np.array(ast.literal_eval(item), dtype=np.float32)
            parsed.append(parsed_item)  # 将解析结果加入列表
        except Exception as e:
            print(f"Error parsing item: {item} -> {e}")  # 打印错误信息
            parsed.append(np.zeros(1, dtype=np.float32))  # 填充默认值
    return np.array(parsed)

def parse_array_column(column):
    import ast 
    parsed = []  # 存储解析结果
    for item in column:
        try:
            # 对 item 进行预处理和修改
            item = item.replace("\n", "").strip()  # 去掉换行符和首尾空格
            
            # 解析字符串为数组
            parsed_item = np.array(ast.literal_eval(item), dtype=np.float32)
            parsed.append(parsed_item)  # 将解析结果加入列表
        except Exception as e:
            print(f"Error parsing item: {item} -> {e}")  # 打印错误信息
            parsed.append(np.zeros(1, dtype=np.float32))  # 填充默认值
    return np.array(parsed)

def excel_parse(file_path):
    
    
    data = pd.read_csv(file_path)

    actions = parse_state(data['action'])   # 假设前100列是 'actions'
    infos = data['info'].to_numpy(dtype=np.int32)          # 假设有一列 'infos'
    observations = parse_state(data['state'])   # 假设接下来100列是 'observations'
    rewards = data['reward'].to_numpy(dtype=np.float32)    # 假设有一列 'rewards'
    terminals =  (data['done'] == 1) | (data['done'] == True) |   (data['done'] == 'true') |   (data['done'] == 'True')      # 假设有一列 'terminals'

    for i in range(len(infos)-1):
        if terminals[i]==True and terminals[i+1]==True:
            terminals[i]==False

    # 组织成目标数据结构
    result = {
        'actions': actions,
        'infos': infos,
        'observations': observations,
        'rewards': rewards,
        'terminals': terminals,
        'timeouts': terminals
    }
    return result

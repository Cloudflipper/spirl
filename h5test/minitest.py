import h5py
import pandas as pd
import os

def h5_to_csv(h5_file_path, output_dir):
    # 打开HDF5文件
    with h5py.File(h5_file_path, 'r') as f:
        # 遍历HDF5文件中的每个数据集
        for name in f:
            if isinstance(f[name], h5py.Dataset):  # 仅处理数据集
                data = f[name][:]
                
                # 将数据集转换为DataFrame
                df = pd.DataFrame(data)
                
                # 保存为CSV文件
                csv_file_path = os.path.join(output_dir, f"{name}.csv")
                df.to_csv(csv_file_path, index=False)
                print(f"Saved {name} to {csv_file_path}")

# 使用示例
h5_file_path = 'h5test/mini.hdf5'  # 替换为你的HDF5文件路径
output_dir = 'output_directory/'     # 替换为保存CSV文件的目录
os.makedirs(output_dir, exist_ok=True)  # 创建输出目录（如果不存在）
h5_to_csv(h5_file_path, output_dir)
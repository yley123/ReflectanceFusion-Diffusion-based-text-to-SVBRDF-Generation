import os

# 设置包含文件的目录
directory = './'

# 遍历目录中的所有文件
for filename in os.listdir(directory):
    if filename.startswith('of_'):
        # 构造旧文件完整路径
        old_path = os.path.join(directory, filename)
        
        # 移除 'of_' 并添加 '.png' 后缀
        new_filename = filename[3:] + '.png'
        new_path = os.path.join(directory, new_filename)
        
        # 重命名文件
        os.rename(old_path, new_path)
        print(f'Renamed "{old_path}" to "{new_path}"')

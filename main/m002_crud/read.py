# import os

# def read(verify_token=False, full_path="", sub_path=""):  
#     try:
#         items = os.listdir(full_path)
#         return {f"{full_path}": items}
#     except Exception as e:
#         return {"error": str(e)}


# from pathlib import Path

# def read(verify_token=False, sub_path=""):  
#     path = Path(sub_path)
#     return [str(p) for p in path.rglob('*')]




# from pathlib import Path

# def read(verify_token=False, sub_path=""):
#     path = Path(sub_path)
#     return [p.as_posix() for p in path.rglob('*')]


from pathlib import Path

def read(verify_token=False, sub_path=""):
    path = Path(sub_path)
    # 包括文件和目录，但不包括sub_path本身
    return [p.relative_to(path).as_posix() for p in path.rglob('*')]

# import os

# def read(verify_token=False, full_path="", sub_path=""):  
#     tree = {}

#     for item in os.listdir(full_path):
#         path = os.path.join(full_path, item)
#         if os.path.isdir(path):
#             # 如果是目录，则递归读取该目录
#             tree[item] = read(path)
#         else:
#             # 如果是文件，只记录文件名
#             tree[item] = None

#     return tree


# import os
# from datetime import datetime

# def read(verify_token=False, full_path="", sub_path=""):
#     directory_contents = []
#     for root, dirs, files in os.walk(full_path):
#         for name in files:
#             file_path = os.path.join(root, name)
#             try:
#                 size = os.path.getsize(file_path)
#                 modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
#                 directory_contents.append({
#                     "type": "file",
#                     "name": name,
#                     "path": file_path,
#                     "size": size,
#                     "modification_time": modification_time
#                 })
#             except OSError as e:
#                 directory_contents.append({
#                     "type": "file",
#                     "name": name,
#                     "path": file_path,
#                     "error": str(e)
#                 })
#         for name in dirs:
#             dir_path = os.path.join(root, name)
#             try:
#                 modification_time = datetime.fromtimestamp(os.path.getmtime(dir_path)).isoformat()
#                 directory_contents.append({
#                     "type": "directory",
#                     "name": name,
#                     "path": dir_path,
#                     "modification_time": modification_time
#                 })
#             except OSError as e:
#                 directory_contents.append({
#                     "type": "directory",
#                     "name": name,
#                     "path": dir_path,
#                     "error": str(e)
#                 })
#     return directory_contents


# import os
# from datetime import datetime

# def read(verify_token=False, full_path="", sub_path=""):
#     directory_tree = {}

#     for root, dirs, files in os.walk(full_path):
#         # 构建从root到当前目录的路径
#         parts = root.split(os.sep)
#         subdir = directory_tree
#         for part in parts:
#             subdir = subdir.setdefault(part or '.', {})

#         # 添加文件信息
#         for file_name in files:
#             file_path = os.path.join(root, file_name)
#             size = os.path.getsize(file_path)
#             modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
#             subdir[file_name] = {"size": size, "modification_time": modification_time}

#         # 为子目录预留空间
#         for dir_name in dirs:
#             subdir.setdefault(dir_name, {})

#     return directory_tree



# import os
# from datetime import datetime


# def read(verify_token=False, full_path="", sub_path=""):
#     """
#     Build a directory structure with files including size and modification date.
#     """
#     directory_structure = {}

#     for root, dirs, files in os.walk(full_path):
#         # Extract the subpath we are looking at, relative to the rootdir
#         subpath = os.path.relpath(root, full_path)
#         if subpath == ".":
#             subpath = ""

#         # Navigate or create the structure in the dictionary
#         pointer = directory_structure
#         if subpath != "":
#             for part in subpath.split(os.sep):
#                 pointer = pointer.setdefault(part, {})

#         # Add files with size and modification date to the current pointer
#         for f in files:
#             file_path = os.path.join(root, f)
#             try:
#                 size = os.path.getsize(file_path)
#                 modification_time = datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()
#                 pointer[f] = {"size": size, "modification_time": modification_time}
#             except OSError as e:
#                 pointer[f] = {"error": str(e)}

#         # Initialize subdirectories
#         for d in dirs:
#             pointer.setdefault(d, {})

#     return directory_structure


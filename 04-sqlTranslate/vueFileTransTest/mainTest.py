import re
import os

messages = [
    # '修改成功', 'Successfully edited',
    # '新增成功', 'Successfully added',
    # '删除成功', 'Successfully deleted',
    # '是否确认删除', 'Confirm delete ',
    # '不能为空', 'can\'t be blank',
    # '请输入', 'Enter',
    # '搜索', 'Search',
    # '重置', 'Reset',
    # '新增', 'Add',
    # '修改', 'Edit',
    # '删除', 'Delete',
    # '导出', 'Export',
    # '关闭', 'Cancel',
    # '备注', 'Description',
    # '创建时间', 'Creation Date',
    '开始日期', 'Start Date',
    '结束日期', 'End Date',
    '内存','Memory',
    '用户', 'User ',
    '手机号码','Phone Number',
    '导入','Import',
    '部门','Department ',
    '角色', 'Role ',
    '编号', 'Number',
    '展开/折叠', 'Expand/collapse',
    '图标','Icon',
    '排序','Order',
    '路径','Path',
    '菜单','Menu ',
    '岗位','Position ',
    '刷新缓存','Flush',
    '标题','Title',
    '类型', 'Type',
    '公告类型', 'Annoncement',
    '清空', 'Clear',
    '详细', 'Details',
    '登陆时间', 'Sign-in Date',
    '任务', 'Task',
    '日志', 'Log ',
    '更多', 'More',
    '用户名', 'User Name',
    '密码', 'Password',
    '磁盘', 'Disk',
    '缓存', 'Cache'
      
    # '状态', 'Status',
    # '操作', 'Action',
    # '确 定', 'Submit',
    # '取 消', 'Cancel',
    # '名称', ' Name '
]

# 创建空字典
translated_messages = {}

# 将每两个元素视为一组，分别作为键值对添加到字典中
def generateDict():
    for i in range(0, len(messages), 2):
        key = messages[i]
        value = messages[i+1]
        translated_messages[key] = value
    print('Dict generated: ' + str(translated_messages))

def replace_keys_in_file_simplified(file_path):
    print('Processing file: ' + file_path)
    with open(file_path, 'r+', encoding='utf-8') as file:
        lines = file.readlines()

        new_lines = []
        for line in lines:
            for key, value in translated_messages.items():
                # 简单文本替换，不考虑Vue模板语法
                line = line.replace(key, value)
            new_lines.append(line)

        # 将替换后的内容写回文件
        file.seek(0)
        file.writelines(new_lines)
        file.truncate()

# 其他代码保持不变...

def search_and_replace_in_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            if file_name.endswith('.vue'):
                file_path = os.path.join(root, file_name)
                replace_keys_in_file_simplified(file_path)

# 生成字典
generateDict()
# 开始递归处理所有.vue文件
search_and_replace_in_folder(
    '/Users/luoran/Workspace/01-java/02-ruoyi-vue/ruoyi-ui/src/views')


import os;


path = "/Users/luoran/Documents/01-course/01-aws/main/";
suffix = ".vtt";

def operFileName(file, subPath):
    print("开始处理次级文件:" + file);
    if (file.endswith(".vtt")):
        #设置旧文件名（就是路径+文件名）
        oldname = subPath + os.sep + file;   # os.sep添加系统分隔符
        #设置新文件名
        newname= subPath + os.sep + file.removesuffix(" Simplified Chinese.vtt") + suffix;
        
        os.rename(oldname,newname)   #用os模块中的rename方法对文件改名

        print(oldname,'======>',newname);

def operFileName(file, subPath):
    print("开始处理次级文件:" + file);
    if (file.endswith(".vtt")):
        #设置旧文件名（就是路径+文件名）
        oldname = subPath + os.sep + file;   # os.sep添加系统分隔符
        #设置新文件名
        newname= subPath + os.sep + file.replace(".vtt", "") + suffix;
        
        os.rename(oldname,newname)   #用os模块中的rename方法对文件改名

        print(oldname,'======>',newname);

fileList=os.listdir(path);

for file in fileList:
    print("开始处理文件夹:" + file);
    if (file.startswith(".DS_Store")):
        continue;
    subPath = path + file;
    subFileList=os.listdir(subPath);
    for subFile in subFileList:
        operFileName(subFile, subPath);

    

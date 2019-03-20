from conf.config import *
import re, os


def get_download_files(pattern=None, dir_path=None):
    '''
    获取浏览器下载一类文件
    :param pattern: 文件匹配规则,默认None ,目录下所有文件
    :param dir_path: 下载目录，默认是配置文件中的google的默认配置路径
    :return:
    '''
    if not dir_path:
        dir_path = os.path.join(BROWSER.get('google').get('download'), CURRENT_DATE)
    files = []
    for f in os.listdir(dir_path):
        if pattern is not None:
            result = re.search(r'' + pattern, os.path.splitext(f)[0])
            if result:
                files.append(os.path.basename(f).rstrip('.crdownload'))
        else:
            files.append(os.path.basename(f).rstrip('.crdownload'))
    return files


def is_files(directory, fileType):
    '''
    判断某类文件是否存在
    :param directory: 文件目录
    :param fileType:
    :return:
    '''
    flag = True
    if isinstance(directory, list):
        for d in directory:
            if os.path.splitext(d)[1] == '.' + fileType:
                flag = flag & True
            else:
                flag = False
    else:
        flag = False
    return flag


def set_timer(is_end=False):
    '''
    计数器，用于记录下载的页面次数
    :param times: 默认是1， 下载完是-1
    :return:
    '''
    if is_end:
        times = -1
    else:
        times = get_next_timer()
    with open(os.path.join(os.getcwd(), SINGLE_PATH), 'w') as f:
        f.write(str(times))

def get_timer():
    with open(os.path.join(os.getcwd(), SINGLE_PATH), 'r') as f:
        content = f.readline()
    if not content:
        content = 0
    return int(content)

def get_next_timer():
    current_timer = get_timer()
    if not current_timer or current_timer == IS_END:
        new_timer = 1
    else:
        new_timer = int(current_timer) + 1
    return new_timer
import jieba
from collections import defaultdict

def read_file(file_path):
    """读取文本文件，返回字符串内容（处理编码异常）"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read().strip()
    except UnicodeDecodeError:
        # 兼容GBK编码文件（避免部分测试用例因编码报错）
        with open(file_path, 'r', encoding='gbk', errors='ignore') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"错误：文件{file_path}不存在")

def clean_text(text):
    """清洗文本：去除标点、特殊字符，转为小写（统一格式）"""
    import re
    # 保留中文、字母、数字，其他字符替换为空格
    cleaned = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9\s]', ' ', text)
    # 多个空格合并为一个
    cleaned = re.sub(r'\s+', ' ', cleaned).strip()
    return cleaned.lower()

def text_to_vector(text):
    """将文本转为词频向量（key：词语，value：出现次数）"""
    cleaned_text = clean_text(text)
    # 分词（使用jieba，需在requirements.txt中添加jieba）
    words = jieba.lcut(cleaned_text)
    # 过滤停用词（可选但推荐，提升准确性，需准备stopwords.txt）
    stopwords = set()
    try:
        with open('utils/stopwords.txt', 'r', encoding='utf-8') as f:
            stopwords = set(f.read().splitlines())
    except FileNotFoundError:
        # 若没有停用词文件，跳过过滤（避免程序崩溃）
        pass
    # 生成词频向量
    vector = defaultdict(int)
    for word in words:
        if word not in stopwords and len(word) > 1:  # 过滤单字和停用词
            vector[word] += 1
    return vector

import math

def cosine_similarity(vec1, vec2):
    """计算两个词频向量的余弦相似度，返回0-1之间的浮点数"""
    # 1. 提取所有不重复的词语
    all_words = set(vec1.keys()).union(set(vec2.keys()))
    # 2. 计算向量点积
    dot_product = 0.0
    for word in all_words:
        dot_product += vec1.get(word, 0) * vec2.get(word, 0)
    # 3. 计算两个向量的模长
    def vector_norm(vec):
        return math.sqrt(sum([val ** 2 for val in vec.values()]))
    norm1 = vector_norm(vec1)
    norm2 = vector_norm(vec2)
    # 4. 处理特殊情况（空向量）
    if norm1 == 0 or norm2 == 0:
        return 0.0  # 两个空文本或一个空文本，相似度为0
    # 5. 计算余弦相似度
    return dot_product / (norm1 * norm2)

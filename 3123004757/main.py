import sys
from utils.text_processor import read_file, text_to_vector
from utils.similarity_calculator import cosine_similarity

def main():
    # 1. 检查命令行参数数量（需传入3个文件路径）
    if len(sys.argv) != 4:
        print("错误：参数数量不足！正确格式：python main.py [原文路径] [抄袭版路径] [答案路径]")
        sys.exit(1)  # 异常退出，返回非0状态码
    
    # 2. 提取参数
    orig_path = sys.argv[1]
    plag_path = sys.argv[2]
    ans_path = sys.argv[3]
    
    try:
        # 3. 读取文本并转为向量
        orig_text = read_file(orig_path)
        plag_text = read_file(plag_path)
        orig_vec = text_to_vector(orig_text)
        plag_vec = text_to_vector(plag_text)
        
        # 4. 计算相似度并保留两位小数
        similarity = cosine_similarity(orig_vec, plag_vec)
        result = round(similarity, 2)  # 直接四舍五入，满足“精确到小数点后两位”要求
        
        # 5. 写入答案文件
        with open(ans_path, 'w', encoding='utf-8') as f:
            f.write(f"{result:.2f}")  # 格式化为两位小数（如0.85、1.00）
        
        print(f"成功：相似度已写入{ans_path}，结果为{result:.2f}")
    
    except Exception as e:
        # 捕获所有异常并提示（避免程序崩溃无反馈）
        print(f"执行错误：{str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()

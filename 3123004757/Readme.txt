3123004757 is my Student number, This is my homework, as you see

If you run the code in PyCharm, you can enter a word that 
cd UseTree-main
cd 3123004757
python main.py test case/orig.txt test case/orig add.txt test case/ans.txt in the command line

output:
st_case/orig_add.txt test_case/ans.txt
Building prefix dict from the default dictionary ...
Dumping model to file cache C:\Users\tree\AppData\Local\Temp\jieba.cache
Loading model cost 0.700 seconds.
Prefix dict has been built successfully.
成功：相似度已写入test_case/ans.txt，结果为0.71

[3123004757]/
├── main.py          # 程序主入口（必须命名，处理命令行参数、流程调度）
├── requirements.txt # Python依赖清单（记录第三方库：分词库jieba）
├── test.py          # 单元测试文件
├── test_cases/      # 测试用例文件夹（存放原文、抄袭版文件，方便测试）
│   ├── orig.txt     # 示例原文
│   ├── orig_add.txt # 示例抄袭版
│   └── empty.txt    # 空文件
└── utils/           # 工具函数文件夹
    ├── text_processor.py # 文本预处理模块
    ├── stopwords.txt # 从网上下载标准中文停用词表
    └── similarity_calculator.py # 相似度计算模块（余弦相似度核心）

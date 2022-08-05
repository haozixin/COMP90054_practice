# New python code style/skills/idea summary

1. 
        # enumerate 的使用
        for idx, instance in enumerate(features):
             numeric_features[idx].append(num_feat_values[idx])
        
        # 上面两行等效于
        for i in range(len(features)):
            numeric_features[i].append(num_feat_values[i])
2.  
        # 打印嵌套列表比如 [[],[],[],[]] 的数据
        方法一:
           for i in numeric_features:
               print('{}\t{}\t{}\t{}'.format(i[0], i[1], i[2], i[3]))
        方法二:
           for i in features:
               print('\t'.join(i))  # Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'
3.      
        # 这种写法能省下好多for 循环
        # initialize our new structure to hold the numeric features
        # features 是嵌套列表 [[],[],[],[]]
        numeric_features = [[] for i in features]
        # [] for i ... 中的[] 能换成别的，代表每次循环后放到最外层[]中的元素
4.      
        # lambda 表达式
        x = lambda a, b : a * b
        print(x(5, 6))
         # result = 30
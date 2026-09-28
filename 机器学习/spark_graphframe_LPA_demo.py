# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from graphframes import *
spark = SparkSession.builder \
        .appName("commdty_cluster") \
        .config("spark.sql.broadcastTimeout", 20 * 60) \
        .config("spark.sql.crossJoin.enabled", True) \
        .config("odps.exec.dynamic.partition.mode", "nonstrict") \
        .config("spark.sql.codegen.wholeStage", False) \
        .getOrCreate()

# 获取日期参数
bizdate = sys.argv[1]

# 通过SQL读取边表到dataframe，必须包含：src，dst。
# 由于graphframe 的LPA不会参考权重，因此如果要带权重则需要多条边，即：不进行聚合
edgesDF = spark.sql(f"""
SELECT  src
        ,dst
        ,weight
FROM    (
            SELECT  start_uid AS src
                    ,end_uid AS dst
                    ,COUNT(DISTINCT edge_value) AS weight
            FROM    merchant_rank.dw_risk_model_merchant_cluster_edge_detail_v1_df
            WHERE   pt = '{bizdate}'
            GROUP BY start_uid
                     ,end_uid
        ) 
WHERE   src < dst
""")

# 节点表，必须包含：id列
verticesDF = spark.sql(f"""
SELECT  DISTINCT start_uid AS id
FROM    merchant_rank.dw_risk_model_merchant_cluster_edge_detail_v1_df
WHERE   pt = '{bizdate}'
""")

# 构图
g = GraphFrame(verticesDF, edgesDF)


# graphframes 的LPA算法不考虑边的权重，因此如果要考虑连接的频次，可以将原始边信息作为输入，而不要聚合成权重
# 阿里云 PAI 平台LPA算子实现了考虑权重的LPA算法。
lpaGraph = g.labelPropagation(maxIter=30)


# 执行完LPA之后，会对节点dataframe新增一列：label
resultDF = lpaGraph.select("id", "label")

resultDF.write.mode("overwrite").saveAsTable("du_risk_algo_dev.tmp_merchant_cluster_demo_20241229")

spark.stop()


"""
同时spark任务配置参数：${bizdate}，调度参数  bizdate  $bizdate
参考du_risk_algo空间下， trade_cluster_test 任务
将pypi下载的包graphframes文件重命名为graphframes.zip，并上传为archieve文件
spark配置：
spark.executorEnv.PYTHONPATH = graphframes
spark.yarn.appMasterEnv.PYTHONPATH = graphframes
选择archives资源：graphframes.zip
联通子图新增节点列：'component'
"""





















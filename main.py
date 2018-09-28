
import ESIndexMapping as esim
import ProductIndexing as pi
import ESSearch as ess
import elasticsearch
from sklearn.externals import joblib

file_path = "/home/fani/Downloads/goods_dump.dat"
goods_list = joblib.load(file_path)

pi.SaveProductCategory(goods_list)

es_client = elasticsearch.Elasticsearch("localhost:9200")

index_name = "shopping"
type = "goods"

esim.CreateIndex(es_client,index_name)

esim.AddProperty(es_client, index_name, type, "pid", "long")
esim.AddProperty(es_client, index_name, type, "name", "text", True)
esim.AddProperty(es_client, index_name, type, "site_name", "text")
esim.AddProperty(es_client, index_name, type, "clickct", "integer")
esim.AddProperty(es_client, index_name, type, "query_click", "text")
esim.AddProperty(es_client, index_name, type, "cate1", "text")
esim.AddProperty(es_client, index_name, type, "cate2", "text")
esim.AddProperty(es_client, index_name, type, "cate3", "text")
esim.AddProperty(es_client, index_name, type, "img", "text")
esim.AddProperty(es_client, index_name, type, "review_num", "integer")
esim.AddProperty(es_client, index_name, type, "review_rate", "long")

pi.IndexProduct(es_client, index_name, type, goods_list)



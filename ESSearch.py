import elasticsearch
import json

#This function maps using keyword_dict
#Parameter:
#   index_name : name of index
#   type : name of type
#   keyword_dict : dictionary of goods
def search(ES, index_name, type, keyword_dict):

    bodydict = {
            'query': {
                "function_score" : {
                    "query" : {
                        "bool" : {
                            "must" : [
                            ]
                        },
                    },
                    "boost" : "1",
                    "functions" : [
                        {
                            "filter" : {
                                "bool" : {
                                    "must" : [

                                    ]
                                }
                            },
                            "weight" : 2
                        },
                        {
                            "field_value_factor": {
                                "field" : "clickct",
                                "factor" : 0.05,
                            },
                            "weight" : 1
                        }
                    ],
                    "score_mode" : "sum"
                }
            }
        }

    if "site_name" in list(keyword_dict.keys()):
        bodydict["query"]["function_score"]["query"]["bool"]["must"].append({"match": {"site_name": keyword_dict["site_name"]}})
        bodydict["query"]["function_score"]["functions"][0]["filter"]["bool"]["must"].append({"match": {"site_name": keyword_dict["site_name"]}})

    if "cate1" in list(keyword_dict.keys()):
        bodydict["query"]["function_score"]["query"]["bool"]["must"].append({"match": {"cate1": keyword_dict["cate1"]}})
        bodydict["query"]["function_score"]["functions"][0]["filter"]["bool"]["must"].append({"match": {"cate1": keyword_dict["cate1"]}})
        if "cate2" in list(keyword_dict.keys()):
            bodydict["query"]["function_score"]["query"]["bool"]["must"].append({"match": {"cate2": keyword_dict["cate2"]}})
            bodydict["query"]["function_score"]["functions"][0]["filter"]["bool"]["must"].append(
                {"match": {"cate2": keyword_dict["cate2"]}})
            if "cate3" in list(keyword_dict.keys()):
                bodydict["query"]["function_score"]["query"]["bool"]["must"].append({"match": {"cate3": keyword_dict["cate3"]}})
                bodydict["query"]["function_score"]["functions"][0]["filter"]["bool"]["must"].append(
                    {"match": {"cate3": keyword_dict["cate3"]}})

    if "keyword" in list(keyword_dict.keys()):
        bodydict["query"]["function_score"]["query"]["bool"]["must"].append({"match": {"name": keyword_dict["keyword"]}})
        bodydict["query"]["function_score"]["functions"][0]["filter"]["bool"]["must"].append(
            {"match": {"name": keyword_dict["keyword"]}})

    docs = ES.search(index=index_name, doc_type=type,body=bodydict)

    print(json.dumps(docs
                     ,ensure_ascii=False, indent=2))

#This function process keywords using Hangul morpheme anlyzer
#Parameter:
#   index_name : name of index
#   keyword : search word
def ProcessKeyword(ES, index_name, keyword):

    keywordlist = []
    reskey = ""

    res = elasticsearch.client.IndicesClient.analyze(ES, index=index_name, body = {
        "analyzer" : "korean",
        "text" : keyword
    })

    for element in res['tokens']:
        if element['type'] == "NNG" or element['type'] == "NNP":
            keyword = element['token']
            if not keyword in keywordlist:
                keywordlist.append(keyword)

    for key in keywordlist:
        reskey += key
        reskey += " "

    return reskey[:-1]




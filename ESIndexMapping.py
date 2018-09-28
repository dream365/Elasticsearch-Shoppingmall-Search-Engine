import elasticsearch

#This function creates index with korean morpheme analyzer
#Parameter:
#   index_name : name of index
def CreateIndex(ES, index_name):
    settings = {
        "settings" : {
            "index" : {
                "analysis" : {
                    "analyzer" : {
                        "korean" : {
                            "type" : "custom",
                            "tokenizer" : "seunjeon_default_tokenizer"
                        }
                    },
                    "tokenizer" : {
                        "seunjeon_default_tokenizer" : {
                            "type" : "mecab_ko_standard_tokenizer",
                            "mecab_args" : "/usr/local/lib/mecab/dic/mecab-ko-dic"
                        }
                    }
                }
            }
        }
    }

    response = elasticsearch.client.IndicesClient.create(ES, index=index_name, body=settings)

    if response["acknowledged"]:
        print("creates index successfully")
        print("index : %s" %index_name)

#This function add new property to a type
#Parameter:
#   index_name : name of index
#   type : name of type
#   property_name : name of property
#   property_type : type of property
#   isAnalized : Variable for application of Hangul morpheme analyzer
def AddProperty(ES, index_name, type, property_name, property_type, isAnalized=False):

    propertydict = {
        "properties": {
            property_name : {
                "type" : property_type
            }
        }
    }

    if isAnalized:
        propertydict["properties"][property_name]["analyzer"] = "korean"

    response = elasticsearch.client.IndicesClient.put_mapping(ES, index=index_name, doc_type= type, body = propertydict)

    if response["acknowledged"]:
        print("add new property successfully")
        print("property : %s, type : %s" % (property_name, property_type))


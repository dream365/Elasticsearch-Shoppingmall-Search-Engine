
#This function index whole of products
#Parameter:
#   index_name : name of index
#   type : name of type
#   product_list : list of goods
def IndexProduct(ES, index_name, type, product_list):

    for product in product_list:
        body_dict = dict()

        for k in product.keys():
            body_dict[k] = product[k]

        ES.create(index=index_name, doc_type=type, id=body_dict["pid"], body=body_dict)

#This function save products category in file
#Parameter:
#   product_list : list of goods
def SaveProductCategory(product_list):

    categorylist = []
    cnt = 0

    for product in product_list:
        cate1 = "cate1" + "," + product["cate1"]
        cate2 = "cate2" + "," + product["cate2"]
        cate3 = "cate3" + "," + product["cate3"]
        cnt += 1
        if cate1 in categorylist:
            if cate2 in categorylist:
                if not cate3 in categorylist:
                    idx = categorylist.index(cate2)
                    categorylist.insert(idx+1, cate3)
            else:
                idx = categorylist.index(cate1)
                categorylist.insert(idx + 1, cate2)
                categorylist.insert(idx + 2, cate3)
        else:
            categorylist.append(cate1)
            categorylist.append(cate2)
            categorylist.append(cate3)

        if cnt == 19410:
            break

    f = open('/home/fani/category.txt', 'w', encoding='utf8')
    for i in categorylist:
        f.write(i+"\n")






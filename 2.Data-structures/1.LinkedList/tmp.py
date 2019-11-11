# # Required Packages
#
# import pymongo
# import os
# import shutil
# import datetime
# import argparse
#
# # connect to mongodb
# myclient = pymongo.MongoClient('mongodb://localhost:27017/')
#
# # get all the database names
# dblist = myclient.list_database_names()
#
# # Get the DB
# mydb = myclient['flask']
#
#
# def PreTrainModelPropagation(cur_dataset_id,cur_premodel_id):
#
#
# def FetchDataSets():
#     get_all_datasets = mydb['dataset_model'].find({"pretrain_model" : { "$exists": True, "$not": {"$size": 0} }},{"pretrain_model":1,"categories":1})
#     for each_dataset in get_all_datasets:
#         cur_dataset_id = each_dataset['_id']
#         #Loop through each pre-train model
#         for each_pretrain in each_dataset['pretrain_model']:
#             # check whether the class name is present or not
#             dataset_categories = each_dataset['categories']
#             get_pretrain_mdl_category = mydb['pretrain_model'].find({"_id":each_pretrain})[0]['categories']
#             for each_pretrain_mdl_category in get_pretrain_mdl_category:
#                 if each_pretrain_mdl_category not in dataset_categories:
#                     #insert the category to the dataset
#                     dataset_categories.append(each_pretrain_mdl_category)
#             #update dataset categories
#             mydb['dataset_model'].update_one({"_id":cur_dataset_id},{"$set": {"categories":  dataset_categories} } )
#             #update the image categories also
#             cur_premodel_id = each_pretrain
#             PreTrainModelPropagation(cur_dataset_id,cur_premodel_id)
#
#
# if __name__ == '__main__':
#     # construct the argument parse and parse the arguments
#     FetchDataSets()
#


import subprocess
subprocess.run(['mkdir', "runMode"])
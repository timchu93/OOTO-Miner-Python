

# For loadVarDesc()
import json  # For pretty print
import collections
from csv import reader

# For loadDataset()
import pandas as pd

# For loadVarDesc()
ITEM_MARKER = "^"
FEAT_NAME = "Name"
OPTION_NAME = "OptionName"



# NOTE: Arrays start at 0
def loadVarDesc(path_variableDesc):
    dict_varDesc = collections.OrderedDict()

    # Open file in read mode
    with open(path_variableDesc, "r") as obj_varDesc:
        read_varDesc = reader(obj_varDesc)
        
        for row in read_varDesc:
            row_id = row[0].strip()

        
            # Create a new dict entry if you see the Item Marker (^)
            if row_id == ITEM_MARKER:
                
                feat_code = row[1].strip()
                feat_name = row[2].strip()
                
                item = collections.OrderedDict()  # The item values/options, i.e. 1, 2
                dict_option_names = collections.OrderedDict()  # The option names, i.e. "Mostly True"

                item[FEAT_NAME] = feat_name
                item[OPTION_NAME] = dict_option_names

                dict_varDesc[feat_code] = item

                # print(feat_code + " - " + feat_name)
                
            # If not New Entry, continue adding to Item
            else:
                feat_val = row[1].strip()  # Ex. In Gender, 1 or 2
                feat_eval = row[0].strip()  # Equivalent value (i.e. "a" or "b")
                item[feat_val] = feat_eval

                dict_option_names[feat_val] = row[2].strip()

        # printDictionary(dict_option_names)
    return dict_varDesc

'''
Loads the dataset and makes necessary replacements according
to the Variable Description File.
'''
def loadDataset(path_dataset, dict_varDesc):
    # Load file as dataframe
    df_dataset = pd.read_csv(path_dataset)
    printDictionary(dict_varDesc)
    # Replace each column value with their equivalent letter based on dict_varDesc (Variable Description File)
    for feat_code, feat_dict in dict_varDesc.items():
        item = dict_varDesc[feat_code]  # For each entry in dict_varDesc
        option_values = []  # Will hold the original option values in the dataset
        option_new_values = []  # Will hold the values to replace the options

        for item_code, item_value in item.items():  # Parse each key and value in that item
            if item_code != FEAT_NAME and item_code != OPTION_NAME:  # If the key does not contain "Name", replace the dataset values
                option_values.append(int(item_code))
                option_new_values.append(item[item_code])  # The value that the option should be. i.e "a"

        df_dataset[feat_code] = df_dataset[feat_code].replace(option_values, option_new_values)
        # df_dataset[key] = df_dataset[key].replace([1, 2], ["a", "b"])

    # print(df_dataset[key])

    return df_dataset


def exportDataset(df_dataset, filename, path):
    path_export = str(path + filename)
    df_dataset.to_csv(path_export, index = False, sep = ",")

def exportResultTable(df_results):
    print("Export Result Table")

def printDictionary(oDict):
    print(json.dumps(oDict, indent = 4))















        
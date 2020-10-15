import pprint
import itertools
import numpy as np
import copy
import time

import Filter_support as FILS
import ChiSquare_support as CHIS
import Loader_support as LS


'''
The main function to call.
Applies necessary functions to output a printable chi-square comparison table. 
'''
def crossProcess(df_dataset, np_CROSS):
    # Generate datasets as dictated by filters
    # NOTE:
    #   np_dataset_pairs[type]                      - A list of cross types
    #   np_dataset_pairs[type][level]               - A list of levels within the list of cross types
    #   np_dataset_pairs[type][level][0]            - A list of dataset pairs (list) within the list of levels
    #   np_dataset_pairs[0][0][0][0]                - The contents of the list containing the dataset pairs
    np_cross_datasets, np_cross_filters = extractDatasets(df_dataset, np_CROSS)  # TODO (Future) Try to optimize

    # print("")
    # print("")
    # print("")
    #
    # print(len(np_cross_datasets))  # Number of accepted features
    # print(type(np_cross_datasets))  # Number of accepted features
    # print("")
    #
    # print(len(np_cross_datasets[0]))  # Number of accepted features
    # print(type(np_cross_datasets[0]))  # Number of accepted features
    # print("")
    #
    # print(len(np_cross_datasets[0][0]))
    # print(type(np_cross_datasets[0][0]))
    # print("")
    #
    # print(len(np_cross_datasets[0][0][0]))
    # print(type(np_cross_datasets[0][0][0]))
    # print("")
    #
    # print(len(np_cross_datasets[0][0][0][0]))
    # print(type(np_cross_datasets[0][0][0][0]))
    # print("")




    start_time = time.time()

    len_cross_datasets = len(np_cross_datasets)
    # len_cross_types = 3  # len(cross_type)
    # len_cross_level = 3  # len(cross_level)
    list_chi_square_table = []
    list_chi_square_output = []


    # Apply Chi-square on all dataset pairs in the list np_dataset_pairs
    for i_cross_type in range(len_cross_datasets):  # TODO Find a good way to partition this
        cross_type = np_cross_datasets[i_cross_type]
        len_cross_types = len(cross_type)
        for i_cross_level in range(len_cross_types):  # The variable cross_level is the list of dataframes
            cross_level = cross_type[i_cross_level]
            len_cross_level = len(cross_level)
            # print("CROSS LEVEL")
            # print(type(cross_level))
            # print(len(cross_level))
            # print("")
            for i_dataset_pairs in range(len_cross_level):
                dataset_pairs = cross_level[i_dataset_pairs]
                len_dataset_pairs = len(dataset_pairs)
                for i_dataset_pair in range(len_dataset_pairs):
                    dataset_pair = dataset_pairs[i_dataset_pair]

                    dict_chi_square = CHIS.chiSquare(dataset_pair)
                    df_output = CHIS.processChiSquareTable(dict_chi_square)  # TODO Printing
                    if df_output is not None:
                        dataset_pair_filter = np_cross_filters[i_cross_type][i_cross_level][i_dataset_pairs]

                        # print("DATASET PAIR FILTER")
                        # print(dataset_pair_filter)
                        # print("")
                        np_dataset_pair_filter = np.array(dataset_pair_filter)

                        # list_chi_square_output.append([df_output, np_dataset_pair_filter])
                        list_index = [i_cross_type, i_cross_level]
                        # TODO Printing
                        LS.exportChiSquareTable(df_output, dataset_pair_filter, list_index)  # NOTE: Leave the brackets, it has to be within an array
                    else:
                        print("DF OUTPUT IS NULL: Skipping Item")

    print("--- %s seconds ---" % (time.time() - start_time))

    # CHIS.printTable(dict_chi_square)



def extractDatasets(df_dataset, np_CROSS):

    list_cross_type = []
    list_cross_type_filter = []

    # Filter datasets according to filters
    for np_cross_type in np_CROSS:  # np_cross_type[type] | Runs: 3; Per run length: 3

        list_level = []
        list_level_filter = []
        # np_cross_type[type][level] | Runs: 3; Per run length:
        # 1-[15, 66, 28] 2-[58, 276, 496] 3-[6, 6, 0]
        # Run length is the number of dataset pairs per level
        for np_level in np_cross_type:  # Runs: 3 per Cross Type

            list_pairs = []
            list_pairs_filter = []
            # [["b1:a", "b2:b"], ["u3:b", "b5:b]]
            # Runs: 1-[15, 66, 28] 2-[58, 276, 496] 3-[6, 6, 0];
            # Per run length: 2 (which is [filterA, filterB]
            for list_filter in np_level:
                df_filtered_dataset = df_dataset.copy(deep = True)  # TODO OPTIMIZE to proceed
                np_dataset_pair = FILS.applyFilter(df_filtered_dataset, list_filter)  # [datasetA, datasetB] | Length: 2

                # list_dataset_pairs.append(np_dataset_pair)
                list_pairs.append(np_dataset_pair)  # List of dataset pairs (list) in a level [ [datasetA, datasetB], [<...>] ]
                list_pairs_filter.append(list_filter)
            list_level.append(list_pairs)
            list_level_filter.append(list_pairs_filter)
        list_cross_type.append(list_level)  # List of levels (list) of dataset pairs
        list_cross_type_filter.append(list_level_filter)  # List of levels filters equivalent to list_cross_type


    np_list_cross_type = np.array(list_cross_type)
    # list_cross_type_filter = np.array(list_cross_type_filter)


    return np_list_cross_type, list_cross_type_filter









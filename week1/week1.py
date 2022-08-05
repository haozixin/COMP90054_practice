def string_feature_to_numeric_feature(str_values):
    str_value_set = list(set(str_values))  # create a set of all values in value_list
    numeric_values = []  # initialize our new value list
    for str_value in str_values:
        num_value = str_value_set.index(
            str_value)  # Python way of saying: 'give me the position of str_value in list of str_value_set'
        numeric_values.append(num_value)  # append the numeric value to the new value list
    return numeric_values  # return the new numeric values as an output of the function


if __name__ == "__main__":
    # v = ['a', 'b', 'c', 'a', 'a', 'b', 'd']
    # answer = string_feature_to_numeric_feature(v)
    # print(answer)

    features = [['sunny', 'hot', 'high', 'FALSE'], ['sunny', 'hot', 'high', 'TRUE'], ['overc', 'hot', 'high', 'FALSE'],
                ['rainy', 'mild', 'high', 'FALSE'], ['rainy', 'cool', 'normal', 'FALSE'],
                ['rainy', 'cool', 'normal', 'TRUE'], ['overc', 'cool', 'normal', 'TRUE'],
                ['sunny', 'mild', 'high', 'FALSE'], ['sunny', 'cool', 'normal', 'FALSE'],
                ['rainy', 'mild', 'normal', 'FALSE'], ['sunny', 'mild', 'normal', 'TRUE'],
                ['overc', 'mild', 'high', 'TRUE'], ['overc', 'hot', 'normal', 'FALSE'],
                ['rainy', 'mild', 'high', 'TRUE']]

    # print the original features
    print("This is our original feature matrix:")
    for i in features:
        print('\t'.join(i))  # Example: '.'.join(['ab', 'pq', 'rs']) -> 'ab.pq.rs'

    # initialize our new structure to hold the numeric features
    numeric_features = [[] for i in features]

    # iterate over each feature (i.e., over the columns of our data set) 取列
    for feature_idx in range(len(features[0])):
        # extract all values for that feature (i.e,. write all values in the nth column into a list)
        str_feat_values = [values[feature_idx] for values in features]
        # apply our function
        num_feat_values = string_feature_to_numeric_feature(str_feat_values)
        # write the new, numeric feature values into the numeric feature structure

        # for idx, instance in enumerate(features):
        #     numeric_features[idx].append(num_feat_values[idx])

        # 上面两行等效于
        for i in range(len(features)):
            numeric_features[i].append(num_feat_values[i])

    # print the new, numeric veatures
    print("\n\nThis is our new, numeric feature matrix:")
    for i in numeric_features:
        print('{}\t{}\t{}\t{}'.format(i[0], i[1], i[2], i[3]))

    # numeric_features = [i for i in features]
    # """
    # [i for i in features] is a list comprehension.
    # =
    # for i in features:
    # put i in the list(outside)
    # """
    # print(numeric_features)

# -*- coding: utf-8 -*-
# https://www.cnblogs.com/ModifyRong/p/7744987.html
# 定义训练数据
train_data = [
    [5.1,3.5,1.4,0.2],
    [4.9,3.0,1.4,0.2],
    [7.0,3.2,4.7,1.4],
    [6.4,3.2,4.5,1.5],
    [6.3,3.3,6.0,2.5],
    [5.8,2.7,5.1,1.9]]

# 定义label
label_data = [[1,0,0],
              [1,0,0],
              [0,1,0],
              [0,1,0],
              [0,0,1],
              [0,0,1]]

def findBestLossAndSplit(train_data,label_data,index):
    """
    实现整个找特征的过程 find best loss and split
    1）获得当前关注的这个类别对应的标签；
    2）遍历每一个特征，对于这个特征需要计算：1）使用这个特征的损失；2）如果使用这个特征，最优的划分特征值；3）保存到目前为止的最佳特征和特征值
    :param train_data: 输入（X)
    :param label_data: 标签 （y)
    :param index: 表示第几类
    :return: minLoss, split, feature
    """
    sample_numbers = len(label_data) # 有多少个样本(e.g. 6)
    feature_numbers = len(train_data[0]) # 有多少个特征(e.g. 4)
    current_label = [] # 当前类别

    # define the minLoss
    minLoss = 10000000 # 最小损失

    # feature代表是特征的第几个维度 feature represents the dimensions of the feature
    feature = 0

    # split代表划分特征的值 split represents the detail split value
    split = 0

    # 获得当前关注的这个类别对应的标签 get current label
    for label_index in range(0,sample_numbers):
        current_label.append(label_data[label_index][index])
    # print("current_label:",current_label)  # [1, 1, 0, 0, 0, 0]

    # trans all features
    for feature_index in range(0,feature_numbers): # 遍历每一个特征，对于这个特征需要计算：1）使用这个特征的损失；2）如果使用这个特征，最优的划分特征值
        ## current feature value
        current_value = []  # current_value用于保存选定特征的特征值（可能的划分点）

        for sample_index in range(0,sample_numbers):
            current_value.append(train_data[sample_index][feature_index])
        L = 0
        ## different split value
        print current_value # [5.1, 4.9, 7.0, 6.4, 6.3, 5.8]
        for index in range(0,len(current_value)): # 遍历每一个特征点，从第一个特征点开始遍历
            R1 = []
            R2 = []
            y1 = 0
            y2 = 0

            # 按照样本和当前特征值的大小划分到不同的集合
            for index_1 in range(0,len(current_value)):
                if current_value[index_1] < current_value[index]:
                    R1.append(index_1)
                else:
                    R2.append(index_1)

            # 计算第一个集合的标签平均值 calculate the samples for first class
            sum_y = 0
            for index_R1 in R1:
                sum_y += current_label[index_R1]
            if len(R1) != 0:
                y1 = float(sum_y) / float(len(R1))
            else:
                y1 = 0

            # 计算第二个集合标签平均值 calculate the samples for second class
            sum_y = 0
            for index_R2 in R2:
                sum_y += current_label[index_R2]
            if len(R2) != 0:
                y2 = float(sum_y) / float(len(R2))
            else:
                y2 = 0

            # 计算当前特征值划分下的损失 trans all samples to find minium loss and best split
            for index_2 in range(0,len(current_value)):
                if index_2 in R1:
                    L += float((current_label[index_2]-y1))*float((current_label[index_2]-y1))
                else:
                    L += float((current_label[index_2]-y2))*float((current_label[index_2]-y2))

            if L < minLoss: # 如果损失比已有的损失小，那么保存特征的序号（即第几个特征），这个特征下的最佳特征值，最小的损失
                feature = feature_index
                split = current_value[index]
                minLoss = L
                print "minLoss"
                print minLoss
                print "split"
                print split
                print "feature"
                print feature
        return minLoss,split,feature

findBestLossAndSplit(train_data,label_data,0)
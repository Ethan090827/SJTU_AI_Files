# data visualization 数据可视化
import pandas as pd                 # 导入 pandas 库，用于读取和处理数据
import matplotlib.pyplot as plt    # 导入 matplotlib 库，用于数据可视化

if __name__ == '__main__':
    # 加载数据
    data = pd.read_csv('./data.csv')    # 使用 pandas 读取 CSV 格式的数据

    feature_names = list(data.columns)[0:3]    # 提取数据中的属性特征
    target_name = list(data.columns)[3:5]        # 提取数据中的目标特征
    print("属性名称:", feature_names)     # 输出属性特征的名称
    print("目标名称:", target_name)         # 输出目标特征的名称

    X = data.iloc[:, 0:3]   # 提取属性特征列，所有行，0至2列
    y = data.iloc[:, 3:5]     # 提取目标特征列，所有行，第3、4列
    print("属性形状:", X.shape)  # 输出特征的矩阵维度
    print("目标形状:", y.shape)    # 输出目标的矩阵维度

    # 可视化
    fig = plt.figure(figsize=(8, 6))     # 创建一个大小为8*6英寸的图形窗口
    ax = fig.add_subplot(111, projection='3d')     # 创建一个3D图形子图
    ax.set_xlabel(feature_names[0], fontsize=10)   # 设置x轴标签
    ax.set_ylabel(feature_names[1], fontsize=10)   # 设置y轴标签
    ax.set_zlabel(feature_names[2], fontsize=10)   # 设置z轴标签
    ax.set_title('Feature distribution')           # 设置图形标题
    xs = X.iloc[:, 0]     # 提取属性特征的第0列（x）作为横坐标
    ys = X.iloc[:, 1]     # 提取属性特征的第1列（y）作为纵坐标
    zs = X.iloc[:, 2]     # 提取属性特征的第2列（z）作为高度坐标
    nums = y.iloc[:, 0]   # 提取目标特征的第0列作为标签
    classes = y.iloc[:, 1] # 提取目标特征的第1列作为类别
    colors = ['red', 'blue']  # 颜色列表
    for i in range(len(xs)):            # 为每个数据点添加标签
        ax.scatter(xs[i], ys[i], zs[i], c=colors[classes[i]-1], marker='o', s=30, alpha=0.8)  # 绘制散点图
        # xs[i]、ys[i]、zs[i] 表示数据点在三维空间中的坐标，c 参数指定点的颜色，marker 参数指定点的形状，s 参数指定点的大小，alpha 参数指定点的透明度。
        ax.text(xs[i], ys[i], zs[i], nums[i], color=colors[classes[i]-1])  # 添加数据点标签
        # nums[i] 表示数据点的标签，color 参数指定标签的颜色。colors 是对应颜色列表，classes[i]-1 的结果则是数据点所属类别对应的颜色在列表中的索引。
    plt.show()          # 显示可视化结果



# one-variable regression 一元线性回归
import pandas as pd    # 导入 pandas 库，用于读取和处理数据
from sklearn.linear_model import LinearRegression     # 导入线性回归模型
from sklearn.metrics import mean_squared_error     # 导入均方误差指标
import matplotlib.pyplot as plt    # 导入 matplotlib 库，用于数据可视化

if __name__ == '__main__':

    # 加载数据
    df = pd.read_csv('./data.csv')    # 使用 pandas 读取 CSV 格式的数据
    X = df.iloc[:, 0]    # 提取数据中的第0列作为属性特征, 数据中的第0、1、2三列分别是Chins,Situps,Jumps三个特征的数据
    y = df.iloc[:, 3]    # 提取数据中的第3列作为目标特征
    
    # 定义测试样本的索引
    test_indices = [1, 17]
    # 拆分训练集和测试集
    X_train = X.drop(test_indices, axis=0)
    y_train = y.drop(test_indices, axis=0)
    X_test = X.iloc[test_indices]
    y_test = y.iloc[test_indices]
    X_train = X_train.values.reshape(-1, 1)    # 将训练集属性特征的一维数组转换为二维数组
    y_train = y_train.values.reshape(-1, 1)    # 将训练集目标特征的一维数组转换为二维数组
    X_test = X_test.values.reshape(-1, 1)    # 将测试集属性特征的一维数组转换为二维数组
    y_test = y_test.values.reshape(-1, 1)    # 将测试集目标特征的一维数组转换为二维数组

    # 构建并拟合线性回归模型
    model = LinearRegression()    # 创建线性回归模型对象
    model.fit(  ,  )    # 使用数据拟合线性回归模型

    # 使用训练好的模型预测
    y_pred = model.predict(  )    # 对特征进行预测
    mse = mean_squared_error(  ,  )    # 计算均方误差（MSE）

    # 输出模型权重、偏置、均方误差
    print('权重:', model.coef_)
    print('偏置:', model.intercept_)
    print('均方误差MSE:', mse)

    # 绘制数据可视化图形
    y_train_pred = model.predict(X_train)    # 对特征进行预测
    fig, ax = plt.subplots()  # 创建一个子图
    ax.plot(X_train, y_train, 'o')  # 绘制数据散点图
    ax.plot(X_train, y_train_pred, '-')  # 绘制拟合直线
    plt.show()  # 显示图形



# multiple regression 多元线性回归
import pandas as pd   # 导入 pandas 库，用于读取和处理数据
from sklearn.linear_model import LinearRegression  # 使用以线性回归模型为基础的库
from sklearn.metrics import mean_squared_error  # 导入用于计算MSE的库


def result(model, X_test, y_test, PrintSample=True):
    # 使用模型预测自变量的值
    y_pred = model.predict(X_test)
    if PrintSample:
        # 打印每个样本的预测值和真实值（可选）
        for i in range(len(y_pred)):
            print("预测值: {:.3f}, 真实值e: {}".format(y_pred[i], y_test.iloc[i]))
    # 计算误差指标：MSE
    mse = mean_squared_error(y_test, y_pred)
    # 打印模型参数和误差指标
    print('权重:', model.coef_)
    print('偏置:', model.intercept_)
    print('均方误差MSE:', mse)


if __name__ == '__main__':

    # 读取数据
    df = pd.read_csv('./data.csv')
    X = df.iloc[:, :3]  # 提取属性特征列 Chins,Situps,Jumps
    y = df.iloc[:, 3]   # 提取目标特征列 Weights

    # 定义测试样本的索引
    test_indices = [1, 17]
    # 拆分训练集和测试集
    X_train = X.drop(test_indices, axis=0)
    y_train = y.drop(test_indices, axis=0)
    X_test = X.iloc[test_indices, :]
    y_test = y.iloc[test_indices]

    # 定义线性回归模型并用训练数据进行拟合
    lin_reg = LinearRegression()
    lin_reg.fit(  ,  )

    # 输入测试数据并输出预测结果和评估指标
    result(lin_reg,   ,   )


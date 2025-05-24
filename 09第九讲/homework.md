## 第九讲 机器视觉3 作业

#### 724602210635 黄奕中

### 1. 代码补全：

```py
line 056 : x = x.view(batch_size, -1)

line 084 : running_correct += (predicted == target).sum().item()

line 103 : correct += (predicted == labels).sum().item()
```

隐藏层维度分别为 $[\text{ batch \_ size },10,12,12]$ 和 $[\text{ batch \_ size },20,4,4]$

输出层维度为 $[\text{ batch \_ size },10]$

运行结果：
```
| Epoch 1 | batch   300 / 938 | loss: 2.198 | acc: 27.47 % |
| Epoch 1 | batch   600 / 938 | loss: 1.556 | acc: 67.04 % |
| Epoch 1 | batch   900 / 938 | loss: 0.722 | acc: 81.51 % |
| Epoch 1 / 5 | Accuracy on test set: 86.0 % |
| Epoch 2 | batch   300 / 938 | loss: 0.483 | acc: 86.11 % |
| Epoch 2 | batch   600 / 938 | loss: 0.414 | acc: 87.85 % |
| Epoch 2 | batch   900 / 938 | loss: 0.380 | acc: 88.72 % |
| Epoch 2 / 5 | Accuracy on test set: 90.3 % |
| Epoch 3 | batch   300 / 938 | loss: 0.340 | acc: 89.89 % |
| Epoch 3 | batch   600 / 938 | loss: 0.327 | acc: 90.13 % |
| Epoch 3 | batch   900 / 938 | loss: 0.307 | acc: 90.62 % |
| Epoch 3 / 5 | Accuracy on test set: 91.9 % |
| Epoch 4 | batch   300 / 938 | loss: 0.292 | acc: 91.41 % |
| Epoch 4 | batch   600 / 938 | loss: 0.264 | acc: 92.02 % |
| Epoch 4 | batch   900 / 938 | loss: 0.270 | acc: 91.99 % |
| Epoch 4 / 5 | Accuracy on test set: 92.6 % |
| Epoch 5 | batch   300 / 938 | loss: 0.245 | acc: 92.40 % |
| Epoch 5 | batch   600 / 938 | loss: 0.242 | acc: 92.72 % |
| Epoch 5 | batch   900 / 938 | loss: 0.223 | acc: 93.40 % |
| Epoch 5 / 5 | Accuracy on test set: 94.0 % |
```


### 2. 修改网络结构：
修改如下两句：
```py
line 37 : torch.nn.Conv2d(1, 10, kernel_size=9),

line 42 : torch.nn.Conv2d(10, 20, kernel_size=3),
```

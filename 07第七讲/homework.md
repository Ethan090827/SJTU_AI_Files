## 第七讲 机器视觉1 作业

#### 724602210635 黄奕中

---

### 角点

枚举 `blocksize` ：$1, 2, 3, \cdots, 10$
枚举 `ksize` ：$1, 3, 5, 7$
发现：`blocksize` = $5$ 、`ksize` = $5$ 时效果较好：
![result1](https://cdn.luogu.com.cn/upload/image_hosting/87jdv5b2.png)
![result2](https://cdn.luogu.com.cn/upload/image_hosting/8apbb5ov.png)
![result3](https://cdn.luogu.com.cn/upload/image_hosting/ngsy7mj9.png)
![result4](https://cdn.luogu.com.cn/upload/image_hosting/tot05u2x.png)

全部枚举结果图片已打包为results.zip上传，命名格式为：
`Harris\_[图片编号(1-4)]\_[blocksize]\_[ksize].jpg`

---

### 箭头识别

- target_1:
  ```
  [26381.938, 67410.4, 40638.46, 70746.13]
  最优分数： 26381.938
  匹配结果： up       
  ```
- target_2:
  ```
  [56747.047, 84864.6, 60254.758, 85175.21]
  最优分数： 56747.047
  匹配结果： up  
  ```
- target_3:
  ```
  [82052.1, 63459.316, 81770.47, 64074.547]
  最优分数： 63459.316
  匹配结果： right   
  ```
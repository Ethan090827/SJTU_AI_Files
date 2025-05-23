## 第八讲 机器视觉2 作业

#### 724602210635 黄奕中

PS 抱歉，我洛谷图床高级空间满了，这份作业的后面几张图以及以后作业的图会带水印，谅解

---

### 直线检测

发现当 `threshold` 较大时，找到的直线较少，对 `line2` 效果较好（图二），但对 `line1` 效果较差（图一），只能找出一小段电线，而杆子完全无法找到；

发现当 `threshold` 较小时，找到的直线较多，对 `line1` 效果较好，可能是因为其背景干净（图三），但对 `line3` 效果较差（图四），背后的山上全是红色线段；

经过大量尝试发现无法找到对两幅图效果都较为理想的方案

---

图一：`threshold=60,  minLineLength=30, maxLineGap=30`
![图一](https://cdn.luogu.com.cn/upload/image_hosting/tpjq4vj2.png)

---

图二：`threshold=60,  minLineLength=30, maxLineGap=30`
![图二](https://cdn.luogu.com.cn/upload/image_hosting/3fo13nrb.png)

---

图三：`threshold=180,  minLineLength=100, maxLineGap=100`
![图三](https://cdn.luogu.com.cn/upload/image_hosting/3a4cw6pm.png)

---

图四：`threshold=180,  minLineLength=100, maxLineGap=100`
![图四](https://cdn.luogu.com.cn/upload/image_hosting/jrlkmeq7.png)

---

### 圆的检测

发现与直线检测类似，`param2` 越大，检测准确度越高，但过高也会导致漏检测

当 `param2` 合适时，无需过多关注 `minRadius` 和 `maxRadius` 就能取得不错的效果

参数： `param1=150, param2=60, minRadius=10, maxRadius=150`

---

`circle1`:
![circle1](https://cdn.luogu.com.cn/upload/image_hosting/ovgwgrnf.png)

---

`circle2`:
![circle2](https://cdn.luogu.com.cn/upload/image_hosting/y5oscrn4.png)

---

### 手指间隙检测

```py
line 59:  if angle <= np.pi / 2:

line 64:  number_of_fingers = cnt + 1
```

---

`cv2.convexityDefects()` 通过计算图像轮廓与 `cv2.convexHull()` 给出的凸包的距离，找到轮廓偏离凸包的缺陷

---

`one`:
![one](https://cdn.luogu.com.cn/upload/image_hosting/qud7isds.png)

---

`three`:
![three](https://cdn.luogu.com.cn/upload/image_hosting/ahsb522z.png)

---

`five`:
![five](https://cdn.luogu.com.cn/upload/image_hosting/0rf2ect2.png)
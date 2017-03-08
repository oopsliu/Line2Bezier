# 生成流向弧线工具 #
## 1	工具简介 ##
人流移动、城市通勤路线等示意图生产过程中常有生成流向线的需求，而在ArcGIS中如果两点间距离较短则在视觉上均体现为直线，可视化效果欠佳，所以产生了本工具，将示意直线转换为弧线。

## 2	功能说明 ##
将只具有起点、终点的直线转换为二阶贝塞尔曲线。

## 3	参数设置 ##
输入直线要素类，如C:\line.shp

输出弧线要素类，如C:\Flowline.gdb\line2bezier

## 4	使用示例 ##
工具参数：
![](http://i.imgur.com/nOnJnt0.png)

转换前：
![](http://i.imgur.com/iNa1tJP.png)

转换后：
![](http://i.imgur.com/IbsG4Te.png)
 
## 下载地址 ##
[https://github.com/oopsliu/Line2Bezier/blob/master/line2bezier.py](https://github.com/oopsliu/Line2Bezier/blob/master/line2bezier.py "FlowLineTool")
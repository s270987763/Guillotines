> 项目介绍

为了更方便的而又跨平台的使用“中国菜刀”，我们创建了这个项目。该项目是Web版的"中国菜刀",我们暂时取名叫“血滴子”。欢迎感兴趣的朋友一起交流学习。

> 开发成员及负责方面

MXi4oyu(Python后端，用于处理“管理器对shell的核心操作”)。Email：798033502@qq.com

Black-Hole（JavaScrip前端，用于处理“管理器”在浏览器下的显示）。Email：158blackhole@gmail.com

> 安装方法

1. `pip install beaker`
2. `pip install pymysql`
3. `pip install sqlalchemy`
4. `pip install bottle_sqlalchemy`
5. `pip install jinja2`

> 项目的目录结构

```
www 根目录
├─App               应用目录
│  ├─Common             公共函数库
│  ├─Conf               配置目录
│  ├─Controller         控制器目录
│  ├─Model              模型目录
│  ├─View               视图目录
├─Core              核心目录
├─Public            静态资源目录
│  ├─js                 javascript文件目录branch
│  │  ├─branch          自定义javascript文件
│  │  ├─library         第三方javascript插件
│  ├─css                css文件目录
│  │  ├─branch          自定义css文件
│  │  ├─library         第三方css插件
│  ├─less               css引擎less文件目录
│  │  ├─branch          自定义less文件
│  ├─fonts              字体目录
│  ├─image              图像目录
├─index.py          入口文件
├─ip.txt            记录ip地址
├─passwd.py         生成密码
└─guillotines.sql   数据库文件
```

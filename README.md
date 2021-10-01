# vismod

* 可直接用来查看urdf、sdf等模型，不需要通过ROS，也不需要额外的软件。

* **下载地址**：https://github.com/borninfreedom/vismod/releases/tag/publish

* 如果想自己重新打包发布，目前使用的打包命令是，可以作为参考

    ```bash
    pyinstaller -F --hidden-import=tkinter --hidden-import=tkinter.filedialog  --hidden-import=numpy --hidden-import=pybullet --noconsole vismod.py
    ```

    

![在这里插入图片描述](https://img-blog.csdnimg.cn/1c4e6256f55e4ef2abf4111f1dda3490.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAYm9ybi1pbi1mcmVlZG9t,size_11,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/fd1d5abd92f843658f423a4a27c69d85.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAYm9ybi1pbi1mcmVlZG9t,size_12,color_FFFFFF,t_70,g_se,x_16)
![在这里插入图片描述](https://img-blog.csdnimg.cn/2de5e5abf18e4057ba6150151b3bf06c.png?x-oss-process=image/watermark,type_ZHJvaWRzYW5zZmFsbGJhY2s,shadow_50,text_Q1NETiBAYm9ybi1pbi1mcmVlZG9t,size_20,color_FFFFFF,t_70,g_se,x_16)

---

目前仅支持Windows，后续会继续开发其他平台。
开发不易，动动手指头，支持作者一杯咖啡~
| ![](https://img-blog.csdnimg.cn/00f6aef92546424cadff9f4dd680f966.png) | ![](https://img-blog.csdnimg.cn/c5102f26a4ed4d768339db98bd6956a8.jpg) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

|      |      |
| ---- | ---- |

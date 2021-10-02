# vismod

* 可直接用来查看urdf、sdf等模型，并且在查看的同时，如果有关节电机的模型，还会添加上关节电机的控制滑条，实现拖动控制。
* 本软件不需要通过ROS，也不需要安装额外的软件，整个软件只有25M左右。

* **下载地址**：https://github.com/borninfreedom/vismod/releases/tag/publish

* 如果想自己重新打包发布，目前使用的打包命令是，可以作为参考

    ```bash
  pyinstaller -F --hidden-import=tkinter --hidden-import=tkinter.filedialog  --hidden-import=numpy --hidden-import=pybullet --noconsole --onefile vismod.py
    ```

    

![在这里插入图片描述](https://img-blog.csdnimg.cn/5d60a8d53728489f8a643a742a0f36ba.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/7ac35c7afa214e3a8881849171dd7e29.png)
![在这里插入图片描述](https://img-blog.csdnimg.cn/d799a3522ee54126a76c1b4528fa79c2.png)

---

目前仅支持Windows，后续会继续开发其他平台。
开发不易，动动手指头，支持作者一杯咖啡~
| ![](https://img-blog.csdnimg.cn/00f6aef92546424cadff9f4dd680f966.png) | ![](https://img-blog.csdnimg.cn/c5102f26a4ed4d768339db98bd6956a8.jpg) |
| ------------------------------------------------------------ | ------------------------------------------------------------ |

|      |      |
| ---- | ---- |

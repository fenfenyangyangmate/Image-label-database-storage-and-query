# - 图片标签数据库存储以及查询
总说之你要下载好sql数据库，然后pip install -r requirements.txt

还有就是别开翻译插件看这个界面！！！

弄这个主要是🐍🐍的图片太多了，平常放着也是放着，不如给他们打上标签存起来，可以随心所欲的查看图片

主要功能是：自动识别图片标签存储和查询标签下的图片

以后可能会弄个ui，但我技术不太行，就先凑合用吧，俺的好朋友正在努力弄ui（虽然不报太大期望就是了）

#下载https://github.com/KichangKim/DeepDanbooru/releases/download/v4-20200814-sgd-e30/deepdanbooru-v4-20200814-sgd-e30.zip
把压缩包里的文件放到demo里（不想下就直接下我的压缩包，都塞在里面了）
首先运行cs.py(会有点久)
结束后就可以用 查询.py 查询标签下的图片了

可以看文件的教程，特别详细，要是还不行+我qq：460452649

# 更新日志：
    2022.1.10 增加了新旧图库
    2022.1.11 优化写入数据库速度
    2022.1.12 旧图库更新升级
    2022.1.13 发现图片识别错误问题，暂决定有问题图片的图库不列入 更新 ，错误图片移动到 problem_picture ，同时写入 data/temporary.txt
    2022.1.14 加入压缩图片，方便更新图库
    2022.1.20 教程修改(才发现一个关键步骤没写)
    2022.1.21 修复读取标签格式出错问题
    2022.1.22 从断点开始

#重要提示：这个也很重要，想着放后面你们也不会细心看我就放上面了（下面是使用教程不要错过）

1、	假如你的图片多的话 第一阶段 会很久，这取决于你的电脑性能

2、	git clone https://github.com/KichangKim/DeepDanbooru.git

3、	cd DeepDanbooru

4、	pip install -r requirements.txt #如果安装tensorflow有问题见此https://www.tensorflow.org/install/pip

5、	pip install .（假如出错了用 powershell试试）

6、	加入了断点继续

7、	重要：data 假如不是移动了很多图片，不得不重新导入的话，不要删除，千万不要，它记录的是已经导入过的图片，还有更新图库要用的内容，否则会再次写入数据库，重新全部识别。（这里我想了想还是先这样设置）

8、	更新是指，将导入过的图库里新文件压缩后识别

9、	图库名不能有空格




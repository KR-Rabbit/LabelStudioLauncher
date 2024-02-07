<div align="center"><a href="https://labelstud.io/"><img alt="Label Studio" src="https://labelstud.io/favicon.svg" width="20"/>LabelStudio</a>启动器</div>

- 项目说明
    - Label Studio 是一个开源的数据标注工具，支持多种数据类型的标注，包括文本、图像、音频、视频等。Label Studio 启动器是一个基于 Docker 的快速启动工具，可以帮助用户快速启动 Label Studio 服务。
    - 本项目是 Label Studio 的启动器，基于PySide6实现了一个简单的界面，主要针对计算机视觉领域的数据标注任务。Label Studio的具体操作请参考[官方文档](https://labelstud.io/guide/)。
- 项目结构
    Label Studio 启动器的项目结构如下：
    ```
    ├── Launcher.py # 启动器的主程序
    ├── README.md # 项目说明文档
    ├── requirements.txt # 项目依赖
    ├── ui
    │   ├── About.ui # 关于界面
    │   ├── Server.ui # 服务器配置界面,用于配置数据路径和HTTP服务IP和端口，并生成Label Studio对应的JSON文件
    │   ├── Common.ui # 普通配置，用于配置软件关闭时的行为
    │   ├── Conda.ui # Conda环境配置界面
    ├── menu # 菜单栏,对应ui文件夹下的界面
    ├── utils # 工具类
    │   ├── __init__.py
    │   ├── global_manager.py # 全局变量管理器，用于更新配置
    │   ├── http.py # HTTP服务
    │   ├── labels.py # 标签格式转换，主要用于url解码
    │   ├── thread.py # 多线程,用于异步生成Label Studio对应的JSON文件
    ```
- 使用方法
    1. 安装Python环境
    2. 安装依赖
        ```shell
        pip install -r requirements.txt
        ```
    3. 运行启动器
        ```shell
        python Launcher.py
        ```
    4. 配置conda环境
        - 选择conda.exe的路径
        - 选择conda环境的名称
    5. 配置服务器
        - 选择数据路径
        - 配置HTTP服务的IP和端口
        - 点击生成Label Studio配置文件
    6. 启动服务
          - 点击启动服务按钮
          - 等待服务启动成功
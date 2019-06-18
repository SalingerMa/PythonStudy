1 创建新项目

	１　新建文件夹
	２　新建pipenv
	３　安装包



Tip: 关于pipenv
它是第三方包管理器，只服务于当前项目

安装pipenv: pip install pipenv

使用：

１）在项目目录下输入命令: pipenv install
会提示:Creating a virtualenv for this project...

2) 进入项目的pipenv：　pipenv shell

3) 安装第三方包：pipenv install flask

常用命令：

１　退出：　exit

2 查看依赖版本: pipenv graph

3 check virectualenv install path: pipenv --venv


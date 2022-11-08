# 软件工程Lab4实验报告

201502002 洪睿琦



## 一、项目简介

本次项目目的是根据实验2中提出的需求分析和实验3中的框架，实现一个程序等价判断工具。此次程序使用python3进行编程，因此执行环境需要安装python3，只调用了python标准库，不需要安装额外的库。



## 二、子模块划分

程序等价判断工具将分为sample_generator模块、execute模块以及main模块。

sample_generator模块负责解读stdin_format.txt中的信息，并且依据其格式生成若干组样例。

execute模块负责调用编译器运行待测试程序，并记录结果。

main模块负责读入input目录中的输入，并且调用上面两个子模块得到各个程序的运行结果。对各程序的运行结果进行比对并将比对结果输出到equal.csv和inequal.csv中。



## 三、使用方法

在根目录下创建input文件夹，并且按照实验要求中的规则导入样例以及样例生成文件后，在项目根目录调用命令`python3 main.py`。执行过程中，程序会显示当前正在哪个输入目录下运行，并根据stdin_format.txt中所给出的样例说明，随机生成若干组样例。随后对于该目录下的所有C++文件，程序会调用编译器对其进行编译。若编译失败，记录该程序编译失败。若编译成功，运行每一样例并记录其 stdout、stderr等输出信息，若发生运行时错误或者超时，也会将其打上标记。在所有运行结束后，程序会给出运行的总时间，并在根目录创建子目录output，并在里面放入equal.csv和inequal.csv两个文件来记录比对结果。



用户可以根据自己的需要调整每个程序的运行时间上限（超出此时限的程序将被认为是死循环），每个程序在运行时使用的样例数量，以及是否使用程序的hash来进行比对。这些信息在根目录下的config.py中可见且允许用户自行修改，如下：

```python
sample_num = 10 #每个程序运行的样例数量
timeout = 1  #单位为秒
use_hash = True #若为True，将用hash码进行等价性判断，否则将用源输出字符串进行判断。
```

对于use_hash参数，在这里给出更详细的说明。

本程序中，对于每个程序我们将生成一个json对象。其中记录了它运行的每组样例的运行状态和输出。最后判断两个程序是否等价时，只需将两个文件对应的json对象转化为字符串，并看两个字符串是否相等即可。但我们注意到，如果样例数量较多，或者程序输出规模较大，记录每一个程序的输出可能非常占用内存且对各程序的输出结果进行比对可能非常浪费时间。于是就想出了可以仅保存json对象的hash码，并对hash码进行比较的方法。这样无论输出规模有多大，保存的字符串大小都会有一个上限。而我们采用的hash函数为安全度极高的sha256，应该也不会因为碰撞造成结果出现差错。

## 四、git尝试

下面的图中我们将展示在本次开发过程中进行的git操作的截图。

首先我们创建新仓库，并与远程仓库连接：

![git init and remote](E:\Study\大三上\软工\lab4\images\git init and remote.png)



创建新仓库后，添加了一些基本的文件，并进行首次git提交：

![首次commit](/images/首次commit.png)

随后我们进行分支，对每个子模块进行开发，从sample_generator开始：

![sample_generator](/images/sample_generator.png)

该模块开发完毕并充分测试其正确性后，将其合并到master分支：

![](/images/git merge.png)

同理，对execute模块创建独立分支并且在完成后合并到master分支：

![execute](/images/execute.png)

![merge execute](/images/merge execute.png)

最后，直接在master分支上对main模块进行开发：

![main](/images/main.png)

在后续调试过程中，发现了一些bug并且进行了修改，调用git diff命令查看工作区和暂存区修改的部分：

![git diff](/images/git diff.png)

下面我们展示git reset的用法：

![add useless](/images/add useless.png)

上图中我们创建了一个为无用的文件，并进行commit。

![git reset](/images/git reset.png)

使用git reset将暂存区回到上一个版本。



最后，使用git push命令将master分支push到github远程仓库上：

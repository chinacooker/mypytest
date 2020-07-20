# pytest 
## pycharm配置
Tools-Python Integrated Tools-Default test runner-pytest
## 基础
文件test_开头或者_test结尾；方法test开头
类Test开头，不带init方法，类的方法与方法一致
### raise
with python. raises():
    f()
    
    
with python. raises(Excption,message="debug"):

def myfunc():
    raise ValueError("Exception 123 raised")
def test_match():
    with pytest.raises(ValueError, match='Exception 123 raised'):
    match=r'.*123.*'   与search一致，模糊匹配
        myfunc()


### 一些参数
-x 失败停止
--maxfail=1 失败次数停止
-k 按名称执行
-m 安mark的名字  @python.mark.name
-v 详细信息
-s 不打印print
-q 静默模式
pytest --showlocals # 在追溯信息中显示局部变量   ****
pytest -l           # 显示局部变量 (简写)
pytest --tb=auto    # (默认) 第1和最后1条使用详细追溯信息，其他使用简短追溯信息
pytest --tb=long    # 详尽，信息丰富的追溯信息格式
pytest --tb=short   # 简短的追溯信息格式  ***
pytest --tb=line    # 每个失败信息一行
pytest --tb=native  # Python标准库格式  ****
pytest --tb=no      # 不使用追溯信息   ****
pytest --durations=10 #耗时最长的case
### 调试模式
--pdb调试模式
import sys;sys.last_traceback.tb_lineno;sys.last_value
sys.last_traceback;sys.last_type;sys.last_value
--trace直接进调试
代码设置断点import pdb; pdb.set_trace()
n+enter执行下一步


### 临时目录使用
执行pytest会生成临时目录tmp_path
d = tmp_path / "sub"
d.mkdir()
p = d / "hello.txt"
p.write_text(CONTENT)
### 报告
pytest --junitxml=path

### 断言
assert 1==1
assert 1!=1,"text"

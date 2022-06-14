# digitalSignal
`digitalSignal/__init__.py `
```
__all__ = ["darray", "SignalArray", "SignalElement", "SignalIndex"]
__all__ += ["expand", "expand2r", "array2t0"]
__all__ += ["dft", "fft", "fft1"]
```
## SignalArray
### 参数
* `index`：`rang` 或 `list`
* `element`：`rang` 或 `list`

### 示例
```
a = darray(range(-1, 10), range(0, 11))
b = darray(range(2, 10))# 如不指定index，默认从0开始
```
> 初始化后，`index`与`element`完成绑定，这将与`SignalArray`容器属性有关

### 字符输出
```
darray range(0, 8)
       0.553733+0.000000j            2.394647-2.097012j     
      -1.386684+0.915560j           -0.881042+0.280414j     
      -0.807574+0.000000j           -0.881042-0.280414j
```
> 不建议输出数字，对于一个序列来说这并不直观

### 内置函数
* `a.reverse()`：倒序
* `a.shift(n: int)`：移位
* `a.phase()`：相位（复数序列有效）
* `a.round(decimals: int)`：保留小数
* `a.public(b: SignalArray)`：两个序列的相同部分
* `a.array()`：序列本身

### 容器属性
* `a[-1]`：返回索引为`-1`元素，数据类型由元素本身决定
* `a[-1:2]`：返回`[-1, 1]`的元素，数据类型为`SignalArray`
* `a[-1]`：为索引为`-1`的元素重新赋值
* `a[-1:2]=[0, 1, 2]`：为`[-1, 1]`的元素重新赋值

### 基础算数运算
加(+)、减(-)、乘(*)、乘方(**)
* 如果是两个`SignalArray`之间进行，则只计算索引相同部分
* 如果是`SignalArray`与`int, float, complex`之间，则对每个元素计算

### 序列操作
* `expand(a: SignalArray, n: int)`：周期延拓
* `expand2r(a: SignalArray)`：周期延拓后的主值序列
* `array2t0(a: SignalArray)`：将周期序列移动到零位

## 傅立叶变换
### 离散傅立叶变换(dft)
```
a: SignalArray,
n: Optional[int] = None,
k: Union[int, float, list, range] = None
```
1. `n`值默认与`index`大小相同，如果`n`值大于序列，序列将被补零；小于，序列将被裁断
2. `k`值默认与`index`相同

### 快速傅立叶变换(fft)
```
a: SignalArray,
n: Optional[int] = None,
```
1. `n`与`dft`相同
2. `fft1`：为基-2的`fft`
3. `fft`：来自[SciPy](https://scipy.org)




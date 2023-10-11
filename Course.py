##################################
#     利用Python进行数据分析     #
##################################

# 数组创建函数
array、asarray、arange、ones、ones_like、zeros、zeros_like、empty、empty_like、eye、identi

# 利用数组进行数据处理 
import numpy as np 
points=np.arange(-5,5,0.01)
xs,ys=np.meshgrid(points,points)
print(xs,type(xs))# numpy.ndarray
print(ys,type(ys))
z=np.sqrt(xs**2,ys**2)
import matplotlib.pyplot as plt
plt.imshow(z,cmap=plt.cm.gray)
plt.colorhar()
plt.title('Image plot of $\sqrt{x^2+y^2}$ for a grid of values')

# 将条件逻辑表达为数组运算
	# numpy.where是三元表达式x if condition else y的矢量化版本
xarr=np.array([1.1,1.2,1.3,1.4,1.5])
yarr=np.array([2.1,2.2,2.3,2.4,2.5])
cond=np.array([True,False,True,True,False])
result=[(x if c else y) for x,y,c in zip(xarr,yarr,cond)]
	# 该种方法对大数组处理速度不是很快(Python完成)，另无法用于多维数组
	# 使用np.where,第二个和第三个参数不必是数组，可以是标量值
result=np.where(cond,xarr,yarr)
		# 将一个随机数据组成的矩阵的所有正值改成2，负值改成-2
arr=np.random.randn(4,4)
result=np.where(arr>0,2,-2)

	# 两个布尔型数组cond1和cond2，根据4中种不同的布尔值组合实现不同的负值操作
	result=[]
	cond1=[False,True,True,False,False]
	cond2=[False,False,True,True,True]
	for i in range(5):
		if cond1[i] and cond2[i]:
			result.append(0)
		elif cond1[i]:
			result.append(1)
		elif cond2[i]:
			result.append(2)
		else:
			result.append(3)
	# 使用np.where( unsupported operand type(s) for &: 'list' and 'list')
	cond11=np.array(cond1)
	cond22=np.array(cond2)
	result=np.where(cond11 & cond22,0,
		np.where(cond11,1,
			np.where(cond22,2,
				3)))
		
# 数学和统计方法
arr=np.random.randn(5,4)
print(arr)
arr.mean()
	# 等价
np.mean(arr)
arr_op_col=arr.mean(axis=1)
print(arr_op_col.shape)
arr_op_row=arr.sum(0)
print(arr_op_row.shape)

print(arr.cumsum(0))
print(arr.cumprod(0))

# 用于布尔型数组的方法
arr=np.random.randn(100)
(arr>0).sum()

	# any检测数组中是否一个或者多个True(非0)
bools=np.array([False,True,False])
bool.any()
boo.all()

	
# 排序
arr=np.random.randn(8)
arr.sort()
	# 多维数组沿轴排序
arr=np.random.randn(3,4)
print(arr)
arr.sort(1)
print(arr)

# 唯一化以及其他的集合逻辑np.unique
names=np.array(['bob','joe','will','bob','joe'])
np.unique(names)# 唯一值并已排序红啊
ints=np.array([2,2,2,1,1,4,4,3])
uni=np.unique(ints)
print(uni)

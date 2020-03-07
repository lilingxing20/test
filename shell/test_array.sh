#!/bin/bash

#
### 数组声明
#
declare -a array_name       # 声明数组，也可以不声明 
declare -a nums=(1 2 3 4)   # 声明数组，同时也可赋值
unset array_name            # 删除数组，撤销数组
unset nums[0]               # 删除数组中的某个元素


#
### 数组定义
#
# 方式一：
array_name=(
value0
value1
value2
value3
)

# 方式二：
names=(Jerry Alice David Wendy)

# 方式三：
names[0]=Jerry
names[1]=Alice
names[2]=David
names[3]=Wendy

# 方式四：
names=([0]=Jerry [1]=Alice [2]=David [3]=Wendy)

# 方式五：
str=“Jerry Alice David Wendy”
names=($str)

#
### 求数组长度
#
nums=(Jerry Alice David Wendy)
#方式一：${#数组名[@]}
echo ${#names[@]}                    # 输出结果：4， 4个元素
#方式一：${#数组名[*]}
echo ${#names[@]}                                     # ${array[@]}等价于${array[*]}

### 求元素长度
nums=(Jerry Alice David Wendy)

# 方式一：${#数组名[index]}
# 求元素长度
${#nums[0]}

# 方式二：expr length ${数组名[index]}
# expr length的函数来求元素长度
expr length ${names[0]}

# 方式三：wc -L
# 使用-L参数累获取当前行的长度
echo ${names[0]} |wc -L

# 方式四：wc -l结合echo -n
# -n参数，去除“\n”换行符
echo -n ${names[0]} |wc -l

# 方式五：expr ${names[0]} : ".*"
# .*代表任意字符，用任意字符来匹配字符串
expr ${names[0]} : ".*"

# 方式六：awk的NF项
# 先分割，再用NF域来求元素长度
echo ${names[0]} | awk -F "" '{print NF}'

# 方式七：awk的length
# 使用awk中的length（）函数
echo ${names[0]} | awk '{print length($0)}'


#
### 数组遍历
#
# 方式一：按索引来遍历
names=(Jerry Alice David Wendy)
for ((i=0;i<${#names[*]}; i++))
do
    echo ${names[$i]}
done

# 方式二：不按索引来遍历
nums=(Jerry Alice David Wendy)
index=0
for i in ${names[@]}
do
    echo "第${index}个元素的值为：==>${i}"
    let index++
done


#
### 数组添加元素
#
nums=(1 2 3 4)    # 定义一个数组
nums[3]=44        # 给第三个元素重新赋值
echo ${nums[@]}   # 结果变成了 1 2 3 44   

#
### 数组添加
#
# 方式一：直接赋值给不在的索引一个值
nums=(1 2 3 4)                   # 定义一个数组
nums[4]=5                        # 给第四个新元素赋值
echo ${nums[@]}                  # 结果变成 1 2 3 4 5

# 方式二：直接使用 新数组=(旧数组 新元素) 的方式来添加元素
old=(1 2 3 4)
new=(${old[*]} 5)
echo ${new[@]}


#
### 数组切片
#
array=(zero one two three four)
$array                            # 默认取第一个元素，输出：zero
${array[0]}                       # 取索引为零对应的元素，输出：zero
${array[@]}                       # 去数组中全部元素
${array[@]:1}                     # 从索引为1到后面所有的值，输出：one two three four
${array[@]:0:3}                   # 从索引为0开始取，共取三位，输出：zero one two
${array[@]::4}                    # 从索引为0开始取，共取四位，输出：zero one two three
${array[@]:(-2):2}                # 从倒数第二个元素开始取，取两位，输出：three four
new_array=(${array[@]}:1:4)       # 得到新的切片数组


#
### 元素切片
#
names=(Jerry Alice David Wendy)
echo ${names[0]:0}                 # 取索引为0开始取所有：Jerry
echo ${names[0]:1}                 # 取索引为1开始取所有：erry
echo ${names[0]:2:2}               # 取索引为2开始取两位：rr
echo ${names[0]:6}                 # 超出元素长度显示空行：


#
### 数组替换
#
array=(zero one two three four)
echo ${array[@]/e/E}              # 每个元素只替换一次: zEro onE two thrEe four
echo ${array[@]//e/E}             # 每个元素只替换多次: zEro onE two thrEE four
echo ${array[@]/e/}               # 最小匹配删除：zro on two thre four
echo ${array[@]//e/}              # 最大匹配删除：zro on two thr four

echo ${array[@]/#o/O}             # 只替换每个元素左边的o: zero One two three four
echo ${array[@]/%o/O}             # 只替换每个元素右边的o: zerO one twO three four


#
### 数组删除
#
list=(book food)
echo ${list[@]#b*o}          # bo匹配到被删除: ok food
echo ${list[@]##b*o}         # boo匹配到被删除: k food
echo ${list[@]%o*d}          # od匹配到被删除: book fo
echo ${list[@]%%o*d}         # ood匹配到被删除: book f


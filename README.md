<!--
 * @Description: 
 * @Author: zgong
 * @Date: 2020-09-23 13:53:44
 * @LastEditTime: 2020-09-23 14:30:04
 * @LastEditors: zgong
 * @FilePath: /ClassDemo/README.md
 * @Reference: 
-->
## How to use it?

1. 教务网站下载classAssignment.xls 置于文件夹中
2. 查看表中数据，确保课程数据结构为：
    classname(classroom)(*任意字符*) 每周/单周/双周 (大部分课程默认满足格式)
3. python etc/run.py
4. 生成my.ics文件！

## 注意
1. 同一个位置可以有多个课程，但要注意中间用；隔开，如
    高数1(理教101)()单周;高数2(理教202)()双周;高数3(理教303)()每周

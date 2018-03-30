# [ChipseaAssembly-GitHub](https://github.com/junglefive/ChipseaAssembly)

  *本文档用于说明 `Chipsea` 汇编，在文本编辑器 `Sublime Text 3` 中的高亮显示插件 `ChipseaAssembly` 的使用及修改方法*

## 使用方法

> 使用:

- 首先需安装 `Sublime Text 3` 文本编辑器 .
- 打开软件，`ctrl+shift+p`->输入'install package'->`回车`->输入`Chipsea Assembly`回车安装.
- 打开代码源文件，语法选择`sublime/View/Syntax/Chipsea`
- 背景选择, `sublime/preference/Color Scheme/Chipsea Assembly/Chipsea Mac 或Chipsea Monokai`

## 更新记录

> 2017/3/13

  - add keyword `csnf`     As `<!-- ChipSea New Function -->`
  - add keyword `csfc`     As `<!-- ChipSea Function Comments -->`
  - add keyword `cshead`   As `<!-- ChipSea Head declare-->`
  - add keyword `csnm`     As `<!-- ChipSea New Macro-->`

> 2017/3/22

  - add keyword `csdelay`  AS `<!-- ChipSea New Delay_1ms -->`

>  2017/4/16

  - add keyword `cdnb`     As `<!-- Chipesa NewBlock -->`

> 2017/7/21

  - 增加了注释的长度
  - 注释中不带`=`号

> 2017/8/29

 - 增加了对`high` `low`的高亮
 - 增加了快捷注释`ctrl + /` `ctrl + shift + /`

> 2017/8/31

 - 增加了`Comments.tmpreferences`对单行注释和多行注释进行支持

> 2017/10/15

 - 增加插件`InsertNum`->[`ctrl+alt+N`]
 - 增加插件`ClearConsole`->[`alt+k`]
 - 增加`cs-asm`自动格式化排版->[`ctrl+alt+F`]
 - 增加`view->console`显示`equ`,`define`,`macro`定义

> 2017/10/16

 - 修复`Include`缩进改为不缩进
 - 修复带`Macro`的行误缩进

> 2017/10/26

 - 空行不做处理(使用`DeleteBlankLines`->`Ctrl+Alt+Backspace `即可)
 
> 2018/03/30

- 增加 `goto defination`到汇编函数、变量、常量

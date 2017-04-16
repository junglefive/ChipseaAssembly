# [ChipseaAssembly-GitHub](https://github.com/junglefive/ChipseaAssembly)

  *本文档用于说明 `Chipsea` 汇编，在文本编辑器 `Sublime Text 3` 中的高亮显示插件 `ChipseaAssembly` 的使用及修改方法*

## 使用方法
> 使用:
- 首先需安装 `Sublime Text 3` 文本编辑器，目前官方稳定版本号为 `3126` .
- 打开软件，复制文件夹 `ChipseaAssembly` ，进入 `sublime/preference/Browse Packages`,粘贴到当前目录
- 打开代码源文件，语法选择`sublime/View/Syntax/Chipsea`
- 背景选择, `sublime/preference/Color Scheme/Chipsea Assembly/Chipsea Mac 或Chipsea Monokai`

> 修改：
1. 安装 `PackageDev` 插件；
2. 通过 `Tools | Packages | Package Development` 菜单进行操作
3. 使用 `Sublime` 打开 `chipseaAssembly.YAML-tmLanguage` 文件，添加高亮关键词，按 `ctrl+B` 选择 `Convert to ...` 会提示 `[Finished in 0.078s]` ,生成(Build)新的 `chipseaAssembly.tmLanguage`文件即可。

## 相关资料

  - `{数字编号}` 可以得到一个`TAB`占位符
  - `{1:default}` 可以得到一个默认值
  - `\$`可以得到`$`字符, 实例见 `csndelay` 
  - [手把手教你写`Sublime中`的Snippet](http://www.jianshu.com/p/356bd7b2ea8e)
  - [`sublime3`自定义`snippets`小技巧](https://segmentfault.com/a/1190000002598116)
  
## 更新记录

> 更新20170313:

  - add keyword `csnf`     As `<!-- ChipSea New Function -->`
  - add keyword `csfc`     As `<!-- ChipSea Function Comments -->`
  - add keyword `cshead`   As `<!-- ChipSea Head declare-->`
  - add keyword `csnm`     As `<!-- ChipSea New Macro-->`

> 更新20170322:

  - add keyword `csdelay`  AS `<!-- ChipSea New Delay_1ms -->`

> 更新20170411:
> 

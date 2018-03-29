import sublime
import sublime_plugin
import re
import os
import sys
import sqlite3

# connect=sqlite3.connect('chipsea.db')

class ChipseaCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")


class GotoFunctionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        buf =self.view.substr(self.view.sel()[0])
        find_list = self.view.find_by_selector("support.function") #comment.line.string
        print(str(type(find_list)))
        for i in find_list:
            print(str(i.a)+":"+str(i.b))
            print(self.view.substr(i))


class ChipseaGetDefine(sublime_plugin.ViewEventListener  ):
    """docstring for ChipseaGetDefine"sublime_plugin.ViewEventListener  def __init__(self, arg):
        super(ChipseaGetDefine,sublime_plugin.ViewEventListener .__init__()
        self.arg = arg
    """
    current_selected_text = ""
    def on_selection_modified(self):
        # print("call on_selection_modified")
        sel_reg_len = len(self.view.sel())
        if sel_reg_len == 1:
            # print("sel_reg_len:",len(self.view.sel()))
            line = self.view.substr(self.view.sel()[0])
            # print("get:",line)
            line = line.strip()

            if line == "":
                pass
            else:
                # .*(?i)macro[\s\S]*endm
                # equ
                result = self.view.find_all(line+r".*(?i)equ.*")
                for reg in result:
                    lin = self.view.substr(reg)
                    # print("search:",lin)
                    if lin != self.current_selected_text:
                        if re.match(r".*(?i)equ.*",lin):
                            print(lin)
                    self.current_selected_text = lin
                # macro
                result = self.view.find_all(line+r".*(?i)macro[\s\S]*endm")
                for  reg in result:
                    pass
                    lin = self.view.substr(reg)
                    if lin != self.current_selected_text:
                        if re.match(r".*(?i)macro",lin):
                            print(lin)
                    self.current_selected_text = lin
                # define
                result = self.view.find_all(r"(?i)define.*"+line+r".*")
                for  reg in result:
                    pass
                    lin = self.view.substr(reg)
                    if lin != self.current_selected_text:
                        if re.match(r"(?i)define.*",lin):
                            print(lin)
                    self.current_selected_text = lin





class ChipseaAlign(sublime_plugin.TextCommand):
    """docstring for ChipseaAlign"""
    def run(self, edit):
        for region in self.view.sel():
            lines = self.view.substr(region)

            comment_block_list = re.findall(r"/\*.*?\*/",lines,re.S)
            len_tmp = len(comment_block_list)
            for i in range(0, len_tmp):
                block = comment_block_list[i]
                try:
                    block = block.replace("/*",";")
                    block = block.replace("*/",";")
                    block = block.replace("\n","\n;")
                    # for line in block:

                    print(block)
                except Exception as e:
                    pass
                try:
                    lines = lines.replace(comment_block_list[i],block)
                except Exception as e:
                    pass
                    print("替换失败",str(e))
                print(lines)

            line_list = re.split(r"\n", lines)
            re_out = ""

            line_content_max_length = 0
            line_equ_max_length = 0
            for line in line_list:
                tmp = line.strip()
                tmp_list = re.split(r";",tmp)
                if re.match(r".*(?i)\bequ\b",tmp):
                    equ_list = re.split(r"(?i)\bequ\b",tmp)
                    equ_content = equ_list[0]
                    equ_content = equ_content.strip()
                    equ_content = re.sub(r"[\s]+"," ", equ_content)
                    tmp_len_equ = len(equ_content)
                    if tmp_len_equ> line_equ_max_length:
                        line_equ_max_length = tmp_len_equ
                    print("equ_len:",line_equ_max_length)
                # tmp_list = re.split(r";|/\*|\*/",tmp)
                content = tmp_list[0] #行内容
                content = content.strip()
                content = re.sub(r"[\s]+"," ", content)
                tmp_len = len(content)
                if tmp_len > line_content_max_length:
                    line_content_max_length = tmp_len



            for line in  line_list:
              tmp = line.strip()
              tmp_list =  re.split(r";",tmp)
              comment = tmp.replace(tmp_list[0],"")
              comment = re.sub(r"[\s]+"," ", comment)
              tmp = tmp_list[0]
              tmp = tmp.strip()
              content = tmp
              tmp = re.sub(r"[\s]+"," ", tmp)
              # 不加缩进
              if re.match(r"(?i).*:|.*\bmacro\b|^\s*\binclude\b.*", tmp):
                    re_out += tmp+"\n"
              else:
                    len_content  =len(tmp)
                    if len_content > 1:
                        block_list = re.split(r"\s",tmp)
                        length = len(block_list[0])
                        tmp_str = block_list[0]

                        if length == 0:
                            pass
                        elif re.match(r".*(?i)\bequ\b",tmp):
                             # print("get equ")
                             for i in range(0,line_equ_max_length-length):
                                tmp_str += " "

                        else:
                           for i in range(0,7-length):
                                tmp_str += " "
                        tmp = tmp.replace(block_list[0], tmp_str)
                        tmp_len = len(tmp)
                        # re_out += "    "+tmp+" "+comment+"\n"
                        for i in range(0, line_content_max_length - tmp_len):
                            tmp += " "
                        re_out +=  "    "+tmp+comment+"\n"
                    else :
                        re_out += comment+"\n"

            self.view.replace(edit, region, re_out)




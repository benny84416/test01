# 输入：command = "G()(al)"
# 输出："Goal"
# 解释：Goal 解析器解释命令的步骤如下所示：
# G -> G
# () -> o
# (al) -> al
# 最后连接得到的结果是 "Goal"
command = "G()(al)"
print(command.replace('()','o').replace('(al)','al'))
import os, glob


width_title = ["0_80em","0_90em","1_00em","1_10em","1_20em","1_30em", "1_32em", "1_40em", "1_50em","1_60em","1_70em","1_80em"]
#                 0        1        2         3       4       5         6        7         8         9       10        11
#width  = width_title[0]

print("press the mode")
for i in range(len(width_title)):
    line_print = width_title[i] + " : " + str(i)
    print(line_print)

x = input()

line_print = "You choose the "+ width_title[x]
print(line_print)
width = width_title[x]




whereisit ="/cms/ldap_home/seungjun/nano/mg5amcnlo/madgraph/various/"
#whereisit ="/u/user/seungjun/SE_UserHome/lhe/"
#whereisit ="/u/user/seungjun/scratch/mg5amcnlo/madgraph/various/"
folder_path = whereisit+width
#folder_path = "1_80em"
file_list = os.listdir(folder_path)
file_count = len(file_list)

print(file_list)
for i in range(file_count):
    file_name = "pwgevents-00"
    count_num = i+1
    if i<10:
        print(count_num)
    if count_num <10:
        file_name = "pwgevents-000" + str(count_num)+".lhe"
        print(file_name)
    if count_num >=10:
        file_name = "pwgevents-00" + str(count_num)+".lhe"
    if count_num >=100:
        file_name = "pwgevents-0" + str(count_num)+".lhe"
    if count_num >=1000:
        file_name = "pwgevents-" + str(count_num)+".lhe"

    #origin_file = whereisit+file_list[i]
    #after_file = whereisit+file_name
    origin_file = folder_path +"/"+ file_list[i]
    after_file  = folder_path +"/"+ file_name
    command = "mv " + origin_file + " " + after_file
    print(command)
    os.system(command)
    #os.chdir(whereisit+folder_path) 
    #os.rename(file_list[i],file_name)

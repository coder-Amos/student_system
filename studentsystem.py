import os


def main():
    while True:
        menu()
        num = int(input("请输入您选择的序号："))
        if num == 0:
            answer = input("您 确定要退出吗？y/n")
            if answer == 'y':
                print("感谢您使用本系统！！！")
                break
            else:
                continue
        elif num == 1:
            insert()
        elif num == 2:
            search()
        elif num == 3:
            delete()
        elif num == 4:
            modify()
        elif num == 5:
            sort()
        elif num == 6:
            total()
        elif num == 7:
            show()


def menu():
    print("============================学生信息管理系统===========================")
    print("-------------------------------功能目录-------------------------------")
    print("\t\t\t\t\t\t1、录入学生信息")
    print("\t\t\t\t\t\t2、查询学生信息")
    print("\t\t\t\t\t\t3、删除学生信息")
    print("\t\t\t\t\t\t4、修改学生信息")
    print("\t\t\t\t\t\t5、排序")
    print("\t\t\t\t\t\t6、统计学生总数")
    print("\t\t\t\t\t\t7、显示所有学生信息")
    print("\t\t\t\t\t\t0、退出系统")
    print("==================================================================")


student_list = []


def insert():
    while True:
        id = int(input('请输入学生的id(如：1001)'))
        if not id:
            print("请输入正确的id")
            break
        name = input('请输入学生姓名')
        if not name:
            break
        try:
            score = float(input('请输入学生总成绩（保留小数点后一位）'))
        except:
            print('成绩输入有误')
            continue
        question = input("是否保存此条记录？y/n")
        if question == 'y':
            student = {'id': id, 'name': name, 'score': score}
            student_list.append(student)
            save(student_list)
            print('学生信息保存成功！！！')
            break
        else:
            break


def save(student_list):
    try:
        stu_txt = open('student.txt', 'a', encoding='utf-8')
    except:
        stu_txt = open('student.txt', 'w', encoding='utf-8')
    for info in student_list:
        stu_txt.write(str(info) + '\n')
    stu_txt.close()


def search():
    while True:
        print("您可以选择查询全部或者按照学生id进行查找：1、查询全部 2、按照id查找")
        selected_item = int(input("请输入您的选择"))
        try:
            student_txt = open('student.txt', 'r', encoding='utf-8')
            student_info = student_txt.readlines()
        except:
            print("没有学生信息--未查询到学生信息文档")
        if selected_item == 1:
            if student_info:
                for info in student_info:
                    print(info)
        elif selected_item == 2:
            input_id = int(input("请输入需要查询的学生ID："))
            s = {}
            info_list = []
            if student_info:
                for info in student_info:
                    s = dict(eval(info))
                    if s['id'] == input_id:
                        info_list.append(s)
                if len(info_list) == 0:
                    print("未查询到该学生信息")
                else:
                    for i in info_list:
                        print('查询结果： ' + str(i))
        else:
            print('请输入正确的选项！！！')
            continue
        to_contine = input("是否继续查询？y/n")
        if to_contine == 'y':
            continue
        else:
            break


def delete():
    while True:
        student_old = []
        select_id = int(input("请输入要删除的学生的id:"))
        if select_id != '':
            if os.path.exists('student.txt'):
                with open('student.txt', 'r', encoding='utf-8') as file:
                    student_old = file.readlines()
            else:
                student_old = []
            flag = False  # 判断是否删除
            if student_old:
                with open('student.txt', 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:
                        d = dict(eval(item))
                        if d['id'] != select_id:
                            print(d['id'] != select_id)
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id为{select_id}的学生信息已删除')
                    else:
                        print('没有查询到该学生信息')
            else:
                print("无学生信息")
                break
            show()
        redetele = input("是否继续删除学生信息？y/n")
        if redetele == 'y':
            continue
        else:
            break


def modify():
    while True:
        mo_student_id = int(input('请输入需要修改的学生id'))
        mo_student_name = input('请输入新的学生姓名')
        mo_student_score = float(input('请输入新的学生成绩'))
        mo_student_list = []
        if mo_student_id != '':
            if os.path.exists('student.txt'):
                with open('student.txt', 'r', encoding='utf-8') as rfile:
                    student_info = rfile.readlines()
            else:
                student_info = []
            if student_info:
                infos = {}
                for info in student_info:
                    infos = dict(eval(info))
                    mo_student_list.append(infos)
                    if infos['id'] != mo_student_id:
                        mo_student_list.append(infos)
                    else:
                        mo_student_list.append(
                            {'id': mo_student_id, 'name': mo_student_name, 'score': mo_student_score})
                for stu in mo_student_list:
                    with open('student.txt', 'w', encoding='utf-8') as wfile:
                        wfile.write(str(stu) + '\n')

                    print("学生信息修改完毕")
            else:
                print("没有查询到该学生信息")
        else:
            print("请输入正确的学生id")
        show()
        remodif = input("是否继续修改学生信息？y/n")
        if remodif == 'y':
            continue
        else:
            break


def sort():
    while True:
        try:
            student_info = open('student.txt', 'r', encoding='utf-8')
            student_info_list = []
        except:
            print("没有学生信息--未查询到学生信息文档")
            break
        if student_info:
            for i in student_info:
                student_info_list.append(dict(eval(i)))
            if len(student_info_list) > 1:
                seletItem = int(input("1、按照id排序，2、按照姓名排序3、按照成绩排序"))
                if seletItem == 1:
                    select_sort_id = int(input("1、升序排序，2、降序排序"))
                    if select_sort_id == 1:
                        print('排序结果如下：')
                        for i1 in sorted(student_info_list, key=lambda i: i['id'], reverse=False):
                            print(str(i1) + '\n')
                        print('---------------------------------------------------')
                    elif select_sort_id == 2:
                        print('排序结果如下：')
                        for i2 in sorted(student_info_list, key=lambda i: i['id'], reverse=True):
                            print(str(i2) + '\n')
                        print('---------------------------------------------------')
                    else:
                        print("请输入正确的选择序号")
                        break

                elif seletItem == 2:
                    select_sort_name = int(input("1、升序排序，2、降序排序"))
                    if select_sort_name == 1:
                        print('排序结果如下：')
                        for i3 in sorted(student_info_list, key=lambda i: i['name'], reverse=False):
                            print(str(i3) + '\n')
                        print('---------------------------------------------------')
                    elif select_sort_name == 2:
                        print('排序结果如下：')
                        for i4 in sorted(student_info_list, key=lambda i: i['name'], reverse=True):
                            print(str(i4) + '\n')
                        print('---------------------------------------------------')
                    else:
                        print("请输入正确的选择序号")
                        break
                elif seletItem == 3:
                    select_sort_score = int(input("1、升序排序，2、降序排序"))
                    if select_sort_score == 1:
                        print('排序结果如下：')
                        for i5 in sorted(student_info_list, key=lambda i: i['score'], reverse=False):
                            print(str(i5) + '\n')
                        print('---------------------------------------------------')
                    elif select_sort_score == 2:
                        print('排序结果如下：')
                        for i6 in sorted(student_info_list, key=lambda i: i['score'], reverse=True):
                            print(str(i6) + '\n')
                        print('---------------------------------------------------')
                    else:
                        print("请输入正确的选择序号")
                        break
                else:
                    print("请输入正确的选择序号")
                    break

            else:
                print("仅有一条学生信息，不用执行排序操作")
        else:
            break
        break


def total():
    try:
        student_txt = open('student.txt', 'r', encoding='utf-8')
        student_info = student_txt.readlines()
    except:
        print("没有学生信息--未查询到学生信息文档")
    if student_info:
        s = {}
        num = 0
        for _ in student_info:
            num += 1
        print("学生总数为：{0}".format(num))
    else:
        print("没有学生信息")


def show():
    try:
        student_txt = open('student.txt', 'r', encoding='utf-8')
        student_info = student_txt.readlines()
    except:
        print("没有学生信息--未查询到学生信息文档")
    if student_info:
        print("查询结果如下：")
        for info in student_info:
            print('-------------------------------------------')
            print(info)
            print('-------------------------------------------')


if __name__ == '__main__':
    main()

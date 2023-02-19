import csv


def specialCharacterSeg(fileName, outFileName, specialChar):
    """
    将结构化的数据导入的csv 中
    :param fileName:  目标文件路径
    :param outFileName: 输出文件名
    :param specialChar: 分割字符
    """
    out = open(outFileName, 'w', newline='')
    csv_writer = csv.writer(out, dialect='excel')

    f = open(fileName, "r")
    for line in f.readlines():
        # line = line.replace(',', '\t')  # 将每行的逗号替换成空格
        list = line.split(specialChar)  # 将字符串转为列表，从而可以按单元格写入csv
        csv_writer.writerow(list)


if __name__ == '__main__':
    specialCharacterSeg("../../file/a.txt", "初赛榜单用户领奖记录.csv", ",")

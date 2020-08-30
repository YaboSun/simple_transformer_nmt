"""
对训练数据进行清洗
"""
import os

import opencc

project_dir = os.path.dirname(os.path.dirname(__file__))
data_dir = os.path.join(project_dir, 'data')


def _write_data2file(data_list, path):
    with open(path, 'w', encoding='utf-8') as wf:
        for data in data_list:
            wf.write(data + '\n')


class DataClean:
    def __init__(self):
        self.data_batch = 2000
        self.traditional_file = os.path.join(data_dir, 'train.txt')
        self.clean_file = os.path.join(data_dir, 'train_cleaned.txt')

    def t2s(self, traditional_file, clean_file):
        """
        繁简转换
        :param traditional_file:
        :param clean_file:
        :return:
        """
        converter = opencc.OpenCC('t2s.json')
        with open(traditional_file, 'r', encoding='utf-8') as rf:
            batch_data = []
            for line in rf:
                line = line.strip().split('\t')
                line[1] = converter.convert(line[1])
                batch_data.append(line[0] + '\t' + line[1])
            _write_data2file(batch_data, clean_file)


if __name__ == '__main__':
    clean = DataClean()
    clean.t2s(clean.traditional_file, clean.clean_file)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import sys
from collections import defaultdict

def calculate_column_averages(csv_file_path):
    """
    读取CSV文件并计算数值列的平均值
    
    Args:
        csv_file_path (str): CSV文件路径
    
    Returns:
        dict: 包含每列平均值的字典
    """
    # 存储每列的数值
    column_values = defaultdict(list)
    
    try:
        # 读取CSV文件
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # 获取列名
            headers = reader.fieldnames
            
            # 遍历每一行
            for row in reader:
                for header in headers:
                    # 尝试将值转换为数字
                    try:
                        value = float(row[header])
                        column_values[header].append(value)
                    except ValueError:
                        # 如果转换失败，跳过该值（非数值列）
                        pass
        
        # 计算每列的平均值
        averages = {}
        for column, values in column_values.items():
            if values:  # 确保列中有数值
                averages[column] = sum(values) / len(values)
            else:
                averages[column] = None  # 非数值列标记为None
        
        return averages
    
    except FileNotFoundError:
        print(f"错误：找不到文件 {csv_file_path}")
        return {}
    except Exception as e:
        print(f"处理文件时出错：{e}")
        return {}

def calculate_row_sums(csv_file_path):
    """
    读取CSV文件并计算每行数值的总和
    
    Args:
        csv_file_path (str): CSV文件路径
    
    Returns:
        list: 包含每行总和的列表
    """
    row_sums = []
    
    try:
        # 读取CSV文件
        with open(csv_file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # 获取列名
            headers = reader.fieldnames
            
            # 遍历每一行
            for row_num, row in enumerate(reader, start=1):
                row_sum = 0
                for header in headers:
                    # 尝试将值转换为数字并累加
                    try:
                        value = float(row[header])
                        row_sum += value
                    except ValueError:
                        # 如果转换失败，跳过该值（非数值列）
                        pass
                row_sums.append(row_sum)
                print(f"第{row_num}行总和: {row_sum:.2f}")
        
        return row_sums
    
    except FileNotFoundError:
        print(f"错误：找不到文件 {csv_file_path}")
        return []
    except Exception as e:
        print(f"处理文件时出错：{e}")
        return []

def main():
    # 如果命令行提供了文件路径，则使用该路径，否则使用默认路径
    if len(sys.argv) > 1:
        csv_file_path = sys.argv[1]
    else:
        csv_file_path = "/workspace/sample_data.csv"
    
    print(f"正在处理文件: {csv_file_path}")
    
    # 计算每行总和
    print("\n每行数值总和:")
    print("-" * 30)
    row_sums = calculate_row_sums(csv_file_path)
    
    # 计算平均值
    averages = calculate_column_averages(csv_file_path)
    
    # 输出结果
    if averages:
        print("\n各列平均值:")
        print("-" * 30)
        for column, average in averages.items():
            if average is not None:
                print(f"{column}: {average:.2f}")
            else:
                print(f"{column}: 非数值列")
    else:
        print("未能计算平均值，请检查文件格式。")

if __name__ == "__main__":
    main()
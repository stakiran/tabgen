# encoding: utf-8

import configparser
import os
import sys

def dp(msg):
    if use_debug:
        print('[Debug] {}'.format(msg))

def file2list(filepath):
    ret = []
    with open(filepath, encoding='utf8', mode='r') as f:
        ret = [line.rstrip('\n') for line in f.readlines()]
    return ret

def list2file(filepath, ls):
    with open(filepath, encoding='utf8', mode='w') as f:
        f.writelines(['{:}\n'.format(line) for line in ls] )

def parse_arguments():
    import argparse

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument('-i', '--input', default=None, required=True,
        help='An input filename.')

    parser.add_argument('-o', '--output', default=None,
        help='[Not Supported Yet]An output filename.')

    parser.add_argument('--debug', default=False, action='store_true',
        help='[Debug] Debug mode. display debug print etc.')

    args = parser.parse_args()
    return args

MYFULLPATH = os.path.abspath(sys.argv[0])
MYDIR = os.path.dirname(MYFULLPATH)

def ____parse_arguments___():
    pass

args = parse_arguments()

use_debug = args.debug

infile_name = args.input
INFILE_FULL = os.path.join(MYDIR, infile_name)
outfile_name = args.output
if outfile_name==None:
    outfile_name = infile_name + '.md'
OUTFILE_FULL = os.path.join(MYDIR, outfile_name)

dp(INFILE_FULL)
dp(OUTFILE_FULL)

def ____loading____():
    pass

ini = configparser.ConfigParser(
    allow_no_value=True
)
ini.read(INFILE_FULL, 'UTF-8')

sectionnames = ini.sections()
dp(sectionnames)

section_columns = ini['column']
columns_by_str = list(section_columns.keys())[0]
dp(columns_by_str)

section_rows = ini['row']
rownames = list(section_rows.keys())
dp(rownames)

section_elements = ini['element']
elementlines = list(section_elements.keys())
dp(elementlines)

section_head = ini['column_head']
column_head_name = list(section_head.keys())[0]
dp(column_head_name)

section_tail = ini['column_tail']
column_tail_name = list(section_tail.keys())[0]
dp(column_tail_name)

section_mark = ini['mark']
marks = {}
for k in list(section_mark.keys()):
    v = section_mark.get(k)
    marks[k] = v
dp(marks)

section_option = ini['option']
options = {}
for k in list(section_option.keys()):
    v = section_option.get(k)
    options[k] = v
dp(options)

dp('===========================')

def ____construct____():
    pass

DELIMITOR_COLUMN = options['delimitor_column']

columns = columns_by_str.split(DELIMITOR_COLUMN)
NUMBER_OF_COLUMN = len(columns)
line_header = ''
for column in columns:
    line_header += '| {} '.format(column)
line_header += '|'

line_boundary = ''
for _ in range(NUMBER_OF_COLUMN):
    line_boundary += '| --- '
line_boundary += '|'

lines_body = []
tail_values = []
for elementline in elementlines:
    values_by_one_char = elementline[:NUMBER_OF_COLUMN]
    rest_value = elementline[NUMBER_OF_COLUMN:]
    rest_value = rest_value.strip()
    tail_values.append(rest_value)

    line = '|'
    for value in values_by_one_char:
        k = value
        converted_mark = k
        if k in marks:
            converted_mark = marks[k]
        line += ' {} |'.format(converted_mark)
    lines_body.append(line)

out_lines = []
out_lines.append(line_header)
out_lines.append(line_boundary)
out_lines.extend(lines_body)

# add head column
for i,line in enumerate(out_lines):
    headstr = ''

    if i==0:
        headstr = column_head_name
    elif i==1:
        headstr = '---'
    else:
        idx = i-2
        headstr = rownames[idx]

    newline = '| {} {}'.format(headstr, line)
    out_lines[i] = newline

# add tail column
for i,line in enumerate(out_lines):
    tailstr = ''

    if i==0:
        tailstr = column_tail_name
    elif i==1:
        tailstr = '---'
    else:
        idx = i-2
        tailstr = tail_values[idx]

    newline = '{} {} |'.format(line, tailstr)
    out_lines[i] = newline

for line in out_lines:
    print(line)

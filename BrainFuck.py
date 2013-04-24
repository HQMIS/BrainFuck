#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Copyright (c) 2013 HQM <qiminis0801@gmail.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

# Hello World!: ++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.

import re

MAXLEN = 10


def str2bf(STR):
    index = 0
    pre_index = 0
    diffValue = 10000
    baseBF = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]'  # [0, 70, 100, 30, 10]
    baseStr = [0, 70, 100, 30, 10]
    strList = [ord(i) for i in list(STR)]
    for i in list(STR):
        num = ord(i)
        for j in xrange(5):
            dValue = num - baseStr[j]
            if abs(dValue) < abs(diffValue):
                diffValue = dValue
                index = j
        diff_index = index - pre_index
        baseBF = baseBF + '>' * abs(diff_index) if diff_index > 0 else baseBF + '<' * abs(diff_index)
        baseBF = baseBF + '+' * abs(diffValue) + '.' if diffValue > 0 else baseBF + '-' * abs(diffValue) + '.'
        pre_index = index
        baseStr[index] = num
        index = 0
        diffValue = 10000
    print baseBF


def bf2str(BF):
    BeginEndDict = {}
    EndBeginDict = {}
    whileBeginList = []
    resultList = []
    for index, item in enumerate(BF):
        if '[' == item:
            whileBeginList.append(index)
        elif ']' == item:
            BeginEndDict[whileBeginList[-1]] = index
            EndBeginDict[index] = whileBeginList[-1]
            whileBeginList = whileBeginList[:-1]
        else:
            pass

    i = 0  # index of list strList
    j = 0  # index of string BF
    strList = [0] * MAXLEN

    BFLen = len(BF)
    while j < BFLen:
        item = BF[j]
        if '+' == item:
            strList[i] += 1
        elif '-' == item:
            strList[i] -= 1
        elif '>' == item:
            i += 1
        elif '<' == item:
            i -= 1
        elif ',' == item:
            try:
                strList[i] = ord(raw_input())
            except:
                strList[i] = 13
        elif '.' == item:
            resultList.append(chr(strList[i]))
        elif '[' == item:
            if 0 == strList[i]:
                j = BeginEndDict[j]
            else:
                pass
        elif ']' == item:
            if 0 == strList[i]:
                pass
            else:
                j = EndBeginDict[j]
        j += 1
    print ''.join(resultList)


def main():
    transStr = raw_input('Input a String:')

    m = re.match(r'[\[+-><.,\]]+', transStr)
    try:
        if m:
            str2bf(transStr) if cmp(transStr, m.group(0)) else bf2str(transStr)
        else:
            str2bf(transStr)
    except:
        print 'error!'

if __name__ == "__main__":
    main()

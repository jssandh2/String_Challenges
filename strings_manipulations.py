__author__ = 'Jus'

import string
import math
import json


class string_challenges:

    def __init__(self):
        self.string_input_1 = None
        self.string_input_2 = None
        self.string_output = None
        self.boolean_return = None
        self.hash_table_1 = {}
        self.hash_table_2 = {}
        self.list_one = []
        self.list_two = []

    def areStringCharactersUnique(self, string_1=str):     # O(n)
        split_array_one = list(string_1)
        for i in range(len(split_array_one)):
            if split_array_one[i] in self.hash_table_1:
                self.boolean_return = False
                return self.boolean_return
            else:
                self.hash_table_1[split_array_one[i]] = 1

    def areTwoStringsAmbigrams(self, string_1=str, string_2=str):       # O(n)
        self.string_input_1 = string_1
        self.string_input_2 = string_2
        split_array_one = list(string_1)
        split_array_two = list(string_2)
        if len(split_array_two) != len(split_array_one):
            self.boolean_return = False
            return self.boolean_return
        else:
            for i in range(len(split_array_one)):
                if split_array_one[i] in self.hash_table_1:
                    self.hash_table_1[split_array_one[i]] += 1
                else:
                    self.hash_table_1[split_array_one[i]] = 1
            for j in range(len(split_array_two)):
                if split_array_two[j] in self.hash_table_2:
                    self.hash_table_2[split_array_two[j]] += 1
                else:
                    self.hash_table_2[split_array_two[j]] = 1
            for key in self.hash_table_1:
                if key in self.hash_table_2:
                    if self.hash_table_1[key] == self.hash_table_2[key]:
                        continue
                else:
                    self.boolean_return = False
                    return self.boolean_return
            self.boolean_return = True
            return self.boolean_return

    def reverseString(self, string_1=str):      # O(n)
        split_null_char = string_1.split("\n")
        self.string_input_1 = split_null_char[0]
        split_all = list(self.string_input_1)
        for i in range(len(split_all)):
            self.list_one.append(split_all[len(split_all) - 1 - i])
        self.string_output = ''.join(self.list_one)
        # Join list into a string. Avoids String buffer problem.
        return self.string_output

    def countAndReturn(self, string_1=str):     # O(n)
        split_all = list(string_1)
        putwithdash = False
        curr_pos = 0
        curr_char = None
        list_return = []
        for i in range(len(split_all)):
            if split_all[i] in self.hash_table_1:
                if i - self.hash_table_1[split_all[i]][0] > 1 and putwithdash is False:
                    self.hash_table_1[split_all[i] + "_" + str(i)] = [i, 1]
                    curr_pos = i
                    putwithdash = True
                    curr_char = split_all[i]
                    list_return.append(split_all[i] + "_" + str(i))
                elif i - self.hash_table_1[split_all[i]][0] > 1 and putwithdash is True:
                    if curr_char == split_all[i]:
                        self.hash_table_1[split_all[i] + "_" + str(curr_pos)][1] += 1
                        self.hash_table_1[split_all[i] + "_" + str(curr_pos)][0] += 1
                    else:
                        self.hash_table_1[split_all[i] + "_" + str(i)] = [i, 1]
                        curr_pos = i
                        curr_char = split_all[i]
                        list_return.append(split_all[i] + "_" + str(i))
                elif i - self.hash_table_1[split_all[i]][0] == 1 and putwithdash is True:
                    continue        # this can never happen in my implementation
                else:   # Difference of one, and being met first time in repetition
                    self.hash_table_1[split_all[i]][1] += 1
                    self.hash_table_1[split_all[i]][0] += 1
            else:
                if putwithdash is True:
                    self.hash_table_1[split_all[i]] = [i, 1]
                    putwithdash = False
                    list_return.append(split_all[i])
                else:
                    self.hash_table_1[split_all[i]] = [i, 1]
                    list_return.append(split_all[i])
        # string_output = ''.join(list_return)
        list_return_final = []
        for i in range(len(list_return)):
            list_return_final.append(list_return[i].split("_")[0] + str(self.hash_table_1[list_return[i]][1]))
        # Join the list again, avoiding the problem of the String buffer.
        string_output = ''.join(list_return_final)
        if len(list(string_output)) < len(split_all):
            return string_output
        else:
            return string_1

    def mXnMatrixtoZero(self, matrix_0_1):      # O(mn)
        list_markers = []
        list_zeroes = []
        for i in range(len(matrix_0_1)):
            list_zeroes.append('0')
            for j in range(len(matrix_0_1[0]) - 1):
                list_zeroes.append('0')
        for i in range(len(matrix_0_1)):
            if matrix_0_1[i][0] == '0':
                list_markers.append((1, (i, 0)))
            else:
                for j in range(len(matrix_0_1[i])):
                    if matrix_0_1[i][j] == '0':
                        list_markers.append((1, (i, j)))
                        break
        for i in range(len(list_markers)):
            if list_markers[i][0] == 1:
                for j in range(len(matrix_0_1)):
                    matrix_0_1[list_markers[i][1][0]] = list_zeroes[j]
                    for k in range(len(matrix_0_1[j]) - 1):
                        matrix_0_1[list_markers[i][1][0]][list_markers[i][1][1]] = list_zeroes[j + k]
        return matrix_0_1

    def isSubstring(self, string_1=str, string_2=str):      # O(n^2)
        split_main = list(string_1)
        split_sub =  list(string_2)
        if len(split_main) < len(split_sub):
            return False
        else:
            for i in range(len(split_main)):
                if split_main[i] in self.hash_table_1:
                    self.hash_table_1[split_main[i]][0] += 1
                    self.hash_table_1[split_main[i]][1].append(i)
                else:
                    self.hash_table_1[split_main[i]] = (1, [i])
            for j in range(len(split_sub)):
                if split_sub[j] in self.hash_table_2:
                    self.hash_table_2[split_sub[j]][0] += 1
                    self.hash_table_1[split_main[j]][1].append(j)
                else:
                    self.hash_table_2[split_sub[j]] = (1, [j])
            position_last = 0
            frequency_curr = {}
            for key in self.hash_table_2:
                if key in self.hash_table_1:
                    if key in frequency_curr:
                        time_visited = frequency_curr[key] + 1
                        if time_visited < len(self.hash_table_2[key][1]):
                            if position_last < self.hash_table_2[key][1][time_visited]:
                                continue
                            else:
                                return False
                        else:
                            return False
                    else:
                        frequency_curr[key] = 0
                        time_visited = frequency_curr[key]
                        if time_visited < len(self.hash_table_2[key][1]):
                            if position_last < self.hash_table_2[key][1][time_visited]:
                                continue
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
            return True

    def isRotation(self, string_1=str, string_2=str):       # O(n^2)
        string_1_1 = string_1 + string_1
        return string_challenges.isSubstring(self, string_1_1, string_2)

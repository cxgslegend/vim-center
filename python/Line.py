import json
import urllib.request
import vim
from math import log10, floor

class Line:
    def __init__(self):
        self.text_within_delimiters_length = 80

    # Functions for vim to call
    def center_line(self):
        self.current_line = self.text_centered_within_delimiters

    def center_line_of_length(self, width):
        self.text_within_delimiters_length = int(width)
        self.center_line()

    # Properties
    '''
    row property getter
    '''
    @property
    def row(self):
        return vim.current.window.cursor[0]

    '''
    column property getter
    '''
    @property
    def column(self):
        return vim.current.window.cursor[1]

    '''
    text_centered_within_delimiters property getter
    '''
    @property
    def text_centered_within_delimiters(self):
        delimiter = self.delimiter
        center_of_line = self.text_within_delimiters
        total_width = self.text_within_delimiters_length

        if total_width <= 0:
            return ""

        delimiter_length_on_one_side = len(delimiter)
        delimiter_length_on_both_sides = delimiter_length_on_one_side * 2
        center_of_line_length = len(center_of_line)
        optimal_number_of_spaces = 2
        minimum_number_of_delimiters = 2
        center_of_line_minimum_width = 1

        # If we can fit everything we want and still have unused space, we need to add spaces to the center_of_line
        if delimiter_length_on_both_sides + center_of_line_length + optimal_number_of_spaces <= total_width:
            return delimiter + center_of_line.center(total_width - delimiter_length_on_both_sides, ' ') + delimiter
        # Else if we cannot fit everything we want to, but we can make space by truncating only the center_of_line
        elif delimiter_length_on_both_sides + optimal_number_of_spaces + center_of_line_minimum_width <= total_width:
            truncated_string_length = total_width - \
                    delimiter_length_on_both_sides - \
                    optimal_number_of_spaces - \
                    center_of_line_minimum_width
            return delimiter + " " + center_of_line[:truncated_string_length + 1] + " " + delimiter
        # Else if we have truncated the center_of_line as much as we can, and we still cannot fit everything else we need,
        # then truncate the delimiters
        elif optimal_number_of_spaces + center_of_line_minimum_width + minimum_number_of_delimiters <= total_width:
            total_delimiter_width = total_width - optimal_number_of_spaces - center_of_line_minimum_width
            right_delimiter_width = total_delimiter_width // 2
            left_delimiter_width = total_delimiter_width - right_delimiter_width
            return delimiter[0] * left_delimiter_width + " " + center_of_line[0] + " " + delimiter[0] * right_delimiter_width
        elif center_of_line_minimum_width + minimum_number_of_delimiters <= total_width:
            total_space = total_width - center_of_line_minimum_width - minimum_number_of_delimiters
            right_space_width = total_space // 2
            left_space_width = total_space - right_space_width
            return delimiter[0] + " " * left_space_width + center_of_line[0] + " " * right_space_width + delimiter[0]
        else:
            return center_of_line[0: total_width]


    '''
    text_within_delimiters property getter
    '''
    @property
    def text_within_delimiters(self):
        if self.current_line == "":
            return ''
        left_character, left_character_count = self.count_consecutive_chars(self.current_line)
        right_character, right_character_count = self.count_consecutive_chars(self.current_line[::-1])
        if right_character.isalnum() and left_character.isalnum():
            return self.current_line.strip()
        elif right_character.isalnum():
            return self.current_line[left_character_count:].strip()
        elif left_character.isalnum():
            return self.current_line[:-right_character_count].strip()
        else:
            return self.current_line[left_character_count: -right_character_count].strip()

    '''
    delimiter property getter
    '''
    @property
    def delimiter(self):
        if self.current_line == "":
            return '*'
        left_character, left_character_count = self.count_consecutive_chars(self.current_line)
        right_character, right_character_count = self.count_consecutive_chars(self.current_line[::-1])
        has_left_delimiter = (left_character_count > 0) and (not left_character.isalnum())
        has_right_delimiter = (right_character_count > 0) and (not right_character.isalnum())
        if has_left_delimiter and has_right_delimiter:
            return left_character * max(left_character_count, right_character_count)
        elif has_left_delimiter:
            return left_character * left_character_count
        elif has_right_delimiter:
            return right_character * right_character_count
        else:
            return '*'

    '''
    current_line property getter/setter
    '''
    @property
    def current_line(self):
        return vim.current.buffer[self.row - 1].strip()

    @current_line.setter
    def current_line(self, current_line):
        vim.current.buffer[self.row - 1] = current_line

    '''
    text_within_delimiters_length property getter/setter
    '''
    @property
    def text_within_delimiters_length(self):
        return self.__text_within_delimiters_length

    @text_within_delimiters_length.setter
    def text_within_delimiters_length(self, text_within_delimiters_length):
        self.__text_within_delimiters_length = text_within_delimiters_length


    ################################################################################
    #####                           Private methods                            #####
    ################################################################################
    def count_consecutive_chars(self, line):
        if len(line) > 0:
            character_to_match = line[0]
        character_count = 0
        for character in line:
            if character_to_match == character:
                character_count += 1
            else:
                break
        # if the amount of consecutive chars is the whole string length, we need to return an error
        if character_count == len(line):
            raise ValueError()
        return character_to_match, character_count

    def print_width(self, width):
        for i in range(width):
            if (i + 1) % 10 == 0:
                print(((i + 1) // 10) % 10, end='')
            else:
                print((i + 1) % 10, end='')
            print(('' if width == 0 else ' ') + '({})'.format(width))

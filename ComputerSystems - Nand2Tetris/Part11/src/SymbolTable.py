# Symbol Table for storing type, kind, index and name of variables

global subroutine_symbols
global symbol_table
subroutine_symbols = {}
symbol_table = {}

local_count = 0


def initialize_subroutine_symbols():
    subroutine_table = {}
    argument_count = 0
    local_count = 0
    subroutine_total = 0

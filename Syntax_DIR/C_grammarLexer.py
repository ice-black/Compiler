# Generated from C_grammar.g4 by ANTLR 4.12.0
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,38,273,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,
        2,6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,
        13,7,13,2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,
        19,2,20,7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,
        26,7,26,2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,
        32,2,33,7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,1,0,1,0,1,0,
        1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,3,1,3,1,3,1,4,
        1,4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,9,1,10,1,10,1,10,1,
        10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,1,11,1,12,1,12,1,12,1,
        12,1,12,1,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,15,1,
        15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,1,19,1,19,1,20,1,20,1,20,1,
        21,1,21,1,21,1,21,1,22,1,22,1,22,1,22,1,22,1,22,1,23,1,23,1,23,1,
        23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,
        25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,27,1,28,1,28,1,
        28,1,28,1,28,1,28,1,28,1,28,1,28,3,28,197,8,28,1,29,1,29,5,29,201,
        8,29,10,29,12,29,204,9,29,1,30,4,30,207,8,30,11,30,12,30,208,1,31,
        4,31,212,8,31,11,31,12,31,213,1,31,1,31,4,31,218,8,31,11,31,12,31,
        219,1,32,1,32,4,32,224,8,32,11,32,12,32,225,1,32,1,32,1,32,1,32,
        1,33,1,33,1,33,1,33,1,34,1,34,5,34,238,8,34,10,34,12,34,241,9,34,
        1,34,1,34,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,1,35,3,35,254,
        8,35,1,36,1,36,1,36,1,36,5,36,260,8,36,10,36,12,36,263,9,36,1,36,
        1,36,1,37,4,37,268,8,37,11,37,12,37,269,1,37,1,37,0,0,38,1,1,3,2,
        5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,25,13,27,14,29,
        15,31,16,33,17,35,18,37,19,39,20,41,21,43,22,45,23,47,24,49,25,51,
        26,53,27,55,28,57,29,59,30,61,31,63,32,65,33,67,34,69,35,71,36,73,
        37,75,38,1,0,8,2,0,60,60,62,62,3,0,65,90,95,95,97,122,4,0,48,57,
        65,90,95,95,97,122,1,0,48,57,2,0,65,90,97,122,1,0,34,34,2,0,10,10,
        13,13,3,0,9,10,13,13,32,32,285,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,
        0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,
        0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,
        0,27,1,0,0,0,0,29,1,0,0,0,0,31,1,0,0,0,0,33,1,0,0,0,0,35,1,0,0,0,
        0,37,1,0,0,0,0,39,1,0,0,0,0,41,1,0,0,0,0,43,1,0,0,0,0,45,1,0,0,0,
        0,47,1,0,0,0,0,49,1,0,0,0,0,51,1,0,0,0,0,53,1,0,0,0,0,55,1,0,0,0,
        0,57,1,0,0,0,0,59,1,0,0,0,0,61,1,0,0,0,0,63,1,0,0,0,0,65,1,0,0,0,
        0,67,1,0,0,0,0,69,1,0,0,0,0,71,1,0,0,0,0,73,1,0,0,0,0,75,1,0,0,0,
        1,77,1,0,0,0,3,86,1,0,0,0,5,88,1,0,0,0,7,90,1,0,0,0,9,95,1,0,0,0,
        11,97,1,0,0,0,13,99,1,0,0,0,15,101,1,0,0,0,17,103,1,0,0,0,19,105,
        1,0,0,0,21,108,1,0,0,0,23,116,1,0,0,0,25,121,1,0,0,0,27,127,1,0,
        0,0,29,134,1,0,0,0,31,136,1,0,0,0,33,138,1,0,0,0,35,140,1,0,0,0,
        37,142,1,0,0,0,39,144,1,0,0,0,41,147,1,0,0,0,43,150,1,0,0,0,45,154,
        1,0,0,0,47,160,1,0,0,0,49,165,1,0,0,0,51,172,1,0,0,0,53,177,1,0,
        0,0,55,182,1,0,0,0,57,196,1,0,0,0,59,198,1,0,0,0,61,206,1,0,0,0,
        63,211,1,0,0,0,65,221,1,0,0,0,67,231,1,0,0,0,69,235,1,0,0,0,71,253,
        1,0,0,0,73,255,1,0,0,0,75,267,1,0,0,0,77,78,5,35,0,0,78,79,5,105,
        0,0,79,80,5,110,0,0,80,81,5,99,0,0,81,82,5,108,0,0,82,83,5,117,0,
        0,83,84,5,100,0,0,84,85,5,101,0,0,85,2,1,0,0,0,86,87,5,40,0,0,87,
        4,1,0,0,0,88,89,5,41,0,0,89,6,1,0,0,0,90,91,5,109,0,0,91,92,5,97,
        0,0,92,93,5,105,0,0,93,94,5,110,0,0,94,8,1,0,0,0,95,96,5,59,0,0,
        96,10,1,0,0,0,97,98,5,44,0,0,98,12,1,0,0,0,99,100,5,123,0,0,100,
        14,1,0,0,0,101,102,5,125,0,0,102,16,1,0,0,0,103,104,5,61,0,0,104,
        18,1,0,0,0,105,106,5,105,0,0,106,107,5,102,0,0,107,20,1,0,0,0,108,
        109,5,101,0,0,109,110,5,108,0,0,110,111,5,115,0,0,111,112,5,101,
        0,0,112,113,5,32,0,0,113,114,5,105,0,0,114,115,5,102,0,0,115,22,
        1,0,0,0,116,117,5,101,0,0,117,118,5,108,0,0,118,119,5,115,0,0,119,
        120,5,101,0,0,120,24,1,0,0,0,121,122,5,119,0,0,122,123,5,104,0,0,
        123,124,5,105,0,0,124,125,5,108,0,0,125,126,5,101,0,0,126,26,1,0,
        0,0,127,128,5,114,0,0,128,129,5,101,0,0,129,130,5,116,0,0,130,131,
        5,117,0,0,131,132,5,114,0,0,132,133,5,110,0,0,133,28,1,0,0,0,134,
        135,5,43,0,0,135,30,1,0,0,0,136,137,5,45,0,0,137,32,1,0,0,0,138,
        139,5,42,0,0,139,34,1,0,0,0,140,141,5,47,0,0,141,36,1,0,0,0,142,
        143,5,37,0,0,143,38,1,0,0,0,144,145,5,38,0,0,145,146,5,38,0,0,146,
        40,1,0,0,0,147,148,5,124,0,0,148,149,5,124,0,0,149,42,1,0,0,0,150,
        151,5,105,0,0,151,152,5,110,0,0,152,153,5,116,0,0,153,44,1,0,0,0,
        154,155,5,102,0,0,155,156,5,108,0,0,156,157,5,111,0,0,157,158,5,
        97,0,0,158,159,5,116,0,0,159,46,1,0,0,0,160,161,5,99,0,0,161,162,
        5,104,0,0,162,163,5,97,0,0,163,164,5,114,0,0,164,48,1,0,0,0,165,
        166,5,100,0,0,166,167,5,111,0,0,167,168,5,117,0,0,168,169,5,98,0,
        0,169,170,5,108,0,0,170,171,5,101,0,0,171,50,1,0,0,0,172,173,5,118,
        0,0,173,174,5,111,0,0,174,175,5,105,0,0,175,176,5,100,0,0,176,52,
        1,0,0,0,177,178,5,98,0,0,178,179,5,111,0,0,179,180,5,111,0,0,180,
        181,5,108,0,0,181,54,1,0,0,0,182,183,5,108,0,0,183,184,5,111,0,0,
        184,185,5,110,0,0,185,186,5,103,0,0,186,56,1,0,0,0,187,188,5,61,
        0,0,188,197,5,61,0,0,189,190,5,33,0,0,190,197,5,61,0,0,191,197,7,
        0,0,0,192,193,5,60,0,0,193,197,5,61,0,0,194,195,5,62,0,0,195,197,
        5,61,0,0,196,187,1,0,0,0,196,189,1,0,0,0,196,191,1,0,0,0,196,192,
        1,0,0,0,196,194,1,0,0,0,197,58,1,0,0,0,198,202,7,1,0,0,199,201,7,
        2,0,0,200,199,1,0,0,0,201,204,1,0,0,0,202,200,1,0,0,0,202,203,1,
        0,0,0,203,60,1,0,0,0,204,202,1,0,0,0,205,207,7,3,0,0,206,205,1,0,
        0,0,207,208,1,0,0,0,208,206,1,0,0,0,208,209,1,0,0,0,209,62,1,0,0,
        0,210,212,7,3,0,0,211,210,1,0,0,0,212,213,1,0,0,0,213,211,1,0,0,
        0,213,214,1,0,0,0,214,215,1,0,0,0,215,217,5,46,0,0,216,218,7,3,0,
        0,217,216,1,0,0,0,218,219,1,0,0,0,219,217,1,0,0,0,219,220,1,0,0,
        0,220,64,1,0,0,0,221,223,5,60,0,0,222,224,7,4,0,0,223,222,1,0,0,
        0,224,225,1,0,0,0,225,223,1,0,0,0,225,226,1,0,0,0,226,227,1,0,0,
        0,227,228,5,46,0,0,228,229,5,104,0,0,229,230,5,62,0,0,230,66,1,0,
        0,0,231,232,5,39,0,0,232,233,9,0,0,0,233,234,5,39,0,0,234,68,1,0,
        0,0,235,239,5,34,0,0,236,238,8,5,0,0,237,236,1,0,0,0,238,241,1,0,
        0,0,239,237,1,0,0,0,239,240,1,0,0,0,240,242,1,0,0,0,241,239,1,0,
        0,0,242,243,5,34,0,0,243,70,1,0,0,0,244,245,5,116,0,0,245,246,5,
        114,0,0,246,247,5,117,0,0,247,254,5,101,0,0,248,249,5,102,0,0,249,
        250,5,97,0,0,250,251,5,108,0,0,251,252,5,115,0,0,252,254,5,101,0,
        0,253,244,1,0,0,0,253,248,1,0,0,0,254,72,1,0,0,0,255,256,5,47,0,
        0,256,257,5,47,0,0,257,261,1,0,0,0,258,260,8,6,0,0,259,258,1,0,0,
        0,260,263,1,0,0,0,261,259,1,0,0,0,261,262,1,0,0,0,262,264,1,0,0,
        0,263,261,1,0,0,0,264,265,6,36,0,0,265,74,1,0,0,0,266,268,7,7,0,
        0,267,266,1,0,0,0,268,269,1,0,0,0,269,267,1,0,0,0,269,270,1,0,0,
        0,270,271,1,0,0,0,271,272,6,37,0,0,272,76,1,0,0,0,11,0,196,202,208,
        213,219,225,239,253,261,269,1,6,0,0
    ]

class C_grammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    CONDITIONAL_OPERATOR = 29
    IDENTIFIER = 30
    INTEGER = 31
    FLOAT = 32
    INCLUDE_DIRECTIVE = 33
    CHAR_LITERAL = 34
    STRING_LITERAL = 35
    BOOLEAN = 36
    SING_LINE_COMMENT = 37
    WS = 38

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'#include'", "'('", "')'", "'main'", "';'", "','", "'{'", "'}'", 
            "'='", "'if'", "'else if'", "'else'", "'while'", "'return'", 
            "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'", "'int'", 
            "'float'", "'char'", "'double'", "'void'", "'bool'", "'long'" ]

    symbolicNames = [ "<INVALID>",
            "CONDITIONAL_OPERATOR", "IDENTIFIER", "INTEGER", "FLOAT", "INCLUDE_DIRECTIVE", 
            "CHAR_LITERAL", "STRING_LITERAL", "BOOLEAN", "SING_LINE_COMMENT", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "T__12", "T__13", 
                  "T__14", "T__15", "T__16", "T__17", "T__18", "T__19", 
                  "T__20", "T__21", "T__22", "T__23", "T__24", "T__25", 
                  "T__26", "T__27", "CONDITIONAL_OPERATOR", "IDENTIFIER", 
                  "INTEGER", "FLOAT", "INCLUDE_DIRECTIVE", "CHAR_LITERAL", 
                  "STRING_LITERAL", "BOOLEAN", "SING_LINE_COMMENT", "WS" ]

    grammarFileName = "C_grammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.12.0")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



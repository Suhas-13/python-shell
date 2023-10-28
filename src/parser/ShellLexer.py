# Generated from src/parser/Shell.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,9,61,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,1,0,1,0,1,1,1,1,1,2,1,2,1,2,1,3,1,3,1,4,1,
        4,5,4,31,8,4,10,4,12,4,34,9,4,1,5,4,5,37,8,5,11,5,12,5,38,1,6,1,
        6,5,6,43,8,6,10,6,12,6,46,9,6,1,6,1,6,1,7,4,7,51,8,7,11,7,12,7,52,
        1,8,4,8,56,8,8,11,8,12,8,57,1,8,1,8,0,0,9,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,17,9,1,0,6,3,0,65,90,95,95,97,122,4,0,48,57,65,90,95,
        95,97,122,5,0,32,32,34,34,60,60,62,62,124,124,1,0,34,34,4,0,32,32,
        60,60,62,62,124,124,3,0,9,10,13,13,32,32,65,0,1,1,0,0,0,0,3,1,0,
        0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,0,
        0,0,15,1,0,0,0,0,17,1,0,0,0,1,19,1,0,0,0,3,21,1,0,0,0,5,23,1,0,0,
        0,7,26,1,0,0,0,9,28,1,0,0,0,11,36,1,0,0,0,13,40,1,0,0,0,15,50,1,
        0,0,0,17,55,1,0,0,0,19,20,5,124,0,0,20,2,1,0,0,0,21,22,5,62,0,0,
        22,4,1,0,0,0,23,24,5,62,0,0,24,25,5,62,0,0,25,6,1,0,0,0,26,27,5,
        60,0,0,27,8,1,0,0,0,28,32,7,0,0,0,29,31,7,1,0,0,30,29,1,0,0,0,31,
        34,1,0,0,0,32,30,1,0,0,0,32,33,1,0,0,0,33,10,1,0,0,0,34,32,1,0,0,
        0,35,37,8,2,0,0,36,35,1,0,0,0,37,38,1,0,0,0,38,36,1,0,0,0,38,39,
        1,0,0,0,39,12,1,0,0,0,40,44,5,34,0,0,41,43,8,3,0,0,42,41,1,0,0,0,
        43,46,1,0,0,0,44,42,1,0,0,0,44,45,1,0,0,0,45,47,1,0,0,0,46,44,1,
        0,0,0,47,48,5,34,0,0,48,14,1,0,0,0,49,51,8,4,0,0,50,49,1,0,0,0,51,
        52,1,0,0,0,52,50,1,0,0,0,52,53,1,0,0,0,53,16,1,0,0,0,54,56,7,5,0,
        0,55,54,1,0,0,0,56,57,1,0,0,0,57,55,1,0,0,0,57,58,1,0,0,0,58,59,
        1,0,0,0,59,60,6,8,0,0,60,18,1,0,0,0,6,0,32,38,44,52,57,1,6,0,0
    ]

class ShellLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    COMMAND = 5
    ARG = 6
    QUOTED_ARG = 7
    FILE = 8
    WS = 9

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'|'", "'>'", "'>>'", "'<'" ]

    symbolicNames = [ "<INVALID>",
            "COMMAND", "ARG", "QUOTED_ARG", "FILE", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "COMMAND", "ARG", "QUOTED_ARG", 
                  "FILE", "WS" ]

    grammarFileName = "Shell.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None



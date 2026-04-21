# Generated from C:/Users/vooco/Documents/PPL_252/ASSIGNMENT_1/tyc-compiler/src/grammar/TyC.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,51,423,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,2,33,
        7,33,2,34,7,34,2,35,7,35,2,36,7,36,2,37,7,37,2,38,7,38,2,39,7,39,
        2,40,7,40,2,41,7,41,2,42,7,42,2,43,7,43,2,44,7,44,2,45,7,45,1,0,
        1,0,1,0,5,0,96,8,0,10,0,12,0,99,9,0,1,1,1,1,1,1,1,1,1,1,3,1,106,
        8,1,1,2,1,2,1,2,5,2,111,8,2,10,2,12,2,114,9,2,1,3,1,3,1,3,5,3,119,
        8,3,10,3,12,3,122,9,3,1,4,1,4,1,4,5,4,127,8,4,10,4,12,4,130,9,4,
        1,5,1,5,1,5,5,5,135,8,5,10,5,12,5,138,9,5,1,6,1,6,1,6,5,6,143,8,
        6,10,6,12,6,146,9,6,1,7,1,7,1,7,5,7,151,8,7,10,7,12,7,154,9,7,1,
        8,1,8,1,8,3,8,159,8,8,1,9,1,9,1,9,3,9,164,8,9,1,10,1,10,5,10,168,
        8,10,10,10,12,10,171,9,10,1,11,1,11,1,11,1,11,1,11,1,11,5,11,179,
        8,11,10,11,12,11,182,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        3,12,192,8,12,1,13,1,13,1,13,3,13,197,8,13,1,13,1,13,1,14,1,14,1,
        14,1,14,1,14,3,14,206,8,14,1,15,1,15,1,16,1,16,3,16,212,8,16,1,16,
        1,16,1,17,1,17,1,17,3,17,219,8,17,1,18,1,18,1,19,1,19,1,20,1,20,
        3,20,227,8,20,1,21,4,21,230,8,21,11,21,12,21,231,1,22,1,22,1,22,
        1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,1,22,3,22,246,8,22,1,23,
        1,23,1,23,1,23,3,23,252,8,23,1,24,1,24,3,24,256,8,24,1,25,1,25,5,
        25,260,8,25,10,25,12,25,263,9,25,1,25,1,25,1,26,1,26,1,26,1,26,1,
        26,1,26,1,26,3,26,274,8,26,1,27,1,27,1,27,1,27,1,27,1,27,1,28,1,
        28,1,28,3,28,285,8,28,1,28,1,28,3,28,289,8,28,1,28,1,28,3,28,293,
        8,28,1,28,1,28,1,28,1,29,1,29,3,29,300,8,29,1,30,1,30,1,30,1,30,
        1,31,1,31,1,31,1,31,1,31,1,31,1,31,1,31,4,31,314,8,31,11,31,12,31,
        315,3,31,318,8,31,1,32,1,32,1,32,1,32,1,32,1,32,5,32,326,8,32,10,
        32,12,32,329,9,32,1,32,3,32,332,8,32,1,32,5,32,335,8,32,10,32,12,
        32,338,9,32,1,32,1,32,1,33,1,33,1,33,1,33,5,33,346,8,33,10,33,12,
        33,349,9,33,1,34,1,34,1,34,5,34,354,8,34,10,34,12,34,357,9,34,1,
        35,1,35,1,35,1,36,1,36,1,36,1,37,1,37,1,37,1,38,1,38,3,38,370,8,
        38,1,38,1,38,1,39,1,39,5,39,376,8,39,10,39,12,39,379,9,39,1,39,1,
        39,1,40,1,40,1,40,1,40,5,40,387,8,40,10,40,12,40,390,9,40,1,40,1,
        40,1,40,1,41,1,41,1,41,1,41,1,42,1,42,1,43,3,43,402,8,43,1,43,1,
        43,1,43,3,43,407,8,43,1,43,1,43,1,43,1,44,1,44,1,44,5,44,415,8,44,
        10,44,12,44,418,9,44,1,45,1,45,1,45,1,45,0,1,22,46,0,2,4,6,8,10,
        12,14,16,18,20,22,24,26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,
        56,58,60,62,64,66,68,70,72,74,76,78,80,82,84,86,88,90,0,10,1,0,21,
        22,1,0,23,26,1,0,17,18,2,0,19,20,27,27,2,0,17,18,30,30,1,0,31,32,
        1,0,43,45,4,0,7,7,10,10,12,12,15,15,5,0,1,1,7,7,10,10,12,12,42,42,
        4,0,7,7,10,10,12,12,42,42,431,0,92,1,0,0,0,2,105,1,0,0,0,4,107,1,
        0,0,0,6,115,1,0,0,0,8,123,1,0,0,0,10,131,1,0,0,0,12,139,1,0,0,0,
        14,147,1,0,0,0,16,158,1,0,0,0,18,163,1,0,0,0,20,165,1,0,0,0,22,172,
        1,0,0,0,24,191,1,0,0,0,26,193,1,0,0,0,28,205,1,0,0,0,30,207,1,0,
        0,0,32,209,1,0,0,0,34,218,1,0,0,0,36,220,1,0,0,0,38,222,1,0,0,0,
        40,226,1,0,0,0,42,229,1,0,0,0,44,245,1,0,0,0,46,247,1,0,0,0,48,255,
        1,0,0,0,50,257,1,0,0,0,52,266,1,0,0,0,54,275,1,0,0,0,56,281,1,0,
        0,0,58,299,1,0,0,0,60,301,1,0,0,0,62,317,1,0,0,0,64,319,1,0,0,0,
        66,341,1,0,0,0,68,350,1,0,0,0,70,358,1,0,0,0,72,361,1,0,0,0,74,364,
        1,0,0,0,76,367,1,0,0,0,78,377,1,0,0,0,80,382,1,0,0,0,82,394,1,0,
        0,0,84,398,1,0,0,0,86,401,1,0,0,0,88,411,1,0,0,0,90,419,1,0,0,0,
        92,97,3,2,1,0,93,94,5,40,0,0,94,96,3,2,1,0,95,93,1,0,0,0,96,99,1,
        0,0,0,97,95,1,0,0,0,97,98,1,0,0,0,98,1,1,0,0,0,99,97,1,0,0,0,100,
        101,3,28,14,0,101,102,5,33,0,0,102,103,3,2,1,0,103,106,1,0,0,0,104,
        106,3,4,2,0,105,100,1,0,0,0,105,104,1,0,0,0,106,3,1,0,0,0,107,112,
        3,6,3,0,108,109,5,28,0,0,109,111,3,6,3,0,110,108,1,0,0,0,111,114,
        1,0,0,0,112,110,1,0,0,0,112,113,1,0,0,0,113,5,1,0,0,0,114,112,1,
        0,0,0,115,120,3,8,4,0,116,117,5,29,0,0,117,119,3,8,4,0,118,116,1,
        0,0,0,119,122,1,0,0,0,120,118,1,0,0,0,120,121,1,0,0,0,121,7,1,0,
        0,0,122,120,1,0,0,0,123,128,3,10,5,0,124,125,7,0,0,0,125,127,3,10,
        5,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,1,0,0,0,128,129,1,0,
        0,0,129,9,1,0,0,0,130,128,1,0,0,0,131,136,3,12,6,0,132,133,7,1,0,
        0,133,135,3,12,6,0,134,132,1,0,0,0,135,138,1,0,0,0,136,134,1,0,0,
        0,136,137,1,0,0,0,137,11,1,0,0,0,138,136,1,0,0,0,139,144,3,14,7,
        0,140,141,7,2,0,0,141,143,3,14,7,0,142,140,1,0,0,0,143,146,1,0,0,
        0,144,142,1,0,0,0,144,145,1,0,0,0,145,13,1,0,0,0,146,144,1,0,0,0,
        147,152,3,16,8,0,148,149,7,3,0,0,149,151,3,16,8,0,150,148,1,0,0,
        0,151,154,1,0,0,0,152,150,1,0,0,0,152,153,1,0,0,0,153,15,1,0,0,0,
        154,152,1,0,0,0,155,156,7,4,0,0,156,159,3,16,8,0,157,159,3,18,9,
        0,158,155,1,0,0,0,158,157,1,0,0,0,159,17,1,0,0,0,160,161,7,5,0,0,
        161,164,3,18,9,0,162,164,3,20,10,0,163,160,1,0,0,0,163,162,1,0,0,
        0,164,19,1,0,0,0,165,169,3,22,11,0,166,168,7,5,0,0,167,166,1,0,0,
        0,168,171,1,0,0,0,169,167,1,0,0,0,169,170,1,0,0,0,170,21,1,0,0,0,
        171,169,1,0,0,0,172,173,6,11,-1,0,173,174,3,24,12,0,174,180,1,0,
        0,0,175,176,10,2,0,0,176,177,5,34,0,0,177,179,5,42,0,0,178,175,1,
        0,0,0,179,182,1,0,0,0,180,178,1,0,0,0,180,181,1,0,0,0,181,23,1,0,
        0,0,182,180,1,0,0,0,183,192,3,30,15,0,184,192,3,32,16,0,185,192,
        3,26,13,0,186,192,5,42,0,0,187,188,5,37,0,0,188,189,3,2,1,0,189,
        190,5,38,0,0,190,192,1,0,0,0,191,183,1,0,0,0,191,184,1,0,0,0,191,
        185,1,0,0,0,191,186,1,0,0,0,191,187,1,0,0,0,192,25,1,0,0,0,193,194,
        5,42,0,0,194,196,5,37,0,0,195,197,3,0,0,0,196,195,1,0,0,0,196,197,
        1,0,0,0,197,198,1,0,0,0,198,199,5,38,0,0,199,27,1,0,0,0,200,201,
        3,22,11,0,201,202,5,34,0,0,202,203,5,42,0,0,203,206,1,0,0,0,204,
        206,5,42,0,0,205,200,1,0,0,0,205,204,1,0,0,0,206,29,1,0,0,0,207,
        208,7,6,0,0,208,31,1,0,0,0,209,211,5,35,0,0,210,212,3,0,0,0,211,
        210,1,0,0,0,211,212,1,0,0,0,212,213,1,0,0,0,213,214,5,36,0,0,214,
        33,1,0,0,0,215,219,3,36,18,0,216,219,5,42,0,0,217,219,5,1,0,0,218,
        215,1,0,0,0,218,216,1,0,0,0,218,217,1,0,0,0,219,35,1,0,0,0,220,221,
        7,7,0,0,221,37,1,0,0,0,222,223,7,8,0,0,223,39,1,0,0,0,224,227,3,
        36,18,0,225,227,5,42,0,0,226,224,1,0,0,0,226,225,1,0,0,0,227,41,
        1,0,0,0,228,230,3,44,22,0,229,228,1,0,0,0,230,231,1,0,0,0,231,229,
        1,0,0,0,231,232,1,0,0,0,232,43,1,0,0,0,233,234,3,46,23,0,234,235,
        5,39,0,0,235,246,1,0,0,0,236,246,3,52,26,0,237,246,3,54,27,0,238,
        246,3,56,28,0,239,246,3,64,32,0,240,246,3,70,35,0,241,246,3,72,36,
        0,242,246,3,50,25,0,243,246,3,74,37,0,244,246,3,76,38,0,245,233,
        1,0,0,0,245,236,1,0,0,0,245,237,1,0,0,0,245,238,1,0,0,0,245,239,
        1,0,0,0,245,240,1,0,0,0,245,241,1,0,0,0,245,242,1,0,0,0,245,243,
        1,0,0,0,245,244,1,0,0,0,246,45,1,0,0,0,247,248,3,38,19,0,248,251,
        5,42,0,0,249,250,5,33,0,0,250,252,3,48,24,0,251,249,1,0,0,0,251,
        252,1,0,0,0,252,47,1,0,0,0,253,256,3,2,1,0,254,256,3,32,16,0,255,
        253,1,0,0,0,255,254,1,0,0,0,256,49,1,0,0,0,257,261,5,35,0,0,258,
        260,3,44,22,0,259,258,1,0,0,0,260,263,1,0,0,0,261,259,1,0,0,0,261,
        262,1,0,0,0,262,264,1,0,0,0,263,261,1,0,0,0,264,265,5,36,0,0,265,
        51,1,0,0,0,266,267,5,9,0,0,267,268,5,37,0,0,268,269,3,2,1,0,269,
        270,5,38,0,0,270,273,3,44,22,0,271,272,5,6,0,0,272,274,3,44,22,0,
        273,271,1,0,0,0,273,274,1,0,0,0,274,53,1,0,0,0,275,276,5,16,0,0,
        276,277,5,37,0,0,277,278,3,2,1,0,278,279,5,38,0,0,279,280,3,44,22,
        0,280,55,1,0,0,0,281,282,5,8,0,0,282,284,5,37,0,0,283,285,3,58,29,
        0,284,283,1,0,0,0,284,285,1,0,0,0,285,286,1,0,0,0,286,288,5,39,0,
        0,287,289,3,2,1,0,288,287,1,0,0,0,288,289,1,0,0,0,289,290,1,0,0,
        0,290,292,5,39,0,0,291,293,3,62,31,0,292,291,1,0,0,0,292,293,1,0,
        0,0,293,294,1,0,0,0,294,295,5,38,0,0,295,296,3,44,22,0,296,57,1,
        0,0,0,297,300,3,46,23,0,298,300,3,60,30,0,299,297,1,0,0,0,299,298,
        1,0,0,0,300,59,1,0,0,0,301,302,3,28,14,0,302,303,5,33,0,0,303,304,
        3,2,1,0,304,61,1,0,0,0,305,306,3,28,14,0,306,307,5,33,0,0,307,308,
        3,2,1,0,308,318,1,0,0,0,309,310,7,5,0,0,310,318,3,18,9,0,311,313,
        3,22,11,0,312,314,7,5,0,0,313,312,1,0,0,0,314,315,1,0,0,0,315,313,
        1,0,0,0,315,316,1,0,0,0,316,318,1,0,0,0,317,305,1,0,0,0,317,309,
        1,0,0,0,317,311,1,0,0,0,318,63,1,0,0,0,319,320,5,14,0,0,320,321,
        5,37,0,0,321,322,3,2,1,0,322,323,5,38,0,0,323,327,5,35,0,0,324,326,
        3,66,33,0,325,324,1,0,0,0,326,329,1,0,0,0,327,325,1,0,0,0,327,328,
        1,0,0,0,328,331,1,0,0,0,329,327,1,0,0,0,330,332,3,68,34,0,331,330,
        1,0,0,0,331,332,1,0,0,0,332,336,1,0,0,0,333,335,3,66,33,0,334,333,
        1,0,0,0,335,338,1,0,0,0,336,334,1,0,0,0,336,337,1,0,0,0,337,339,
        1,0,0,0,338,336,1,0,0,0,339,340,5,36,0,0,340,65,1,0,0,0,341,342,
        5,3,0,0,342,343,3,2,1,0,343,347,5,41,0,0,344,346,3,44,22,0,345,344,
        1,0,0,0,346,349,1,0,0,0,347,345,1,0,0,0,347,348,1,0,0,0,348,67,1,
        0,0,0,349,347,1,0,0,0,350,351,5,5,0,0,351,355,5,41,0,0,352,354,3,
        44,22,0,353,352,1,0,0,0,354,357,1,0,0,0,355,353,1,0,0,0,355,356,
        1,0,0,0,356,69,1,0,0,0,357,355,1,0,0,0,358,359,5,2,0,0,359,360,5,
        39,0,0,360,71,1,0,0,0,361,362,5,4,0,0,362,363,5,39,0,0,363,73,1,
        0,0,0,364,365,3,2,1,0,365,366,5,39,0,0,366,75,1,0,0,0,367,369,5,
        11,0,0,368,370,3,48,24,0,369,368,1,0,0,0,369,370,1,0,0,0,370,371,
        1,0,0,0,371,372,5,39,0,0,372,77,1,0,0,0,373,376,3,80,40,0,374,376,
        3,86,43,0,375,373,1,0,0,0,375,374,1,0,0,0,376,379,1,0,0,0,377,375,
        1,0,0,0,377,378,1,0,0,0,378,380,1,0,0,0,379,377,1,0,0,0,380,381,
        5,0,0,1,381,79,1,0,0,0,382,383,5,13,0,0,383,384,5,42,0,0,384,388,
        5,35,0,0,385,387,3,82,41,0,386,385,1,0,0,0,387,390,1,0,0,0,388,386,
        1,0,0,0,388,389,1,0,0,0,389,391,1,0,0,0,390,388,1,0,0,0,391,392,
        5,36,0,0,392,393,5,39,0,0,393,81,1,0,0,0,394,395,3,84,42,0,395,396,
        5,42,0,0,396,397,5,39,0,0,397,83,1,0,0,0,398,399,7,9,0,0,399,85,
        1,0,0,0,400,402,3,40,20,0,401,400,1,0,0,0,401,402,1,0,0,0,402,403,
        1,0,0,0,403,404,5,42,0,0,404,406,5,37,0,0,405,407,3,88,44,0,406,
        405,1,0,0,0,406,407,1,0,0,0,407,408,1,0,0,0,408,409,5,38,0,0,409,
        410,3,50,25,0,410,87,1,0,0,0,411,416,3,90,45,0,412,413,5,40,0,0,
        413,415,3,90,45,0,414,412,1,0,0,0,415,418,1,0,0,0,416,414,1,0,0,
        0,416,417,1,0,0,0,417,89,1,0,0,0,418,416,1,0,0,0,419,420,3,84,42,
        0,420,421,5,42,0,0,421,91,1,0,0,0,42,97,105,112,120,128,136,144,
        152,158,163,169,180,191,196,205,211,218,226,231,245,251,255,261,
        273,284,288,292,299,315,317,327,331,336,347,355,369,375,377,388,
        401,406,416
    ]

class CSParser ( Parser ):

    grammarFileName = "CS.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'auto'", "'break'", "'case'", "'continue'", 
                     "'default'", "'else'", "'float'", "'for'", "'if'", 
                     "'int'", "'return'", "'string'", "'struct'", "'switch'", 
                     "'void'", "'while'", "'+'", "'-'", "'*'", "'/'", "'=='", 
                     "'!='", "'<'", "'>'", "'<='", "'>='", "'%'", "'||'", 
                     "'&&'", "'!'", "'++'", "'--'", "'='", "'.'", "'{'", 
                     "'}'", "'('", "')'", "';'", "','", "':'" ]

    symbolicNames = [ "<INVALID>", "AUTO", "BREAK", "CASE", "CONTINUE", 
                      "DEFAULT", "ELSE", "FLOAT", "FOR", "IF", "INT", "RETURN", 
                      "STRING", "STRUCT", "SWITCH", "VOID", "WHILE", "PLUS", 
                      "SUB", "MUL", "DIV", "EQ", "NEQ", "LT", "GT", "LTE", 
                      "GTE", "MOD", "OR", "AND", "NOT", "INCRE", "DECRE", 
                      "ASSIGN", "ACCESS", "LBRACE", "RBRACE", "LPAREN", 
                      "RPAREN", "SEMI", "COMMA", "COLON", "ID", "INT_LIT", 
                      "FLOAT_LIT", "STRING_LIT", "WS", "BLOCK_COMMENT", 
                      "LINE_COMMENT", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "ERROR_CHAR" ]

    RULE_list_expression = 0
    RULE_expression = 1
    RULE_expression1 = 2
    RULE_expression2 = 3
    RULE_expression3 = 4
    RULE_expression4 = 5
    RULE_expression5 = 6
    RULE_expression6 = 7
    RULE_expression7 = 8
    RULE_expression8 = 9
    RULE_expression9 = 10
    RULE_expression10 = 11
    RULE_expression11 = 12
    RULE_function_call = 13
    RULE_lhs = 14
    RULE_literal = 15
    RULE_struct_literal = 16
    RULE_all_type = 17
    RULE_primitive_type = 18
    RULE_var_type = 19
    RULE_function_type = 20
    RULE_list_statement = 21
    RULE_statement = 22
    RULE_var_statement = 23
    RULE_init_value = 24
    RULE_block_statement = 25
    RULE_if_statement = 26
    RULE_while_statement = 27
    RULE_for_statement = 28
    RULE_for_init = 29
    RULE_assign_init = 30
    RULE_for_update = 31
    RULE_switch_statement = 32
    RULE_case_section = 33
    RULE_default_section = 34
    RULE_break_statement = 35
    RULE_continue_statement = 36
    RULE_expression_statement = 37
    RULE_return_statement = 38
    RULE_program = 39
    RULE_structs = 40
    RULE_struct_body = 41
    RULE_explicit_type = 42
    RULE_functions = 43
    RULE_list_parameter = 44
    RULE_parameter = 45

    ruleNames =  [ "list_expression", "expression", "expression1", "expression2", 
                   "expression3", "expression4", "expression5", "expression6", 
                   "expression7", "expression8", "expression9", "expression10", 
                   "expression11", "function_call", "lhs", "literal", "struct_literal", 
                   "all_type", "primitive_type", "var_type", "function_type", 
                   "list_statement", "statement", "var_statement", "init_value", 
                   "block_statement", "if_statement", "while_statement", 
                   "for_statement", "for_init", "assign_init", "for_update", 
                   "switch_statement", "case_section", "default_section", 
                   "break_statement", "continue_statement", "expression_statement", 
                   "return_statement", "program", "structs", "struct_body", 
                   "explicit_type", "functions", "list_parameter", "parameter" ]

    EOF = Token.EOF
    AUTO=1
    BREAK=2
    CASE=3
    CONTINUE=4
    DEFAULT=5
    ELSE=6
    FLOAT=7
    FOR=8
    IF=9
    INT=10
    RETURN=11
    STRING=12
    STRUCT=13
    SWITCH=14
    VOID=15
    WHILE=16
    PLUS=17
    SUB=18
    MUL=19
    DIV=20
    EQ=21
    NEQ=22
    LT=23
    GT=24
    LTE=25
    GTE=26
    MOD=27
    OR=28
    AND=29
    NOT=30
    INCRE=31
    DECRE=32
    ASSIGN=33
    ACCESS=34
    LBRACE=35
    RBRACE=36
    LPAREN=37
    RPAREN=38
    SEMI=39
    COMMA=40
    COLON=41
    ID=42
    INT_LIT=43
    FLOAT_LIT=44
    STRING_LIT=45
    WS=46
    BLOCK_COMMENT=47
    LINE_COMMENT=48
    UNCLOSE_STRING=49
    ILLEGAL_ESCAPE=50
    ERROR_CHAR=51

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class List_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(CSParser.ExpressionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.COMMA)
            else:
                return self.getToken(CSParser.COMMA, i)

        def getRuleIndex(self):
            return CSParser.RULE_list_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_expression" ):
                return visitor.visitList_expression(self)
            else:
                return visitor.visitChildren(self)




    def list_expression(self):

        localctx = CSParser.List_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_list_expression)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.expression()
            self.state = 97
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 93
                self.match(CSParser.COMMA)
                self.state = 94
                self.expression()
                self.state = 99
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def expression1(self):
            return self.getTypedRuleContext(CSParser.Expression1Context,0)


        def getRuleIndex(self):
            return CSParser.RULE_expression

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = CSParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 105
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 100
                self.lhs()
                self.state = 101
                self.match(CSParser.ASSIGN)
                self.state = 102
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 104
                self.expression1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression2Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression2Context,i)


        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.OR)
            else:
                return self.getToken(CSParser.OR, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression1

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression1" ):
                return visitor.visitExpression1(self)
            else:
                return visitor.visitChildren(self)




    def expression1(self):

        localctx = CSParser.Expression1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_expression1)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 107
            self.expression2()
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==28:
                self.state = 108
                self.match(CSParser.OR)
                self.state = 109
                self.expression2()
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression3Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression3Context,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.AND)
            else:
                return self.getToken(CSParser.AND, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression2

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression2" ):
                return visitor.visitExpression2(self)
            else:
                return visitor.visitChildren(self)




    def expression2(self):

        localctx = CSParser.Expression2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_expression2)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.expression3()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==29:
                self.state = 116
                self.match(CSParser.AND)
                self.state = 117
                self.expression3()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression4(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression4Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression4Context,i)


        def EQ(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.EQ)
            else:
                return self.getToken(CSParser.EQ, i)

        def NEQ(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.NEQ)
            else:
                return self.getToken(CSParser.NEQ, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression3

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression3" ):
                return visitor.visitExpression3(self)
            else:
                return visitor.visitChildren(self)




    def expression3(self):

        localctx = CSParser.Expression3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression3)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.expression4()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==21 or _la==22:
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==21 or _la==22):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 125
                self.expression4()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression4Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression5(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression5Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression5Context,i)


        def LT(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.LT)
            else:
                return self.getToken(CSParser.LT, i)

        def LTE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.LTE)
            else:
                return self.getToken(CSParser.LTE, i)

        def GT(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.GT)
            else:
                return self.getToken(CSParser.GT, i)

        def GTE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.GTE)
            else:
                return self.getToken(CSParser.GTE, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression4

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression4" ):
                return visitor.visitExpression4(self)
            else:
                return visitor.visitChildren(self)




    def expression4(self):

        localctx = CSParser.Expression4Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expression4)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.expression5()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0):
                self.state = 132
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 125829120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 133
                self.expression5()
                self.state = 138
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression5Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression6(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression6Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression6Context,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.PLUS)
            else:
                return self.getToken(CSParser.PLUS, i)

        def SUB(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.SUB)
            else:
                return self.getToken(CSParser.SUB, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression5

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression5" ):
                return visitor.visitExpression5(self)
            else:
                return visitor.visitChildren(self)




    def expression5(self):

        localctx = CSParser.Expression5Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expression5)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            self.expression6()
            self.state = 144
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 140
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 141
                self.expression6()
                self.state = 146
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression6Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Expression7Context)
            else:
                return self.getTypedRuleContext(CSParser.Expression7Context,i)


        def MUL(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.MUL)
            else:
                return self.getToken(CSParser.MUL, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.DIV)
            else:
                return self.getToken(CSParser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.MOD)
            else:
                return self.getToken(CSParser.MOD, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression6

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression6" ):
                return visitor.visitExpression6(self)
            else:
                return visitor.visitChildren(self)




    def expression6(self):

        localctx = CSParser.Expression6Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression6)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.expression7()
            self.state = 152
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 135790592) != 0):
                self.state = 148
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 135790592) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 149
                self.expression7()
                self.state = 154
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression7Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression7(self):
            return self.getTypedRuleContext(CSParser.Expression7Context,0)


        def NOT(self):
            return self.getToken(CSParser.NOT, 0)

        def SUB(self):
            return self.getToken(CSParser.SUB, 0)

        def PLUS(self):
            return self.getToken(CSParser.PLUS, 0)

        def expression8(self):
            return self.getTypedRuleContext(CSParser.Expression8Context,0)


        def getRuleIndex(self):
            return CSParser.RULE_expression7

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression7" ):
                return visitor.visitExpression7(self)
            else:
                return visitor.visitChildren(self)




    def expression7(self):

        localctx = CSParser.Expression7Context(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression7)
        self._la = 0 # Token type
        try:
            self.state = 158
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [17, 18, 30]:
                self.enterOuterAlt(localctx, 1)
                self.state = 155
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1074135040) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 156
                self.expression7()
                pass
            elif token in [31, 32, 35, 37, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 157
                self.expression8()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression8Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression8(self):
            return self.getTypedRuleContext(CSParser.Expression8Context,0)


        def INCRE(self):
            return self.getToken(CSParser.INCRE, 0)

        def DECRE(self):
            return self.getToken(CSParser.DECRE, 0)

        def expression9(self):
            return self.getTypedRuleContext(CSParser.Expression9Context,0)


        def getRuleIndex(self):
            return CSParser.RULE_expression8

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression8" ):
                return visitor.visitExpression8(self)
            else:
                return visitor.visitChildren(self)




    def expression8(self):

        localctx = CSParser.Expression8Context(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_expression8)
        self._la = 0 # Token type
        try:
            self.state = 163
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31, 32]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 161
                self.expression8()
                pass
            elif token in [35, 37, 42, 43, 44, 45]:
                self.enterOuterAlt(localctx, 2)
                self.state = 162
                self.expression9()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression9Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression10(self):
            return self.getTypedRuleContext(CSParser.Expression10Context,0)


        def INCRE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.INCRE)
            else:
                return self.getToken(CSParser.INCRE, i)

        def DECRE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.DECRE)
            else:
                return self.getToken(CSParser.DECRE, i)

        def getRuleIndex(self):
            return CSParser.RULE_expression9

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression9" ):
                return visitor.visitExpression9(self)
            else:
                return visitor.visitChildren(self)




    def expression9(self):

        localctx = CSParser.Expression9Context(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expression9)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            self.expression10(0)
            self.state = 169
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==31 or _la==32:
                self.state = 166
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 171
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression10Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression11(self):
            return self.getTypedRuleContext(CSParser.Expression11Context,0)


        def expression10(self):
            return self.getTypedRuleContext(CSParser.Expression10Context,0)


        def ACCESS(self):
            return self.getToken(CSParser.ACCESS, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_expression10

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression10" ):
                return visitor.visitExpression10(self)
            else:
                return visitor.visitChildren(self)



    def expression10(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = CSParser.Expression10Context(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression10, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.expression11()
            self._ctx.stop = self._input.LT(-1)
            self.state = 180
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = CSParser.Expression10Context(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_expression10)
                    self.state = 175
                    if not self.precpred(self._ctx, 2):
                        from antlr4.error.Errors import FailedPredicateException
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                    self.state = 176
                    self.match(CSParser.ACCESS)
                    self.state = 177
                    self.match(CSParser.ID) 
                self.state = 182
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Expression11Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(CSParser.LiteralContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(CSParser.Struct_literalContext,0)


        def function_call(self):
            return self.getTypedRuleContext(CSParser.Function_callContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def getRuleIndex(self):
            return CSParser.RULE_expression11

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression11" ):
                return visitor.visitExpression11(self)
            else:
                return visitor.visitChildren(self)




    def expression11(self):

        localctx = CSParser.Expression11Context(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_expression11)
        try:
            self.state = 191
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 183
                self.literal()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 184
                self.struct_literal()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 185
                self.function_call()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 186
                self.match(CSParser.ID)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 187
                self.match(CSParser.LPAREN)
                self.state = 188
                self.expression()
                self.state = 189
                self.match(CSParser.RPAREN)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def list_expression(self):
            return self.getTypedRuleContext(CSParser.List_expressionContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_function_call

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_call" ):
                return visitor.visitFunction_call(self)
            else:
                return visitor.visitChildren(self)




    def function_call(self):

        localctx = CSParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(CSParser.ID)
            self.state = 194
            self.match(CSParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150012944384) != 0):
                self.state = 195
                self.list_expression()


            self.state = 198
            self.match(CSParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LhsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression10(self):
            return self.getTypedRuleContext(CSParser.Expression10Context,0)


        def ACCESS(self):
            return self.getToken(CSParser.ACCESS, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_lhs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLhs" ):
                return visitor.visitLhs(self)
            else:
                return visitor.visitChildren(self)




    def lhs(self):

        localctx = CSParser.LhsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_lhs)
        try:
            self.state = 205
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 200
                self.expression10(0)
                self.state = 201
                self.match(CSParser.ACCESS)
                self.state = 202
                self.match(CSParser.ID)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 204
                self.match(CSParser.ID)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(CSParser.INT_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(CSParser.FLOAT_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(CSParser.STRING_LIT, 0)

        def getRuleIndex(self):
            return CSParser.RULE_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLiteral" ):
                return visitor.visitLiteral(self)
            else:
                return visitor.visitChildren(self)




    def literal(self):

        localctx = CSParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 61572651155456) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CSParser.RBRACE, 0)

        def list_expression(self):
            return self.getTypedRuleContext(CSParser.List_expressionContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_struct_literal

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_literal" ):
                return visitor.visitStruct_literal(self)
            else:
                return visitor.visitChildren(self)




    def struct_literal(self):

        localctx = CSParser.Struct_literalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_struct_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(CSParser.LBRACE)
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150012944384) != 0):
                self.state = 210
                self.list_expression()


            self.state = 213
            self.match(CSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class All_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(CSParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def AUTO(self):
            return self.getToken(CSParser.AUTO, 0)

        def getRuleIndex(self):
            return CSParser.RULE_all_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAll_type" ):
                return visitor.visitAll_type(self)
            else:
                return visitor.visitChildren(self)




    def all_type(self):

        localctx = CSParser.All_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_all_type)
        try:
            self.state = 218
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 10, 12, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 215
                self.primitive_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 216
                self.match(CSParser.ID)
                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 217
                self.match(CSParser.AUTO)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Primitive_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSParser.STRING, 0)

        def VOID(self):
            return self.getToken(CSParser.VOID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_primitive_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrimitive_type" ):
                return visitor.visitPrimitive_type(self)
            else:
                return visitor.visitChildren(self)




    def primitive_type(self):

        localctx = CSParser.Primitive_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_primitive_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 220
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 38016) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSParser.STRING, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def AUTO(self):
            return self.getToken(CSParser.AUTO, 0)

        def getRuleIndex(self):
            return CSParser.RULE_var_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_type" ):
                return visitor.visitVar_type(self)
            else:
                return visitor.visitChildren(self)




    def var_type(self):

        localctx = CSParser.Var_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_var_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 222
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046516354) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def primitive_type(self):
            return self.getTypedRuleContext(CSParser.Primitive_typeContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_function_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunction_type" ):
                return visitor.visitFunction_type(self)
            else:
                return visitor.visitChildren(self)




    def function_type(self):

        localctx = CSParser.Function_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_function_type)
        try:
            self.state = 226
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7, 10, 12, 15]:
                self.enterOuterAlt(localctx, 1)
                self.state = 224
                self.primitive_type()
                pass
            elif token in [42]:
                self.enterOuterAlt(localctx, 2)
                self.state = 225
                self.match(CSParser.ID)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_list_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_statement" ):
                return visitor.visitList_statement(self)
            else:
                return visitor.visitChildren(self)




    def list_statement(self):

        localctx = CSParser.List_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 228
                self.statement()
                self.state = 231 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 66150013034390) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_statement(self):
            return self.getTypedRuleContext(CSParser.Var_statementContext,0)


        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def if_statement(self):
            return self.getTypedRuleContext(CSParser.If_statementContext,0)


        def while_statement(self):
            return self.getTypedRuleContext(CSParser.While_statementContext,0)


        def for_statement(self):
            return self.getTypedRuleContext(CSParser.For_statementContext,0)


        def switch_statement(self):
            return self.getTypedRuleContext(CSParser.Switch_statementContext,0)


        def break_statement(self):
            return self.getTypedRuleContext(CSParser.Break_statementContext,0)


        def continue_statement(self):
            return self.getTypedRuleContext(CSParser.Continue_statementContext,0)


        def block_statement(self):
            return self.getTypedRuleContext(CSParser.Block_statementContext,0)


        def expression_statement(self):
            return self.getTypedRuleContext(CSParser.Expression_statementContext,0)


        def return_statement(self):
            return self.getTypedRuleContext(CSParser.Return_statementContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = CSParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_statement)
        try:
            self.state = 245
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 233
                self.var_statement()
                self.state = 234
                self.match(CSParser.SEMI)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 236
                self.if_statement()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 237
                self.while_statement()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 238
                self.for_statement()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 239
                self.switch_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 240
                self.break_statement()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 241
                self.continue_statement()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 242
                self.block_statement()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 243
                self.expression_statement()
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 244
                self.return_statement()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_type(self):
            return self.getTypedRuleContext(CSParser.Var_typeContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(CSParser.ASSIGN, 0)

        def init_value(self):
            return self.getTypedRuleContext(CSParser.Init_valueContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_var_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_statement" ):
                return visitor.visitVar_statement(self)
            else:
                return visitor.visitChildren(self)




    def var_statement(self):

        localctx = CSParser.Var_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_var_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 247
            self.var_type()
            self.state = 248
            self.match(CSParser.ID)
            self.state = 251
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==33:
                self.state = 249
                self.match(CSParser.ASSIGN)
                self.state = 250
                self.init_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def struct_literal(self):
            return self.getTypedRuleContext(CSParser.Struct_literalContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_init_value

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInit_value" ):
                return visitor.visitInit_value(self)
            else:
                return visitor.visitChildren(self)




    def init_value(self):

        localctx = CSParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_init_value)
        try:
            self.state = 255
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 253
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 254
                self.struct_literal()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Block_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(CSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CSParser.RBRACE, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_block_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock_statement" ):
                return visitor.visitBlock_statement(self)
            else:
                return visitor.visitChildren(self)




    def block_statement(self):

        localctx = CSParser.Block_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_block_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(CSParser.LBRACE)
            self.state = 261
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150013034390) != 0):
                self.state = 258
                self.statement()
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 264
            self.match(CSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(CSParser.IF, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def ELSE(self):
            return self.getToken(CSParser.ELSE, 0)

        def getRuleIndex(self):
            return CSParser.RULE_if_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIf_statement" ):
                return visitor.visitIf_statement(self)
            else:
                return visitor.visitChildren(self)




    def if_statement(self):

        localctx = CSParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            self.match(CSParser.IF)
            self.state = 267
            self.match(CSParser.LPAREN)
            self.state = 268
            self.expression()
            self.state = 269
            self.match(CSParser.RPAREN)
            self.state = 270
            self.statement()
            self.state = 273
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
            if la_ == 1:
                self.state = 271
                self.match(CSParser.ELSE)
                self.state = 272
                self.statement()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class While_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(CSParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(CSParser.StatementContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_while_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhile_statement" ):
                return visitor.visitWhile_statement(self)
            else:
                return visitor.visitChildren(self)




    def while_statement(self):

        localctx = CSParser.While_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_while_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 275
            self.match(CSParser.WHILE)
            self.state = 276
            self.match(CSParser.LPAREN)
            self.state = 277
            self.expression()
            self.state = 278
            self.match(CSParser.RPAREN)
            self.state = 279
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(CSParser.FOR, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def SEMI(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.SEMI)
            else:
                return self.getToken(CSParser.SEMI, i)

        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def statement(self):
            return self.getTypedRuleContext(CSParser.StatementContext,0)


        def for_init(self):
            return self.getTypedRuleContext(CSParser.For_initContext,0)


        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def for_update(self):
            return self.getTypedRuleContext(CSParser.For_updateContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_for_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_statement" ):
                return visitor.visitFor_statement(self)
            else:
                return visitor.visitChildren(self)




    def for_statement(self):

        localctx = CSParser.For_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_for_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 281
            self.match(CSParser.FOR)
            self.state = 282
            self.match(CSParser.LPAREN)
            self.state = 284
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66142496363650) != 0):
                self.state = 283
                self.for_init()


            self.state = 286
            self.match(CSParser.SEMI)
            self.state = 288
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150012944384) != 0):
                self.state = 287
                self.expression()


            self.state = 290
            self.match(CSParser.SEMI)
            self.state = 292
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66148938809344) != 0):
                self.state = 291
                self.for_update()


            self.state = 294
            self.match(CSParser.RPAREN)
            self.state = 295
            self.statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_statement(self):
            return self.getTypedRuleContext(CSParser.Var_statementContext,0)


        def assign_init(self):
            return self.getTypedRuleContext(CSParser.Assign_initContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_for_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_init" ):
                return visitor.visitFor_init(self)
            else:
                return visitor.visitChildren(self)




    def for_init(self):

        localctx = CSParser.For_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_for_init)
        try:
            self.state = 299
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,27,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 297
                self.var_statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 298
                self.assign_init()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Assign_initContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_assign_init

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssign_init" ):
                return visitor.visitAssign_init(self)
            else:
                return visitor.visitChildren(self)




    def assign_init(self):

        localctx = CSParser.Assign_initContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_assign_init)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 301
            self.lhs()
            self.state = 302
            self.match(CSParser.ASSIGN)
            self.state = 303
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class For_updateContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def lhs(self):
            return self.getTypedRuleContext(CSParser.LhsContext,0)


        def ASSIGN(self):
            return self.getToken(CSParser.ASSIGN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def expression8(self):
            return self.getTypedRuleContext(CSParser.Expression8Context,0)


        def INCRE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.INCRE)
            else:
                return self.getToken(CSParser.INCRE, i)

        def DECRE(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.DECRE)
            else:
                return self.getToken(CSParser.DECRE, i)

        def expression10(self):
            return self.getTypedRuleContext(CSParser.Expression10Context,0)


        def getRuleIndex(self):
            return CSParser.RULE_for_update

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFor_update" ):
                return visitor.visitFor_update(self)
            else:
                return visitor.visitChildren(self)




    def for_update(self):

        localctx = CSParser.For_updateContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_for_update)
        self._la = 0 # Token type
        try:
            self.state = 317
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,29,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 305
                self.lhs()
                self.state = 306
                self.match(CSParser.ASSIGN)
                self.state = 307
                self.expression()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 309
                _la = self._input.LA(1)
                if not(_la==31 or _la==32):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 310
                self.expression8()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 311
                self.expression10(0)
                self.state = 313 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 312
                    _la = self._input.LA(1)
                    if not(_la==31 or _la==32):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 315 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==31 or _la==32):
                        break

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Switch_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SWITCH(self):
            return self.getToken(CSParser.SWITCH, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def LBRACE(self):
            return self.getToken(CSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CSParser.RBRACE, 0)

        def case_section(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Case_sectionContext)
            else:
                return self.getTypedRuleContext(CSParser.Case_sectionContext,i)


        def default_section(self):
            return self.getTypedRuleContext(CSParser.Default_sectionContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_switch_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSwitch_statement" ):
                return visitor.visitSwitch_statement(self)
            else:
                return visitor.visitChildren(self)




    def switch_statement(self):

        localctx = CSParser.Switch_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_switch_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 319
            self.match(CSParser.SWITCH)
            self.state = 320
            self.match(CSParser.LPAREN)
            self.state = 321
            self.expression()
            self.state = 322
            self.match(CSParser.RPAREN)
            self.state = 323
            self.match(CSParser.LBRACE)
            self.state = 327
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 324
                    self.case_section() 
                self.state = 329
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

            self.state = 331
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 330
                self.default_section()


            self.state = 336
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3:
                self.state = 333
                self.case_section()
                self.state = 338
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 339
            self.match(CSParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Case_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CASE(self):
            return self.getToken(CSParser.CASE, 0)

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def COLON(self):
            return self.getToken(CSParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_case_section

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCase_section" ):
                return visitor.visitCase_section(self)
            else:
                return visitor.visitChildren(self)




    def case_section(self):

        localctx = CSParser.Case_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_case_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 341
            self.match(CSParser.CASE)
            self.state = 342
            self.expression()
            self.state = 343
            self.match(CSParser.COLON)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150013034390) != 0):
                self.state = 344
                self.statement()
                self.state = 349
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Default_sectionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DEFAULT(self):
            return self.getToken(CSParser.DEFAULT, 0)

        def COLON(self):
            return self.getToken(CSParser.COLON, 0)

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StatementContext)
            else:
                return self.getTypedRuleContext(CSParser.StatementContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_default_section

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefault_section" ):
                return visitor.visitDefault_section(self)
            else:
                return visitor.visitChildren(self)




    def default_section(self):

        localctx = CSParser.Default_sectionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_default_section)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 350
            self.match(CSParser.DEFAULT)
            self.state = 351
            self.match(CSParser.COLON)
            self.state = 355
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150013034390) != 0):
                self.state = 352
                self.statement()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Break_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(CSParser.BREAK, 0)

        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def getRuleIndex(self):
            return CSParser.RULE_break_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak_statement" ):
                return visitor.visitBreak_statement(self)
            else:
                return visitor.visitChildren(self)




    def break_statement(self):

        localctx = CSParser.Break_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_break_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 358
            self.match(CSParser.BREAK)
            self.state = 359
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Continue_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CONTINUE(self):
            return self.getToken(CSParser.CONTINUE, 0)

        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def getRuleIndex(self):
            return CSParser.RULE_continue_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitContinue_statement" ):
                return visitor.visitContinue_statement(self)
            else:
                return visitor.visitChildren(self)




    def continue_statement(self):

        localctx = CSParser.Continue_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_continue_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 361
            self.match(CSParser.CONTINUE)
            self.state = 362
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expression_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(CSParser.ExpressionContext,0)


        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def getRuleIndex(self):
            return CSParser.RULE_expression_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression_statement" ):
                return visitor.visitExpression_statement(self)
            else:
                return visitor.visitChildren(self)




    def expression_statement(self):

        localctx = CSParser.Expression_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_expression_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expression()
            self.state = 365
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RETURN(self):
            return self.getToken(CSParser.RETURN, 0)

        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def init_value(self):
            return self.getTypedRuleContext(CSParser.Init_valueContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_return_statement

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturn_statement" ):
                return visitor.visitReturn_statement(self)
            else:
                return visitor.visitChildren(self)




    def return_statement(self):

        localctx = CSParser.Return_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_return_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 367
            self.match(CSParser.RETURN)
            self.state = 369
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 66150012944384) != 0):
                self.state = 368
                self.init_value()


            self.state = 371
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(CSParser.EOF, 0)

        def structs(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.StructsContext)
            else:
                return self.getTypedRuleContext(CSParser.StructsContext,i)


        def functions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.FunctionsContext)
            else:
                return self.getTypedRuleContext(CSParser.FunctionsContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_program

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = CSParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 377
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046557312) != 0):
                self.state = 375
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [13]:
                    self.state = 373
                    self.structs()
                    pass
                elif token in [7, 10, 12, 15, 42]:
                    self.state = 374
                    self.functions()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 379
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 380
            self.match(CSParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StructsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRUCT(self):
            return self.getToken(CSParser.STRUCT, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def LBRACE(self):
            return self.getToken(CSParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(CSParser.RBRACE, 0)

        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def struct_body(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.Struct_bodyContext)
            else:
                return self.getTypedRuleContext(CSParser.Struct_bodyContext,i)


        def getRuleIndex(self):
            return CSParser.RULE_structs

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStructs" ):
                return visitor.visitStructs(self)
            else:
                return visitor.visitChildren(self)




    def structs(self):

        localctx = CSParser.StructsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_structs)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 382
            self.match(CSParser.STRUCT)
            self.state = 383
            self.match(CSParser.ID)
            self.state = 384
            self.match(CSParser.LBRACE)
            self.state = 388
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046516352) != 0):
                self.state = 385
                self.struct_body()
                self.state = 390
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 391
            self.match(CSParser.RBRACE)
            self.state = 392
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Struct_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_type(self):
            return self.getTypedRuleContext(CSParser.Explicit_typeContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def SEMI(self):
            return self.getToken(CSParser.SEMI, 0)

        def getRuleIndex(self):
            return CSParser.RULE_struct_body

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStruct_body" ):
                return visitor.visitStruct_body(self)
            else:
                return visitor.visitChildren(self)




    def struct_body(self):

        localctx = CSParser.Struct_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_struct_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 394
            self.explicit_type()
            self.state = 395
            self.match(CSParser.ID)
            self.state = 396
            self.match(CSParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Explicit_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(CSParser.INT, 0)

        def FLOAT(self):
            return self.getToken(CSParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(CSParser.STRING, 0)

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_explicit_type

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExplicit_type" ):
                return visitor.visitExplicit_type(self)
            else:
                return visitor.visitChildren(self)




    def explicit_type(self):

        localctx = CSParser.Explicit_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_explicit_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 398
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046516352) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def LPAREN(self):
            return self.getToken(CSParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(CSParser.RPAREN, 0)

        def block_statement(self):
            return self.getTypedRuleContext(CSParser.Block_statementContext,0)


        def function_type(self):
            return self.getTypedRuleContext(CSParser.Function_typeContext,0)


        def list_parameter(self):
            return self.getTypedRuleContext(CSParser.List_parameterContext,0)


        def getRuleIndex(self):
            return CSParser.RULE_functions

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = CSParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_functions)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 401
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,39,self._ctx)
            if la_ == 1:
                self.state = 400
                self.function_type()


            self.state = 403
            self.match(CSParser.ID)
            self.state = 404
            self.match(CSParser.LPAREN)
            self.state = 406
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 4398046516352) != 0):
                self.state = 405
                self.list_parameter()


            self.state = 408
            self.match(CSParser.RPAREN)
            self.state = 409
            self.block_statement()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class List_parameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def parameter(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(CSParser.ParameterContext)
            else:
                return self.getTypedRuleContext(CSParser.ParameterContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(CSParser.COMMA)
            else:
                return self.getToken(CSParser.COMMA, i)

        def getRuleIndex(self):
            return CSParser.RULE_list_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitList_parameter" ):
                return visitor.visitList_parameter(self)
            else:
                return visitor.visitChildren(self)




    def list_parameter(self):

        localctx = CSParser.List_parameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_list_parameter)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 411
            self.parameter()
            self.state = 416
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==40:
                self.state = 412
                self.match(CSParser.COMMA)
                self.state = 413
                self.parameter()
                self.state = 418
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParameterContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def explicit_type(self):
            return self.getTypedRuleContext(CSParser.Explicit_typeContext,0)


        def ID(self):
            return self.getToken(CSParser.ID, 0)

        def getRuleIndex(self):
            return CSParser.RULE_parameter

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameter" ):
                return visitor.visitParameter(self)
            else:
                return visitor.visitChildren(self)




    def parameter(self):

        localctx = CSParser.ParameterContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_parameter)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 419
            self.explicit_type()
            self.state = 420
            self.match(CSParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression10_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression10_sempred(self, localctx:Expression10Context, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 2)
         





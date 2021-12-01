
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'A AltGr Ampersand Asterisk At B BackQuote Backslash Backspace Break C CapsLock Caret Clear Colon Comma D Dollar DoubleQuote E EQUALS Equals Escape Exclaim F FLIGHT Float G Greater H Hash Help Horizontal I ID J K L LeftAlt LeftBracket LeftCommand LeftControl LeftParen LeftShift LeftWindows Less M Minus N NONE O P Pause Period Plus Print Q Question Quote R REGULAR Return RightAlt RightApple RightBracket RightCommand RightControl RightParen RightShift RightWindows S ScrollLock Semicolon Slash Space Speed SysReq T TOPDOWN Tab U Underscore V Vertical W X Y Zscript : Regular\n                | TopDown\n                | FlightRegular : REGULAR Speedfunc MovementTopDown : TOPDOWN Speedfunc MovementFlight : FLIGHT Speedfunc MovementSpeedfunc : Speed EQUALS FloatMovement : ID EQUALS Direction ID EQUALS DirectionDirection : Horizontal\n    | Vertical\n    | NONEKeyCode : \n          | A\n          | B\n          | C\n          | D\n          | E\n          | F\n          | G\n          | H\n          | I\n          | J\n          | K\n          | L\n          | M\n          | N\n          | O\n          | P\n          | Q\n          | R\n          | S\n          | T\n          | U\n          | V\n          | W\n          | X\n          | Y\n          | Z\n          | Backspace\n          | Tab\n          | SysReq\n          | Break\n          | CapsLock\n          | ScrollLock\n          | RightShift\n          | LeftShift\n          | RightControl\n          | LeftControl\n          | RightAlt\n          | LeftAlt\n          | RightCommand\n          | RightApple\n          | LeftCommand\n          | LeftWindows\n          | RightWindows\n          | AltGr\n          | Help\n          | Print\n          | Clear\n          | Return\n          | Pause\n          | Escape\n          | Space\n          | Exclaim\n          | DoubleQuote\n          | Hash\n          | Dollar\n\t\t  | Ampersand\n\t\t  | Quote\n\t\t  | LeftParen\n\t\t  | RightParen\n\t\t  | Asterisk\n\t\t  | Plus\n\t\t  | Comma\n\t\t  | Minus\n\t\t  | Period\n\t\t  | Slash\n\t\t  | Colon\n\t\t  | Semicolon\n\t\t  | Less\n\t\t  | Equals\n\t\t  | Greater\n\t\t  | Question\n\t\t  | At\n\t\t  | LeftBracket\n\t\t  | Backslash\n\t\t  | RightBracket\n\t\t  | Caret\n\t\t  | Underscore\n\t\t  | BackQuote\n\t\t  \n'
    
_lr_action_items = {'REGULAR':([0,],[5,]),'TOPDOWN':([0,],[6,]),'FLIGHT':([0,],[7,]),'$end':([1,2,3,4,12,15,16,20,21,22,25,],[0,-1,-2,-3,-4,-5,-6,-9,-10,-11,-8,]),'Speed':([5,6,7,],[9,9,9,]),'ID':([8,10,11,18,19,20,21,22,],[13,13,13,-7,23,-9,-10,-11,]),'EQUALS':([9,13,23,],[14,17,24,]),'Float':([14,],[18,]),'Horizontal':([17,24,],[20,20,]),'Vertical':([17,24,],[21,21,]),'NONE':([17,24,],[22,22,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'script':([0,],[1,]),'Regular':([0,],[2,]),'TopDown':([0,],[3,]),'Flight':([0,],[4,]),'Speedfunc':([5,6,7,],[8,10,11,]),'Movement':([8,10,11,],[12,15,16,]),'Direction':([17,24,],[19,25,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> script","S'",1,None,None,None),
  ('script -> Regular','script',1,'p_setScript','Parser.py',8),
  ('script -> TopDown','script',1,'p_setScript','Parser.py',9),
  ('script -> Flight','script',1,'p_setScript','Parser.py',10),
  ('Regular -> REGULAR Speedfunc Movement','Regular',3,'p_Regular_script','Parser.py',13),
  ('TopDown -> TOPDOWN Speedfunc Movement','TopDown',3,'p_TopDown_script2','Parser.py',35),
  ('Flight -> FLIGHT Speedfunc Movement','Flight',3,'p_Flight_script','Parser.py',53),
  ('Speedfunc -> Speed EQUALS Float','Speedfunc',3,'p_speedfunc','Parser.py',67),
  ('Movement -> ID EQUALS Direction ID EQUALS Direction','Movement',6,'p_movement_rule','Parser.py',72),
  ('Direction -> Horizontal','Direction',1,'p_Direction','Parser.py',81),
  ('Direction -> Vertical','Direction',1,'p_Direction','Parser.py',82),
  ('Direction -> NONE','Direction',1,'p_Direction','Parser.py',83),
  ('KeyCode -> <empty>','KeyCode',0,'p_KeyCode','Parser.py',87),
  ('KeyCode -> A','KeyCode',1,'p_KeyCode','Parser.py',88),
  ('KeyCode -> B','KeyCode',1,'p_KeyCode','Parser.py',89),
  ('KeyCode -> C','KeyCode',1,'p_KeyCode','Parser.py',90),
  ('KeyCode -> D','KeyCode',1,'p_KeyCode','Parser.py',91),
  ('KeyCode -> E','KeyCode',1,'p_KeyCode','Parser.py',92),
  ('KeyCode -> F','KeyCode',1,'p_KeyCode','Parser.py',93),
  ('KeyCode -> G','KeyCode',1,'p_KeyCode','Parser.py',94),
  ('KeyCode -> H','KeyCode',1,'p_KeyCode','Parser.py',95),
  ('KeyCode -> I','KeyCode',1,'p_KeyCode','Parser.py',96),
  ('KeyCode -> J','KeyCode',1,'p_KeyCode','Parser.py',97),
  ('KeyCode -> K','KeyCode',1,'p_KeyCode','Parser.py',98),
  ('KeyCode -> L','KeyCode',1,'p_KeyCode','Parser.py',99),
  ('KeyCode -> M','KeyCode',1,'p_KeyCode','Parser.py',100),
  ('KeyCode -> N','KeyCode',1,'p_KeyCode','Parser.py',101),
  ('KeyCode -> O','KeyCode',1,'p_KeyCode','Parser.py',102),
  ('KeyCode -> P','KeyCode',1,'p_KeyCode','Parser.py',103),
  ('KeyCode -> Q','KeyCode',1,'p_KeyCode','Parser.py',104),
  ('KeyCode -> R','KeyCode',1,'p_KeyCode','Parser.py',105),
  ('KeyCode -> S','KeyCode',1,'p_KeyCode','Parser.py',106),
  ('KeyCode -> T','KeyCode',1,'p_KeyCode','Parser.py',107),
  ('KeyCode -> U','KeyCode',1,'p_KeyCode','Parser.py',108),
  ('KeyCode -> V','KeyCode',1,'p_KeyCode','Parser.py',109),
  ('KeyCode -> W','KeyCode',1,'p_KeyCode','Parser.py',110),
  ('KeyCode -> X','KeyCode',1,'p_KeyCode','Parser.py',111),
  ('KeyCode -> Y','KeyCode',1,'p_KeyCode','Parser.py',112),
  ('KeyCode -> Z','KeyCode',1,'p_KeyCode','Parser.py',113),
  ('KeyCode -> Backspace','KeyCode',1,'p_KeyCode','Parser.py',114),
  ('KeyCode -> Tab','KeyCode',1,'p_KeyCode','Parser.py',115),
  ('KeyCode -> SysReq','KeyCode',1,'p_KeyCode','Parser.py',116),
  ('KeyCode -> Break','KeyCode',1,'p_KeyCode','Parser.py',117),
  ('KeyCode -> CapsLock','KeyCode',1,'p_KeyCode','Parser.py',118),
  ('KeyCode -> ScrollLock','KeyCode',1,'p_KeyCode','Parser.py',119),
  ('KeyCode -> RightShift','KeyCode',1,'p_KeyCode','Parser.py',120),
  ('KeyCode -> LeftShift','KeyCode',1,'p_KeyCode','Parser.py',121),
  ('KeyCode -> RightControl','KeyCode',1,'p_KeyCode','Parser.py',122),
  ('KeyCode -> LeftControl','KeyCode',1,'p_KeyCode','Parser.py',123),
  ('KeyCode -> RightAlt','KeyCode',1,'p_KeyCode','Parser.py',124),
  ('KeyCode -> LeftAlt','KeyCode',1,'p_KeyCode','Parser.py',125),
  ('KeyCode -> RightCommand','KeyCode',1,'p_KeyCode','Parser.py',126),
  ('KeyCode -> RightApple','KeyCode',1,'p_KeyCode','Parser.py',127),
  ('KeyCode -> LeftCommand','KeyCode',1,'p_KeyCode','Parser.py',128),
  ('KeyCode -> LeftWindows','KeyCode',1,'p_KeyCode','Parser.py',129),
  ('KeyCode -> RightWindows','KeyCode',1,'p_KeyCode','Parser.py',130),
  ('KeyCode -> AltGr','KeyCode',1,'p_KeyCode','Parser.py',131),
  ('KeyCode -> Help','KeyCode',1,'p_KeyCode','Parser.py',132),
  ('KeyCode -> Print','KeyCode',1,'p_KeyCode','Parser.py',133),
  ('KeyCode -> Clear','KeyCode',1,'p_KeyCode','Parser.py',134),
  ('KeyCode -> Return','KeyCode',1,'p_KeyCode','Parser.py',135),
  ('KeyCode -> Pause','KeyCode',1,'p_KeyCode','Parser.py',136),
  ('KeyCode -> Escape','KeyCode',1,'p_KeyCode','Parser.py',137),
  ('KeyCode -> Space','KeyCode',1,'p_KeyCode','Parser.py',138),
  ('KeyCode -> Exclaim','KeyCode',1,'p_KeyCode','Parser.py',139),
  ('KeyCode -> DoubleQuote','KeyCode',1,'p_KeyCode','Parser.py',140),
  ('KeyCode -> Hash','KeyCode',1,'p_KeyCode','Parser.py',141),
  ('KeyCode -> Dollar','KeyCode',1,'p_KeyCode','Parser.py',142),
  ('KeyCode -> Ampersand','KeyCode',1,'p_KeyCode','Parser.py',143),
  ('KeyCode -> Quote','KeyCode',1,'p_KeyCode','Parser.py',144),
  ('KeyCode -> LeftParen','KeyCode',1,'p_KeyCode','Parser.py',145),
  ('KeyCode -> RightParen','KeyCode',1,'p_KeyCode','Parser.py',146),
  ('KeyCode -> Asterisk','KeyCode',1,'p_KeyCode','Parser.py',147),
  ('KeyCode -> Plus','KeyCode',1,'p_KeyCode','Parser.py',148),
  ('KeyCode -> Comma','KeyCode',1,'p_KeyCode','Parser.py',149),
  ('KeyCode -> Minus','KeyCode',1,'p_KeyCode','Parser.py',150),
  ('KeyCode -> Period','KeyCode',1,'p_KeyCode','Parser.py',151),
  ('KeyCode -> Slash','KeyCode',1,'p_KeyCode','Parser.py',152),
  ('KeyCode -> Colon','KeyCode',1,'p_KeyCode','Parser.py',153),
  ('KeyCode -> Semicolon','KeyCode',1,'p_KeyCode','Parser.py',154),
  ('KeyCode -> Less','KeyCode',1,'p_KeyCode','Parser.py',155),
  ('KeyCode -> Equals','KeyCode',1,'p_KeyCode','Parser.py',156),
  ('KeyCode -> Greater','KeyCode',1,'p_KeyCode','Parser.py',157),
  ('KeyCode -> Question','KeyCode',1,'p_KeyCode','Parser.py',158),
  ('KeyCode -> At','KeyCode',1,'p_KeyCode','Parser.py',159),
  ('KeyCode -> LeftBracket','KeyCode',1,'p_KeyCode','Parser.py',160),
  ('KeyCode -> Backslash','KeyCode',1,'p_KeyCode','Parser.py',161),
  ('KeyCode -> RightBracket','KeyCode',1,'p_KeyCode','Parser.py',162),
  ('KeyCode -> Caret','KeyCode',1,'p_KeyCode','Parser.py',163),
  ('KeyCode -> Underscore','KeyCode',1,'p_KeyCode','Parser.py',164),
  ('KeyCode -> BackQuote','KeyCode',1,'p_KeyCode','Parser.py',165),
]
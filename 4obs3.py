""#line:5:"""
__all__ =[]#line:7:__all__ = []
class OOO0O0OO0000OO0OO :#line:9:class Node:
    def __init__ (O00O00O00O00O0O00 ,O0000O0000O0O00OO ):#line:11:def __init__(self, candidate):
        O00O00O00O00O0O00 .candidate =O0000O0000O0O00OO #line:13:self.candidate = candidate
class O0000O0000O0OO000 :#line:15:class HeaderNode:
    def __init__ (OOO00O0O0O000O000 ,OOO000OOOO00OOOO0 ):#line:17:def __init__(self, constraint):
        OOO00O0O0O000O000 .constraint =OOO000OOOO00OOOO0 #line:18:self.constraint = constraint
class O000000OOO0OO000O (object ):#line:20:class DancingLinks(object):
    def __init__ (OOOOOOOOOOO0OO0OO ,O00O00O0OOO0000O0 ,O0OO0000000OO0OO0 ,O000000O00O0O000O ,OOO0OO0000OOO000O ):#line:22:def __init__(self, candidates, constraints, optional, check_func):
        OOOOOOOOOOO0OO0OO .__OO0O0O0OO00OOO0OO =O00O00O0OOO0000O0 #line:23:self.__candidates = candidates
        OOOOOOOOOOO0OO0OO .__O0OOOO00O00O0O00O =O0OO0000000OO0OO0 #line:24:self.__constraints = constraints
        OOOOOOOOOOO0OO0OO .__O00OOO0O00O0OO0O0 =O000000O00O0O000O #line:25:self.__optional = optional
        OOOOOOOOOOO0OO0OO .__O0OOO0OOO0OOOOO0O =OOO0OO0000OOO000O #line:26:self.__check = check_func
        OOOOOOOOOOO0OO0OO .__OOO0OOOOO0OO00000 =None #line:28:self.__head = None
        OOOOOOOOOOO0OO0OO .__OO0O0OOOOO000OO00 =[]#line:30:self.__results = []
        OOOOOOOOOOO0OO0OO .__O0O00O0OO0O00O00O =[]#line:31:self.__partial = []
    def build_links (OO000O0OO00OO0OOO ):#line:33:def build_links(self):
        OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 =O0000O0000O0OO000 (None )#line:35:self.__head = HeaderNode(None)
        OOOO0OO0O00O00OOO =OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 #line:36:cursor = self.__head
        for OOO00OOO0OO00O000 in OO000O0OO00OO0OOO .__O0OOOO00O00O0O00O :#line:37:for constraint in self.__constraints:
            OOOO00O0OOOO0O0OO =O0000O0000O0OO000 (OOO00OOO0OO00O000 )#line:38:header = HeaderNode(constraint)
            OOOO0OO0O00O00OOO .next =OOOO00O0OOOO0O0OO #line:39:cursor.next = header
            OOOO00O0OOOO0O0OO .prev =OOOO0OO0O00O00OOO #line:40:header.prev = cursor
            OOOO00O0OOOO0O0OO .up =OOOO00O0OOOO0O0OO #line:42:header.up = header
            OOOO00O0OOOO0O0OO .down =OOOO00O0OOOO0O0OO #line:43:header.down = header
            OOOO0OO0O00O00OOO =OOOO00O0OOOO0O0OO #line:44:cursor = header
        OOOO0OO0O00O00OOO .next =OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 #line:45:cursor.next = self.__head
        OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 .prev =OOOO0OO0O00O00OOO #line:46:self.__head.prev = cursor
        for O0O00OOOOOOOOO00O ,OO00OO00OO0OOO0OO in enumerate (OO000O0OO00OO0OOO .__OO0O0O0OO00OOO0OO ):#line:49:for i, candidate in enumerate(self.__candidates):
            O0OO0000OOOOOO0O0 =None #line:50:rowhead = None
            OO00000O0O00OOO0O =None #line:51:current = None
            OOOO0OO0O00O00OOO =OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 .next #line:52:cursor = self.__head.next
            while OOOO0OO0O00O00OOO !=OO000O0OO00OO0OOO .__OOO0OOOOO0OO00000 :#line:53:while cursor!=self.__head:
                if OO000O0OO00OO0OOO .__O0OOO0OOO0OOOOO0O (OO00OO00OO0OOO0OO ,OOOO0OO0O00O00OOO .constraint ):#line:54:if self.__check(candidate, cursor.constraint):
                    O0OOO0OO0OOOOO00O =OOO0O0OO0000OO0OO (O0O00OOOOOOOOO00O )#line:56:node = Node(i)
                    if not O0OO0000OOOOOO0O0 :#line:58:if not rowhead:
                        O0OO0000OOOOOO0O0 =OO00000O0O00OOO0O =O0OOO0OO0OOOOO00O #line:59:rowhead = current = node
                    else :#line:60:else:
                        OO00000O0O00OOO0O .next =O0OOO0OO0OOOOO00O #line:61:current.next = node
                        O0OOO0OO0OOOOO00O .prev =OO00000O0O00OOO0O #line:62:node.prev = current
                        OO00000O0O00OOO0O =O0OOO0OO0OOOOO00O #line:63:current = node
                    O0O00OOOO0O00000O =OOOO0OO0O00O00OOO .up #line:65:temp = cursor.up
                    OOOO0OO0O00O00OOO .up =O0OOO0OO0OOOOO00O #line:66:cursor.up = node
                    O0OOO0OO0OOOOO00O .down =OOOO0OO0O00O00OOO #line:67:node.down = cursor
                    O0OOO0OO0OOOOO00O .up =O0O00OOOO0O00000O #line:68:node.up = temp
                    O0O00OOOO0O00000O .down =O0OOO0OO0OOOOO00O #line:69:temp.down = node
                OOOO0OO0O00O00OOO =OOOO0OO0O00O00OOO .next #line:71:cursor = cursor.next
            if OO00000O0O00OOO0O :#line:73:if current:
                OO00000O0O00OOO0O .next =O0OO0000OOOOOO0O0 #line:74:current.next = rowhead
                O0OO0000OOOOOO0O0 .prev =OO00000O0O00OOO0O #line:75:rowhead.prev = current
    def algorithm_x (O0O00OOO0OO0O0O0O ):#line:79:def algorithm_x(self):
        OO0OO0OOO0O00OOO0 =(O0O00OOO0OO0O0O0O .__OOO0OOOOO0OO00000 .next ==O0O00OOO0OO0O0O0O .__OOO0OOOOO0OO00000 )#line:81:empty = (self.__head.next == self.__head)
        if not OO0OO0OOO0O00OOO0 :#line:83:if not empty:
            OO0OO00OOO00000OO =True #line:84:all_empty_optional = True
            OOO000OO0OOO0OOOO =O0O00OOO0OO0O0O0O .__OOO0OOOOO0OO00000 .next #line:85:col = self.__head.next
            while OOO000OO0OOO0OOOO !=O0O00OOO0OO0O0O0O .__OOO0OOOOO0OO00000 :#line:86:while col!=self.__head:
                if OOO000OO0OOO0OOOO .constraint not in O0O00OOO0OO0O0O0O .__O00OOO0O00O0OO0O0 or OOO000OO0OOO0OOOO .down !=OOO000OO0OOO0OOOO :#line:87:if col.constraint not in self.__optional or col.down != col:
                    OO0OO00OOO00000OO =False #line:88:all_empty_optional = False
                    break #line:89:break
                OOO000OO0OOO0OOOO =OOO000OO0OOO0OOOO .next #line:90:col = col.next
        if OO0OO0OOO0O00OOO0 or OO0OO00OOO00000OO :#line:92:if empty or all_empty_optional:
            O0OOOOO00O00OO000 =sorted (O0O00OOO0OO0O0O0O .__O0O00O0OO0O00O00O )#line:93:result = sorted(self.__partial)
            if O0OOOOO00O00OO000 not in O0O00OOO0OO0O0O0O .__OO0O0OOOOO000OO00 :#line:94:if result not in self.__results:
                O0O00OOO0OO0O0O0O .__OO0O0OOOOO000OO00 .append (O0OOOOO00O00OO000 )#line:95:self.__results.append(result)
        else :#line:96:else:
            OOO000OO0OOO0OOOO =O0O00OOO0OO0O0O0O .__OOO0OOOOO0OO00000 .next #line:97:col = self.__head.next
            if OOO000OO0OOO0OOOO .down ==OOO000OO0OOO0OOOO :#line:98:if col.down == col:
                if OOO000OO0OOO0OOOO .constraint in O0O00OOO0OO0O0O0O .__O00OOO0O00O0OO0O0 :#line:99:if col.constraint in self.__optional:
                    OOO000OO0OOO0OOOO =OOO000OO0OOO0OOOO .next #line:100:col = col.next
                else :#line:101:else:
                    return #line:103:return
            O0OO0O0000OO000OO =OOO000OO0OOO0OOOO .down #line:105:row = col.down
            while O0OO0O0000OO000OO !=OOO000OO0OOO0OOOO :#line:106:while row!=col:
                O0O00OOO0OO0O0O0O .__O0O00O0OO0O00O00O .append (O0OO0O0000OO000OO .candidate )#line:108:self.__partial.append(row.candidate)
                O0O00OOO0OO0O0O0O .__OO0O00OO0O0000000 (O0OO0O0000OO000OO )#line:110:self.__cover_row(row)
                O0O00OOO0OO0O0O0O .algorithm_x ()#line:112:self.algorithm_x()
                O0O00OOO0OO0O0O0O .__O00000O00O000000O (O0OO0O0000OO000OO )#line:114:self.__uncover_row(row)
                O0O00OOO0OO0O0O0O .__O0O00O0OO0O00O00O .pop ()#line:116:self.__partial.pop()
                O0OO0O0000OO000OO =O0OO0O0000OO000OO .down #line:118:row = row.down
    def __OO0O00OO0O0000000 (OO000OOOO0OOOOO0O ,OOOO00OO0O00000O0 ):#line:120:def __cover_row(self, r):
        OO0OOO000OO0O0OOO =OOOO00OO0O00000O0 #line:121:rr = r
        OO000OOOO0OOOOO0O .__OOO0OOO0000O0000O (OOOO00OO0O00000O0 )#line:122:self.__cover_column(r)
        OOOO00OO0O00000O0 =OOOO00OO0O00000O0 .next #line:123:r = r.next
        while OOOO00OO0O00000O0 !=OO0OOO000OO0O0OOO :#line:124:while r!=rr:
            OO000OOOO0OOOOO0O .__OOO0OOO0000O0000O (OOOO00OO0O00000O0 )#line:125:self.__cover_column(r)
            OOOO00OO0O00000O0 =OOOO00OO0O00000O0 .next #line:126:r = r.next
    def __O00000O00O000000O (O000O00OO0OO0OOO0 ,OOO0O0OOO0OOO0O00 ):#line:128:def __uncover_row(self, r):
        O00OOOO0O00000000 =OOO0O0OOO0OOO0O00 #line:129:rr = r
        OOO0O0OOO0OOO0O00 =OOO0O0OOO0OOO0O00 .prev #line:130:r = r.prev
        while OOO0O0OOO0OOO0O00 !=O00OOOO0O00000000 :#line:131:while r!=rr:
            O000O00OO0OO0OOO0 .__OOOO0O00OO0OOOOO0 (OOO0O0OOO0OOO0O00 )#line:132:self.__uncover_column(r)
            OOO0O0OOO0OOO0O00 =OOO0O0OOO0OOO0O00 .prev #line:133:r = r.prev
        O000O00OO0OO0OOO0 .__OOOO0O00OO0OOOOO0 (OOO0O0OOO0OOO0O00 )#line:134:self.__uncover_column(r)
    def __OOO0OOO0000O0000O (OO00O000OOOO00OOO ,OOO0O0O0OO0O0OOOO ):#line:136:def __cover_column(self, c):
        while not isinstance (OOO0O0O0OO0O0OOOO ,O0000O0000O0OO000 ):#line:138:while not isinstance(c, HeaderNode):
            OOO0O0O0OO0O0OOOO =OOO0O0O0OO0O0OOOO .up #line:139:c = c.up
        OOO0O0O0OO0O0OOOO .next .prev =OOO0O0O0OO0O0OOOO .prev #line:142:c.next.prev = c.prev
        OOO0O0O0OO0O0OOOO .prev .next =OOO0O0O0OO0O0OOOO .next #line:143:c.prev.next = c.next
        OOOOO00OO000OO00O =OOO0O0O0OO0O0OOOO #line:146:h = c
        OOO0O0O0OO0O0OOOO =OOO0O0O0OO0O0OOOO .down #line:147:c = c.down
        while OOO0O0O0OO0O0OOOO !=OOOOO00OO000OO00O :#line:148:while c!=h:
            O00OO0000OO000O0O =OOO0O0O0OO0O0OOOO #line:149:r = c
            O0O00O0OO0O0OOOO0 =OOO0O0O0OO0O0OOOO .next #line:150:cell = c.next
            while O0O00O0OO0O0OOOO0 !=O00OO0000OO000O0O :#line:151:while cell!=r:
                O0O00O0OO0O0OOOO0 .up .down =O0O00O0OO0O0OOOO0 .down #line:152:cell.up.down = cell.down
                O0O00O0OO0O0OOOO0 .down .up =O0O00O0OO0O0OOOO0 .up #line:153:cell.down.up = cell.up
                O0O00O0OO0O0OOOO0 =O0O00O0OO0O0OOOO0 .next #line:154:cell = cell.next
            OOO0O0O0OO0O0OOOO =OOO0O0O0OO0O0OOOO .down #line:155:c = c.down
    def __OOOO0O00OO0OOOOO0 (OO0O00O0O000OO0O0 ,OO0000O00OO00O0O0 ):#line:157:def __uncover_column(self, c):
        while not isinstance (OO0000O00OO00O0O0 ,O0000O0000O0OO000 ):#line:159:while not isinstance(c, HeaderNode):
            OO0000O00OO00O0O0 =OO0000O00OO00O0O0 .up #line:160:c = c.up
        OO0000O00OO00O0O0 .prev .next =OO0000O00OO00O0O0 #line:162:c.prev.next = c
        OO0000O00OO00O0O0 .next .prev =OO0000O00OO00O0O0 #line:163:c.next.prev = c
        OO0O0000O0OO0O000 =OO0000O00OO00O0O0 #line:165:h = c
        OO0000O00OO00O0O0 =OO0000O00OO00O0O0 .up #line:166:c = c.up
        while OO0000O00OO00O0O0 !=OO0O0000O0OO0O000 :#line:167:while c!=h:
            O0OOO0O0OO000O00O =OO0000O00OO00O0O0 #line:168:r = c
            O000OO00OOO00OO00 =OO0000O00OO00O0O0 .next #line:169:cell = c.next
            while O000OO00OOO00OO00 !=O0OOO0O0OO000O00O :#line:170:while cell!=r:
                O000OO00OOO00OO00 .up .down =O000OO00OOO00OO00 #line:171:cell.up.down = cell
                O000OO00OOO00OO00 .down .up =O000OO00OOO00OO00 #line:172:cell.down.up = cell
                O000OO00OOO00OO00 =O000OO00OOO00OO00 .next #line:173:cell = cell.next
            OO0000O00OO00O0O0 =OO0000O00OO00O0O0 .up #line:174:c = c.up
    def get_results (OOOOO0OOOO00O0OOO ):#line:176:def get_results(self):
        return [[OOOOO0OOOO00O0OOO .__OO0O0O0OO00OOO0OO [OO000OOOO0OOOOOO0 ]for OO000OOOO0OOOOOO0 in OO0O00OOO0O000O0O ]for OO0O00OOO0O000O0O in OOOOO0OOOO00O0OOO .__OO0O0OOOOO000OO00 ]#line:179:return [[self.__candidates[x] for x in result] for result in self.__results]
def OOOO0O0O0OOO0OO00 (O0O0O0O00O0000000 ):#line:181:def solve_N_queens(n):
    OO0OOO0O00O0OO0O0 =[(O00O0OO0OOOOO000O ,OOOOOOO000OOO0OO0 )for O00O0OO0OOOOO000O in range (O0O0O0O00O0000000 )for OOOOOOO000OOO0OO0 in range (O0O0O0O00O0000000 )]#line:182:candidates = [(x, y) for x in range(n) for y in range(n)]
    O0OOOO000OOO00O00 =[]#line:183:constraints = []
    O0O00O0000OOOOO0O =[]#line:184:optional = []
    for O0OO00OO0O0000O0O in range (O0O0O0O00O0000000 ):#line:185:for i in range(n):
        O0OOOO000OOO00O00 .append (('row',O0OO00OO0O0000O0O ))#line:187:constraints.append(('row', i))
    for O0OO00OO0O0000O0O in range (O0O0O0O00O0000000 ):#line:188:for i in range(n):
        O0OOOO000OOO00O00 .append (('col',O0OO00OO0O0000O0O ))#line:190:constraints.append(('col', i))
    for O0OO00OO0O0000O0O in range (O0O0O0O00O0000000 *2 -1 ):#line:193:for i in range(n*2-1):
        O0OOOO000OOO00O00 .append (('diag',O0OO00OO0O0000O0O ))#line:195:constraints.append(('diag', i))
        O0O00O0000OOOOO0O .append (('diag',O0OO00OO0O0000O0O ))#line:196:optional.append(('diag', i))
    for O0OO00OO0O0000O0O in range (O0O0O0O00O0000000 *2 -1 ):#line:197:for i in range(n*2-1):
        O0OOOO000OOO00O00 .append (('rdiag',O0OO00OO0O0000O0O ))#line:198:constraints.append(('rdiag', i))
        O0O00O0000OOOOO0O .append (('rdiag',O0OO00OO0O0000O0O ))#line:199:optional.append(('rdiag', i))
    def OOO0OOO0OOO00OO0O (O0OO00O000O00O00O ,O00OOOOO000000O00 ):#line:201:def checker(candidate, constraint):
        OOOO0OO000OO00O0O ,O000O0O0000O00000 =O00OOOOO000000O00 #line:202:t, val = constraint
        if OOOO0OO000OO00O0O =='row':#line:203:if t=='row':
            return O0OO00O000O00O00O [0 ]==O000O0O0000O00000 #line:204:return candidate[0]==val
        if OOOO0OO000OO00O0O =='col':#line:205:if t=='col':
            return O0OO00O000O00O00O [1 ]==O000O0O0000O00000 #line:206:return candidate[1]==val
        if OOOO0OO000OO00O0O =='diag':#line:207:if t=='diag':
            return (O0OO00O000O00O00O [0 ]+O0OO00O000O00O00O [1 ])==O000O0O0000O00000 #line:208:return (candidate[0]+candidate[1])==val
        else :#line:209:else:
            return (O0O0O0O00O0000000 -1 -O0OO00O000O00O00O [0 ]+O0OO00O000O00O00O [1 ])==O000O0O0000O00000 #line:210:return (n-1-candidate[0]+candidate[1])==val
    O0OOO0O0O0000O0OO =O000000OOO0OO000O (OO0OOO0O00O0OO0O0 ,O0OOOO000OOO00O00 ,O0O00O0000OOOOO0O ,OOO0OOO0OOO00OO0O )#line:212:dl = DancingLinks(candidates, constraints, optional, checker)
    O0OOO0O0O0000O0OO .build_links ()#line:213:dl.build_links()
    O0OOO0O0O0000O0OO .algorithm_x ()#line:214:dl.algorithm_x()
    OOO0O0O0OO0O000O0 =O0OOO0O0O0000O0OO .get_results ()#line:215:results = dl.get_results()
    for OO0OOO0O0O0000OOO in OOO0O0O0OO0O000O0 :#line:217:for result in results:
        print ("+++++++++")#line:218:print("+++++++++")
        for O0OO00OO0O0000O0O in range (O0O0O0O00O0000000 ):#line:219:for i in range(n):
            OOOOOO00O0OO00OO0 =""#line:220:s = ""
            for OO00OOO0OOO0000OO in range (O0O0O0O00O0000000 ):#line:221:for j in range(n):
                if (O0OO00OO0O0000O0O ,OO00OOO0OOO0000OO )in OO0OOO0O0O0000OOO :#line:222:if (i, j) in result:
                    OOOOOO00O0OO00OO0 +="1"#line:223:s+="1"
                else :#line:224:else:
                    OOOOOO00O0OO00OO0 +="0"#line:225:s+="0"
            print (OOOOOO00O0OO00OO0 )#line:226:print(s)
        print ("+++++++++")#line:227:print("+++++++++")
    print ("%d results found for N-Queen"%len (OOO0O0O0OO0O000O0 ))#line:228:print("%d results found for N-Queen"%len(results))
def O0OO0O0OOOOO00OO0 ():#line:230:def main():
    OOOO0O0O0OOO0OO00 (10 )#line:231:solve_N_queens(10)
if __name__ =="__main__":#line:233:if __name__ == "__main__":
    O0OO0O0OOOOO00OO0 ()#line:234:main()


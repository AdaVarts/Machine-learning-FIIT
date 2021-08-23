import copy

class Rule(object):
    def __init__(self, name):
        self.name = name
        self.condition = ""
        self.outcome = ""
        self.listC = []
        self.same = []

    # Gets all conditions from the rule without '?' substrings
    def m(self):
        for con in self.condition.split(','):
            txt = con.split(' ')
            for i in txt:
                if '?' in i:
                    txt.remove(i)
            for i in txt:
                if '?' in i:
                    txt.remove(i)
            self.listC.append(txt)

    # Writes positions in string where is '?', removes all substrings with '?'
    def exec(self, facts):
        a={}
        conditions = self.condition.split(',')
        for con in conditions:
            txt = con.split(' ')
            for i in txt:
                if '?' in i:
                    if i not in a: a[i] = [[conditions.index(con), txt.index(i)]]
                    else: a[i].append([conditions.index(con), txt.index(i)])
        b = {}
        for k in a.keys():
            if len(a[k]) > 1:
                b[k] = copy.deepcopy(a[k])
        right = []

        # Compares substrings on positions of same '?' label
        for k in b.keys():
            for fact in facts[2]:
                for fact2 in facts[3]:
                    if fact.split(' ')[b[k][0][1]] == fact2.split(' ')[b[k][1][1]]:
                        if "<>" in conditions[len(conditions)-1]:
                            con = conditions[len(conditions)-1].split(' ')
                            if fact.split(' ')[a[con[1]][0][1]] == fact2.split(' ')[a[con[2]][0][1]]: continue
                        right.append([fact, fact2])
        if len(right) == 0:
            return

        # Writes final executable actions with data
        do_list = []
        for r in right:
            txt = str(copy.deepcopy(self.outcome))
            for re in self.outcome.split(','):
                for res in re.split(' '): 
                    if '?' in res:
                        txt = txt.replace(res, r[a[res][0][0]].split(' ')[a[res][0][1]])
                do_list.append(txt)
        # print(do_list)

        return do_list

    def __repr__(self):
        return self.name + "\n" + self.condition + "\n" + self.outcome + "\n"
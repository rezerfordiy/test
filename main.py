import re
import random
import datetime
class Question:
    def __init__(self, info, *q, ans=[], note = None):
        self.info = info
        self.variants = list(q[:])
        self.ans = ans[:]
        self.note = note
    def check(self, k):
        return self.variants[k] in self.ans
    
    def shuffle(self):
        random.shuffle(self.variants)

    def __str__(self):
        return f"{self.info}\n{self.variants}\n{self.ans}\n" + (f"{self.note}\n" if self.note is not None else '')
    



def main():
    file = 'questions/test.txt'

    try:
        with open(file, 'r', encoding='utf-8') as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("файла нет")
        return




    
    qs = parse(lines)

    total = len(qs)
    good = 0
    st1=datetime.datetime.now()

    for i in qs:
        i.shuffle()
    random.shuffle(qs)
    print("Начинаю тестирование")
    for i,q in enumerate(qs):
        print(f"Вопрос {i + 1}/{total}: {q.info}\n")
        for j, ask in enumerate(q.variants):
            print(f"{j+1}. {ask}")
        correct = False
        while not correct:
            user = input()
            try:
                user = int(user)
            except:
                print("Неправильнные данные")
                continue
            if 1<=user<=len(q.variants):
                correct = True
            else:
                print("Нет такого ответа")
        if (q.check(user - 1)):
            print("Правильно")
            good+=1
        else:
            print("Неправильно\nОтветы:")
            print(*q.ans)
            if q.note is not None:
                print(q.note)

        if i < len(qs) -1:
            print("Переходим к следующему вопросу...")
    end1=datetime.datetime.now()
    print("Тестирование завершенно")
    print(f"Общее количество вопросов: {total}\nКоличество правильных ответов: {good}\nПроцент правильных ответов: {good / total *100}%\n")


    with open("result.txt", 'a') as f:
        f.write(f"Время начала теста: {st1}\n")
        f.write(f"Время окончания теста: {end1}\n")
        f.write(f"Общее количество вопросов: {total}\nКоличество правильных ответов: {good}\nПроцент правильных ответов: {good / total *100}%\n\n")



        
    




    
    

def parse(mas):
    for i in range(len(mas)):
        mas[i] = mas[i].strip()
    mas = [i for i in mas if len(i) > 0]
    mas = [i[3:] if i[:7] != "Ответ: " else i for i in mas ]
    qq = []
    i = 0
    while i < len(mas):
        nt = None

        q = mas[i]
        i+=1
        lst = []
        while (i < len(mas) and 'Ответ: ' not in mas[i]):
            lst.append(mas[i])
            i+=1
        if i < len(mas):
            a = re.findall(r'\d+|\D+', mas[i][7:])
            otvets = []
            for k,j in enumerate(a):
                if j in '1234567890':
                    a[k] = lst[int(j) - 1]
                    otvets.append(a[k])
            i+=1
            if len(a)>1:
                nt = ' '.join(a)


        qq.append(Question(q, *lst, ans=otvets, note=nt))
    
    
    
    return qq





if __name__ == "__main__":

    main()
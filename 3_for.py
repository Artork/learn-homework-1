"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    scool_10 = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4б', 'scores': [3,4,4,5,2]}, 
      {'school_class': '4в', 'scores': [5,5,5,5,5]}, 
      {'school_class': '4г', 'scores': [4,4,4,4,4]} 
      ]

    sum_scores = 0
    sum_pupol = 0
    for i in range(len(scool_10)):
      scores = sum(scool_10[i]['scores'])
      pupol =  len(scool_10[i]['scores'])
      sum_scores += scores
      sum_pupol += pupol
    print(sum_scores)
    print(sum_pupol)
    print(sum_scores/sum_pupol)
    

    #for i in range(len(scool_10)):
    # pupol =  len(scool_10[i]['scores'])
    # sum_pupol += pupol
    #print(sum_pupol)
    #print(sum_scores)
      






if __name__ == "__main__":
    main()

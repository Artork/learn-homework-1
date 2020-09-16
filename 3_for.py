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
    for item in scool_10:
      scores = sum(item['scores'])
      pupol =  len(item['scores'])
      sum_scores += scores
      sum_pupol += pupol
    print('Средняя оценка в школе: ', sum_scores/sum_pupol)
    
   
    for i in range(len(scool_10)):
      score_class = sum(scool_10[i]['scores'])
      pupol_class = len(scool_10[i]['scores'])
      print('В классе ', scool_10[i]['school_class'], 'Средняя оценка: ', score_class/pupol_class)


   






if __name__ == "__main__":
    main()

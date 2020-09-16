"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
  scool_10 = [
      {'school_class': '4a', 'scores': [3,4,4,5,2]},
      {'school_class': '4б', 'scores': [3,4,4,5,2]}, 
      {'school_class': '4в', 'scores': [5,5,5,5,5]}, 
      {'school_class': '4г', 'scores': [4,4,4,4,4]} 
  ]
  score_class = 0
  pupol_class = 0
  sum_scores = 0
  sum_pupol = 0
  for item in scool_10:
    scores = sum(item['scores'])
    pupol =  len(item['scores'])
    score_class = sum(item['scores'])
    pupol_class = len(item['scores'])
    sum_scores += scores
    sum_pupol += pupol
    print('В классе ', item['school_class'], 'Средняя оценка: ', round((score_class/pupol_class),1))
  print('Средняя оценка в школе: ', round((sum_scores/sum_pupol),1))

   
if __name__ == "__main__":
    main()

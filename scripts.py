import random
from datacenter.models import Schoolkid, Lesson, Commendation, Chastisement, Mark


commendation_texts = [
    "Молодец!",
    "Отлично!",
    "Хорошо!",
    "Гораздо лучше, чем я ожидал!",
    "Ты меня приятно удивил!",
    "Великолепно!",
    "Прекрасно!",
    "Ты меня очень обрадовал!",
    "Именно этого я давно ждал от тебя!"
]

def find_schoolkid(schoolkid_name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=schoolkid_name)
        return schoolkid
    except Schoolkid.MultipleObjectsReturned:
        print(f"Найдено несколько учеников с именем, содержащим '{schoolkid_name}'. Уточните запрос.")
        return None
    except Schoolkid.DoesNotExist:
        print(f"Учёник с именем, содержащим '{schoolkid_name}', не найден.")
        return None

def fix_marks(schoolkid):
    bad_marks = Mark.objects.filter(schoolkid=schoolkid, points__in=[2, 3])
    count = bad_marks.count()
    for mark in bad_marks:
        mark.points = 5
        mark.save()
    print(f"Исправлено {count} оценок для ученика {schoolkid.full_name}.")

def delete_chastisements_for(schoolkid_name):
    schoolkid = find_schoolkid(schoolkid_name)
    if schoolkid:
        chastisements = Chastisement.objects.filter(schoolkid=schoolkid)
        count = chastisements.count()
        chastisements.delete()
        print(f"Удалено {count} замечаний для {schoolkid.full_name}.")

def create_commendation(schoolkid_name, subject_name):
    schoolkid = find_schoolkid(schoolkid_name)
    if not schoolkid:
        return

    lesson = Lesson.objects.filter(
        subject__title=subject_name,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    ).order_by('-date').first()
    
    if lesson:
        commendation_text = random.choice(commendation_texts)
        Commendation.objects.create(
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher,
            text=commendation_text,
            created=lesson.date
        )
        print(f"Похвала для {schoolkid.full_name} создана по предмету '{subject_name}' на дату {lesson.date}.")
    else:
        print(f"Не найден урок по предмету '{subject_name}' для {schoolkid.full_name}.")


delete_chastisements_for('Фролов Иван')


schoolkid = find_schoolkid('Фролов Иван')
if schoolkid:
    fix_marks(schoolkid)


create_commendation('Фролов Иван', 'Музыка')

import random
from django.shortcuts import render, get_object_or_404
from .models import Level, Word, Category

def index(request):
    levels = Level.objects.all().prefetch_related('category_set')
    # Добавляем категории для каждого уровня
    levels_with_categories = []
    for level in levels:
        categories = Category.objects.filter(level=level).values_list('name', flat=True)
        # Убираем часть после двоеточия из названия уровня (например, "Level 1: Humans" -> "Level 1")
        level_name_short = level.name.split(':')[0] if ':' in level.name else level.name
        levels_with_categories.append({
            'level': level,
            'level_name_short': level_name_short,
            'categories': list(categories)
        })
    return render(request, 'index.html', {'levels_data': levels_with_categories})

def quiz(request, level_id):
    level = get_object_or_404(Level, id=level_id)
    words = list(Word.objects.filter(category__level=level))
    
    # Проверяем, что есть слова для квиза
    if not words:
        from django.http import HttpResponse
        return HttpResponse("Нет слов для этого уровня. Обратитесь к администратору.")
    
    quiz_data = []
    for w in words:
        # ИСПРАВЛЕНИЕ: Берем неправильные ответы ТОЛЬКО из той же категории
        category_kazakh = list(
            Word.objects.filter(category=w.category)
            .exclude(id=w.id)  # Исключаем текущее слово
            .values_list('kazakh', flat=True)
            .distinct()
        )
        
        # Если в категории мало слов (меньше 3), используем весь уровень как fallback
        if len(category_kazakh) < 3:
            print(f"DEBUG: Category '{w.category.name}' has only {len(category_kazakh)} words, using level fallback")
            wrong_candidates = list(
                Word.objects.filter(category__level=level)
                .exclude(id=w.id)
                .values_list('kazakh', flat=True)
                .distinct()
            )
        else:
            wrong_candidates = category_kazakh
        
        # Определяем количество неправильных ответов (минимум 3, но не больше доступных)
        num_wrong = min(3, len(wrong_candidates))
        
        if num_wrong > 0:
            wrong = random.sample(wrong_candidates, num_wrong)
        else:
            # Если совсем нет других слов, оставляем пустой список
            wrong = []
        
        # Создаем список вариантов ответов
        options = [w.kazakh] + wrong
        random.shuffle(options)
        
        quiz_data.append({
            'q': w.english,
            'a': w.kazakh,
            'opts': options,
            'category': w.category.name  # Добавляем для отладки
        })
    
    # Перемешиваем вопросы для разнообразия
    random.shuffle(quiz_data)
    
    # Отладочная информация
    print(f"DEBUG: Level: {level.name}, Questions generated: {len(quiz_data)}")
    if quiz_data:
        print(f"DEBUG: First question: {quiz_data[0]['q']} ({quiz_data[0]['category']}) -> {quiz_data[0]['a']}")
        print(f"DEBUG: Options: {quiz_data[0]['opts']}")
    
    return render(request, 'quiz.html', {
        'quiz_data': quiz_data, 
        'level': level,
        'total_questions': len(quiz_data)
    })

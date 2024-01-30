from .models import *

def get_courses_category(course_name):
    context = {}
    # Query all categories and their related sub-categories
    categories = Category.objects.filter(subject__name=course_name)
    
    sub_categories = Sub_Category.objects.all()
    # Loop through each category and retrieve its related sub-categories
    for category in categories:
        subcategories = Sub_Category.objects.filter(category=category)
        subcategory_list = [{'name': sub.name, 'more_sub': sub.more_sub, 'details': sub.details} for sub in subcategories]
        
        # Add the category and its subcategories to the dictionary
        context[category.name] = subcategory_list
    # context['course_name'] = course_name
    # print('context: ---', context)
    return context
def student(*marks,sit=False):
    """
    Analyzes student's performance based on grades.
    :param marks: One or more numerical grades.
    :param sit: (optional) If true, shows a status assessment.
    :return: Dictionary with performance summary.
    """
    performance = {}
    performance['quantity'] = len(marks)
    performance['highest'] = max(marks)
    performance['lowest'] = min(marks)
    avg = sum(marks) / len(marks)
    performance['average'] = round(avg,2)
    if sit:
        if avg <= 5:
            performance['situation'] = 'You failed'
        elif 5 < avg < 7:
            performance['situation'] = 'You need to retake the exam'
        else:
            performance['situation'] = 'You passed!'
    return performance

print(student(10,4,5, sit=True))


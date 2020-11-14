from django.http import HttpResponse


def page_2003(request):
    return HttpResponse('这是page2003页面')


def page_num(request, num):
    html = '<h3>这是编号为%s的页面</h3>' % (num)
    return HttpResponse(html)


def cal_view(request, num1, op, num2):
    if op not in ['add', 'sub', 'mul']:
        return HttpResponse('Your operation is wrong')
    result = 0
    if op == 'add':
        result = num1 + num2
    elif op == 'sub':
        result = num1 - num2
    elif op == 'mul':
        result = num1 * num2
    return HttpResponse('结果是%s' % result)


def default_page(request):
    html = '<h1>这是默认首页,别再找火箭页面了</h1>'
    return HttpResponse(html)


def birthday_view(request, y, m, d):
    print('******************')
    print(request.path_info)
    print(request.method)
    print(request.get_full_path())

    # 1得到的是一个类字典的结构
    print(request.GET)
    # 2 如果a有多个值,拿到是最后一个
    print(request.GET['a'])
    # 3 如果a有多个值,getlist获取所有a的值
    print(request.GET.getlist('a'))
    print(request.GET['b'])
    # 4 温柔的获取,一般对于查询字符串的值,采用这种获取方式
    print(request.GET.get('c',1000))

    print('******************')
    html = '生日为:%s年%s月%s日' % (y, m, d)
    return HttpResponse(html)

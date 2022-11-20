import sys

print('%s=%s' % ('spam', 42))                   #вираз форматування
print('{0}={1}'.format('spam', 42))             #метод форматування
print('{}={}'.format('spam', 42))               #автоматична нумерація

print('%s, %s and %s' % (3.14, 42, [1, 2]))     #довільні типи
print('My %(kind)s runs %(platform)s' % {'kind': 'laptop', 'platform': sys.platform})
print('My %(kind)s runs %(platform)s' % dict(kind='laptop', platform=sys.platform))

somelist = list('SPAM')
parts = somelist[0], somelist[-1], somelist[1:3]
print('first=%s, last=%s, midle=%s' % parts)

print('%-10s = %10s' % ('spam', 123.4567))
print('%10s = %-10s' % ('spam', 123.4567))
print('%(plat)10s = %(kind)-10s' % dict(plat=sys.platform, kind='laptop'))
print('%e, %.3e, %g' % (3.14159, 3.14159, 3.14159))
print('%f, %.2f, %06.2f' % (3.14159, 3.14159, 3.14159))
print('%x, %o' % (255, 255))

print('My {1[kind]:<8} rusn {0.platform:>8}'.format(sys, {'kind': 'laptop'}))
print('My %(kind)-8s runs %(plat)8s' % dict(kind='laptop', plat=sys.platform))

data = dict(platform=sys.platform, kind='laptop')
print('My {kind:<8} runs {platform:>8}'.format(**data))
print('My %(kind)-8s runs %(platform)8s' % data)

print('{0:d}'.format(999999999999))
print('{0:,d}'.format(999999999999))

print('{:,d}'.format(999999999999))
print('{:,d} {:,d}'.format(9999999, 8888888))
print('{:,.2f}'.format(296999.2567))
print('*    *\t   **  \t *****\t *****\n'
      '*   * \t  *  * \t   *  \t *\n'
      '*  *  \t *    *\t   *  \t *\n'
      '* *   \t *    *\t   *  \t *\n'
      '**    \t ******\t   *  \t *****\n'
      '* *   \t *    *\t   *  \t *\n'
      '*  *  \t *    *\t   *  \t *\n'
      '*   * \t *    *\t   *  \t *\n'
      '*    *\t *    *\t   *  \t *****')

print('==========================================')

print('Escape sequences')
print('\\a\tBell (alert)')
print('\\b\tBackspace')
print('\\n\tNew line')
print('\\t\tHorizontal tab')
print('\\\\\tBackslash \\')
print('\\”\tDouble quotation mark “')
print('\\’\tSingle quotation mark ‘')

print('==========================================')

x = 12
y = 64
print(x, y)
print('x:{X}, y:{Y}'.format(Y=y, X=x))
print('Result of sum {X} and {Y}: {Z}'.format(Y=y, X=x, Z=x + y))
print('Result of division {Y} and {X}: {Z}'.format(Y=y, X=x, Z=y//x))
print('Rest of division {Y} and {X}: {Z}'.format(Y=y, X=x, Z=y % x))
print('{X} to the {Y} power: {Z}'.format(Y=y, X=x, Z=x**y))

print('==========================================')
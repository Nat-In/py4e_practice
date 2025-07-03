# arithmetic operators(aрифметические операторы):
# +	addition
# -	subtraction
# *	multiplication
# /	division(always float)
# // integer division(целочисленное деление)	10 // 3 ->	3
# %	modulo/remainder(остаток от деления)	10 % 3 ->	1
# **	возведение в степень

# comparison operators(операторы сравнения):
# ==	equal	5 == 5	True
# !=	not equal	5 != 4	True
# >	greater than	6 > 2	True
# <	less than	3 < 4	True
# >=	greater than or equal	5 >= 5	True
# <=	less than or equal	2 <= 3	True

# assignment operators(операторы присваивания):
# =	simple assignment
# +=	add and assign	x += 2	=> x=x+2
# -=	subtract end assign	x -= 1	=> x=x-1
# *=	multiply and assign	x *= 3	=> x=x*3
# /=	divide and assign	x /= 2	=> x=x/2
# //=	integer divide and assign	x //= 2	=> x=x//2
# %=	modulo and assign	x %= 2	=> x=x%2
# **=	exponentiate and assign(в степень)	x **= 2	=> x=x**2

# logical operators(логические операторы(работают с True и False):
# and	-logical AND -True and False	-> False
# or	-logical OR	-True or False	-> True
# not	-logical NOT -not True	-> False

# membership operators(операторы принадлежности):
# in	-membership check(проверка вхождения)	-'a' in 'cat'	-> True
# not in	-non-membership check(отсутствиe вхождения)	-'a' not in 'cat'	-> False

# identity operators(операторы идентичности(сравнение по объекту, не по значению):
# is	-object identity check(являются ли объекты одним и тем же)	a is b ->	True/False
# is not	-object non-identity check(не являются)	a is not b	-> True/False

# bitwise operators(побитовые операторы):
# они работают с двоичными представлениями чисел(битами)
# исп. в системном програмировании, разработке драйверов и встроеных систем(embedded) криптографии
# исп. в сжатие и обработка данных, графика и игры, сетевое программирование, алгоритмы и структуры данных
# безопасность и шифрование, работа с низкоуровневыми данными
# быстроя упаковка/распаковка информации
# управление флагами и настройками в виде битов
# pабота с регистрами процессора,портами ввода-вывода,памятью
# &	-bitwise AND	=> 5 & 3	=> 0b0101 & 0b0011 = 0b0001 → 1
# |	-bitwise OR	=> 5 | 3	=> 0b0101 | 0b0011 = 0b0111 → 7
# ^	-bitwise XOR (еxclusive OR)	=> 5 ^ 3	0b0101 ^ 0b0011 = 0b0110 → 6
# ~	-bitwise NOT	=> ~5	инвертирует все биты (даёт -6)
# <<	left bitwise shift(cдвиг влево)	5 << 1	0b0101 → 0b1010 → 10   -nри сдвиге влево справа добавляются нули
# >>	right bitwise shift	5 >> 1	0b0101 → 0b0010 → 2  -при сдвиге вправо слева добавляются нули


default_settings = 0b0000
LIGHT_ON = 0b0001
VIDEO_ON = 0b0010
SOUND_ON = 0b0100
GATE_OPEN = 0b1000

# 1=0b0001
LIGHT_ON = 1 << 0  # 0b0001
VIDEO_ON = 1 << 1  # 0b0010
SOUND_ON = 1 << 2  # 0b0100
GATE_OPEN = 1 << 3  # 0b1000

settings = default_settings

settings_light_on = settings | LIGHT_ON  # 0b0001
# ~LIGHT_ON=0b1110
settings_light_off = settings_light_on & ~LIGHT_ON  # 0b0000

light_check = settings & LIGHT_ON
if light_check:
    print("Light ON")  # light_check=0b0001
else:
    print("Light OFF")  # light_check=0b0000

turn_on_video_sound = settings | VIDEO_ON | SOUND_ON  # 0b0110
# ~SOUND_ON=0b1011
turn_off_sound = turn_on_video_sound & ~SOUND_ON  # 0b0010

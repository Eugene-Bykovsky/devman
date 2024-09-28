import time

# Вывод первой планеты
print("\u001b[34m", end="")
print("""\
                _-o#&&*''''?d:>b\\_
              _o/'`''  '',, dMF9MMMMMHo_
           .o&#'        `'MbHMMMMMMMMMMMHo.
         .o'' '         vodM*$&&HMMMMMMMMMM?.
        ,'              $M&ood,~'`(&##MMMMMMH\\
       /               ,MMMMMMM#b?#bobMMMMHMMML
      &              ?MMMMMMMMMMMMMMMMM7MMM$R*Hk
     ?$.            :MMMMMMMMMMMMMMMMMMM/HMMM|`*L
    |               |MMMMMMMMMMMMMMMMMMMMbMH'   T,
    $H#:            `*MMMMMMMMMMMMMMMMMMMMb#}'  `?
    ]MMH#             ''*''''*#MMMMMMMMMMMMM'    -
    MMMMMb_                   |MMMMMMMMMMMP'     :
    HMMMMMMMHo                 `MMMMMMMMMT       .
    ?MMMMMMMMP                  9MMMMMMMM}       -
    -?MMMMMMM                  |MMMMMMMMM?,d-    '
     :|MMMMMM-                 `MMMMMMMT .M|.   :
      .9MMM[                    &MMMMM*' `'    .
       :9MMk                    `MMM#'        -
         &M}                     `          .-
          `&.                             .
            `~,   .                     ./
                . _                  .-PP
                  '`--._,dd###pp=''
""",
      end="")

# Задержка
time.sleep(1)

# Очистка экрана
print("\033[2J", end="")

# Перемещение курсора в начало
print("\u001b[23A", end="")

# Вывод второй планеты
print("\u001b[32m", end="")
print("""\
                 .ovr:HMM#?:`' >b\\_
              .,:&Hi' `'   '' \\\\|&bSMHo_
            oHMMM#*}          `?&dMMMMMMHo.
         .dMMMH'''''           ,oHH*&&9MMMM?.
        ,MMM*'                 `*M\\bd<|'*&#MH\\
       dHH?'                   :MMMMMM#bd#odMML
      H' |\\                  `dMMMMMMMMMMMMMM9Mk
     JL/'7+,.                `MMMMMMMMMMMMMMMH9ML
    -`Hp     '               |MMMMMMMMMMMMMMMMHH|:
    :  \\\\#M#d?                `HMMMMMMMMMMMMMMMMH.
    .   JMMMMM##,              ``*''''*#MMMMMMMMH
    -. ,MMMMMMMM6o_                    |MMMMMMMM':
    :  |MMMMMMMMMMMMMb\\                 TMMMMMMT :
    .   ?MMMMMMMMMMMMM'                 :MMMMMM|.`
    -    ?HMMMMMMMMMM:                  HMMMMMM\\|:
     :     9MMMMMMMMH'                 `MMMMMP.P.
      .    `MMMMMMT''                   HMMM*''-
       -    TMMMMM'                     MM*'  -
        '.   HMM#                            -
          -. `9M:                          .'
            -. `b,,    .                . '
              '-\\   .,               .-`
                  '-:b~\\\\_,oddq==--'
""",
      end="")

# Сброс цвета в конце
print("\u001b[0m", end="")

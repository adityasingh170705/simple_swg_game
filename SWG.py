print('''
░██████╗███╗░░██╗░█████╗░██╗░░██╗███████╗  ░██╗░░░░░░░██╗░█████╗░████████╗███████╗██████╗░  ░██████╗░██╗░░░██╗███╗░░██╗
██╔════╝████╗░██║██╔══██╗██║░██╔╝██╔════╝  ░██║░░██╗░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗  ██╔════╝░██║░░░██║████╗░██║
╚█████╗░██╔██╗██║███████║█████═╝░█████╗░░  ░╚██╗████╗██╔╝███████║░░░██║░░░█████╗░░██████╔╝  ██║░░██╗░██║░░░██║██╔██╗██║
░╚═══██╗██║╚████║██╔══██║██╔═██╗░██╔══╝░░  ░░████╔═████║░██╔══██║░░░██║░░░██╔══╝░░██╔══██╗  ██║░░╚██╗██║░░░██║██║╚████║
██████╔╝██║░╚███║██║░░██║██║░╚██╗███████╗  ░░╚██╔╝░╚██╔╝░██║░░██║░░░██║░░░███████╗██║░░██║  ╚██████╔╝╚██████╔╝██║░╚███║
╚═════╝░╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝░░╚═╝  ░╚═════╝░░╚═════╝░╚═╝░░╚══╝''')
import random
print("\n")

b= input("Choose Snake(s), Water(w) or Gun(g) :")

print('''YOU CHOSE:  
      
      ''')
if b =='s':
    print('''
       ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\
       `/'\__/      \ _ _ \*\
      /^|            \ _ _ \*''')

elif b=='w':
    print('''
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~''')
elif b=='g':
    print('''
                                    ______
        |\_______________ (_____\______________
HH======#H###############H#######################
        ' ~""""""""""""""`##(_))#H"""""Y########
                          ))    \#H\       `"Y###
                          "      }#H)''')
print('\n')    
print('\n')
    
print('''COMPUTER CHOSE:  
      
      ''')
    

a=random.randint(1,3)
if a ==1:
    cs= "s"
    print('''
       ---_ ......._-_--.
      (|\ /      / /| \  \
      /  /     .'  -=-'   `.
     /  /    .'             )
   _/  /   .'        _.)   /
  / o   o        _.-' /  .'
  \          _.-'    / .'*|
   \______.-'//    .'.' \*|
    \|  \ | //   .'.' _ |*|
     `   \|//  .'.'_ _ _|*|
      .  .// .'.' | _ _ \*|
      \`-|\_/ /    \ _ _ \*\
       `/'\__/      \ _ _ \*\
      /^|            \ _ _ \*''')
elif a==2:
    cs= "w"
    print('''
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~
~^~^~^~^~^~^~^~^~^~^~''')
elif a==3:
    cs= "g"
    print('''
                                    ______
        |\_______________ (_____\______________
HH======#H###############H#######################
        ' ~""""""""""""""`##(_))#H"""""Y########
                          ))    \#H\       `"Y###
                          "      }#H)''')


print('\n')    
print('\n')  
def game(comp, user):
    if comp== 's' and user== 'w':
        user=="loser"
    if comp== 'w' and user== 's':
        user=="winner"
    if comp== 'w' and user== 'g':
        user=="loser"
    if comp== 'g' and user== 'w':
        user="winner"
    if comp== 'g' and user== 's':
        user=="loser"
    if comp== 's' and user== 'g':
        user="winner"
    if comp== 's' and user== 's':
        user= 'draw'
    if comp== 'w' and user== 'w':
        user= 'draw'
    if comp== 'g' and user== 'g':
        user= 'draw'
    
    
    
    if user=="winner":
        print('You WON!')
    elif user=="draw":
        print('Its a DRAW!')
    else:
        print('You LOST!')

    

game(cs, b)


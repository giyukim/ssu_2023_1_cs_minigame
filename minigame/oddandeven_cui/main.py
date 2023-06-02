def main():
    import random
    import time
    print('홀짝게임을 시작합니다.')
    print('시드 머니는 10만원이고, 상대의 돈을 1만원 미만으로 만들어야 승리할 수 있습니다.')
    print('홀짝은 컴퓨터와 유저가 건 돈의 총합의 일의 자리 숫자로 결정됩니다.')
    print('유저가 홀, 짝을 고르고 맞추면 건 돈을 모두 가져가고, 틀리면 컴퓨터가 가져갑니다.')
    print('움직이는 돈은 건 돈 중 더 적은 돈이다.')
    usm=100000
    csm=100000
    i=0
    while 1:
        print('')
        print("")
        i+=1  
        time.sleep(0.8)
        print('='*50)
        print('='*50)
        print(f'<{i}번째 베팅입니다.>')
        time.sleep(1)
        print(f'컴퓨터의 잔액은 <{csm}>원 입니다.')
        print(f'당신의 잔액은 <{usm}>원 입니다.')
        print('')
        print('*'*50)
        time.sleep(0.5)
        print(f'컴퓨터는 베팅했습니다.')
        time.sleep(0.8)
        cb=random.randint(0,csm)
        while 1:
            try:
                ub=int(input('얼마를 베팅하시겠습니까?: '))
                if ub<0 or ub>usm:
                    print("그만한 돈이 없습니다.")
                    continue
                break
            except ValueError:
                print('정수를 입력해야 합니다.')
        time.sleep(0.5)    
        b=(cb+ub)
        w=b%2
        if w==1:
            w='홀'
        elif w==0:
            w='짝'
        print('베팅이 완료되었습니다.')
        time.sleep(0.5)
        print('')
        print('*'*50)
        choose=input('홀짝 중 하나를 고르시오.: ')
        while choose not in ['홀','짝']:
            print('다시 입력하십시오.')
            choose=input('홀짝 중 하나를 고르시오.: ')
        time.sleep(0.5)
        print(f'당신은 <{choose}>를 입력하였습니다.')
        print('*'*50)
        time.sleep(0.5)
        print('3')
        time.sleep(0.5)
        print('2')
        time.sleep(0.5)
        print('1')
        time.sleep(0.5)
        print('')
        print(f'컴퓨터는 <{cb}>원을 베팅하였습니다.')
        time.sleep(0.5)
        print(f'결과는 <{b%10}>으로 <{w}수>입니다.')
        print('')
        print('*'*50)
        time.sleep(0.5)
        if choose==w:
            print('맞췄습니다.')
            print('')
            print('*'*50)
            if ub<=cb: #유저가 더 적은 돈을 걺
                time.sleep(0.5)
                print(f'움직이는 돈은 당신의 <{ub}>원입니다.')
                usm+=ub
                csm-=ub 
                time.sleep(0.5)     
                print(f'당신은 <{ub}>원을 얻었습니다.')
            else: #유저가 더 큰 돈을 걺
                time.sleep(0.5)
                if csm-ub<10000:
                    print('아쉽게도')  
                print(f'움직이는 돈은 컴퓨터의 <{cb}>원입니다.')          
                usm+=cb
                csm-=cb
                time.sleep(0.5)
                print(f'당신은 <{cb}>원을 얻었습니다.')
        elif choose!=w:        
            print('틀렸습니다.')
            print('')
            print('*'*50)
            if cb<=ub:   #컴퓨터가 더 적은 돈을 걺
                time.sleep(0.5)
                if usm-ub<10000:
                    print('다행이도')
                print(f'움직이는 돈은 컴퓨터의 <{cb}>원입니다.')              
                csm+=cb
                usm-=cb
                time.sleep(0.5)
                print(f'당신은 <{cb}>원을 잃었습니다.')
            else:
                time.sleep(0.5)
                if usm-cb<10000:
                    if usm-ub>=10000:
                        print('다행이도')
                print(f'움직이는 돈은 당신의 <{ub}>원입니다.')            
                csm+=ub
                usm-=ub
                time.sleep(0.5)
                print(f'당신은 <{ub}>원을 잃었습니다.')
        
        time.sleep(0.5)
        print('')
        if csm<10000:
            print('@'+'-'*48+'@')
            print('<컴퓨터>는 더 이상 참여 불가능합니다.')
            print('<당신>의 승리입니다.')
            print('@'+'-'*48+'@')
            break
        if usm<10000:
            print('@'+'-'*48+'@')
            print('<당신>은 더 이상 참여 불가능합니다.')
            print('<컴퓨터>의 승리입니다.')
            print('@'+'-'*48+'@')
            break

if __name__ == "__main__":
    main()